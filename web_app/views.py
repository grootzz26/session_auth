from django.shortcuts import render
from .models import Device, Session, User
import logging
from django.views.decorators.http import require_http_methods
from .forms import DeviceRegisterForm, UserCreationForm
from .helpers import generate_device_id, generating_client_key
from .helpers import required_valid_session
from .ressponses import Result
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .session_cache import set_cache

# Create your views here.

Logger = logging.getLogger("session_auth.web_app.helpers")
STATUS_SUCCESS = "SUCCESS"
STATUS_FAILURE = "FAILED"
STATUS_INVALID_SESSION_ID = "ERR_INVALID_SESSION_ID"


@require_http_methods(["POST"])
@method_decorator(csrf_exempt, name="dispatch")
def register_device(request):
    """View function to load the device info into device tablr."""

    form = DeviceRegisterForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        device_id = generate_device_id(
            data["os"], data["os_version"], data["make"], data["model"], data["profile"]
        )
        Logger.info("generating device id : %s", device_id)
        device_obj, created = Device.objects.get_or_create(**data, device_id=device_id)
        if created:
            Logger.info("generating new client key")
        else:
            Logger.info("renewing client key for the device_id %s", device_obj.id)

        client_key = generating_client_key(device_obj.device_id)
        ip_address = 0
        if client_key:
            session_params = {
                "user": None,
                "client_key": client_key,
                "device": device_obj,
                "ip_address": ip_address,
            }
            session = Session.objects.create(**session_params)
            extra_fields = {
                "client_key": session.client_key,
                "devide_id": session.device.device_id,
            }
            result = Result(
                200, STATUS_SUCCESS, "successfully registered", extra_fields
            )
            return result.http_response(int(request.POST.get("pretty", 0)))
    else:
        return Result(200, STATUS_FAILURE, "Failure", extra_fields={}).http_response(
            int(request.POST.get("pretty", 0))
        )


@require_http_methods(["POST"])
@method_decorator(csrf_exempt, name="dispatch")
@required_valid_session
def sign_up(request, session):
    """Handles the User registration."""
    if session:
        try:
            if session.user:
                Logger.info("user already logged in for this session")
                return
            form = UserCreationForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                user = User.objects.create(**data)
        except:
            pass

        extra_fields = {
            "user": user.mobile_no,
            "session": session.id,
            "client_key": session.client_key,
        }

        result = Result(
            200, STATUS_SUCCESS, "user registration succesfully", extra_fields
        )

        return result.http_response()


@require_http_methods(["POST"])
@method_decorator(csrf_exempt, name="dispatch")
@required_valid_session
def sign_in(request, session, key):
    """Handles the user login."""
    if session:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.get(mobile_no=data["mobile_no"])
            if not session.user and user:
                # log in
                session.user = user
                session.save()
                if session.device:
                    session.device.user = user
                    session.device.save()
                set_cache(key, session, from_view=True)

                return Result(
                    200, STATUS_SUCCESS, "sign_in successfully"
                ).http_response()


@require_http_methods(["POST"])
@method_decorator(csrf_exempt, name="dispatch")
@required_valid_session
def sign_out(request, session, key):
    """Handles the user logout from our app."""

    if session and session.user:
        # log out
        session.user = None
        session.save()
        set_cache(key, session, from_view=True)
        return Result(200, STATUS_SUCCESS, "successfully logged out").http_response()
