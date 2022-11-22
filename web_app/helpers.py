import logging
from .session_cache import get_api_session
import hashlib


def generate_device_id(os, os_v, make, model, profile):
    """Generating device id for the device>"""

    fields = [os, os_v, make, model, profile]
    f = ":".join([str(i) for i in fields])
    return f


def generating_client_key(device_id):
    """generating client key for user."""
    key = hashlib.sha256(str.encode())
    return key.hexdigest()


def required_valid_session(view_func):
    """checking valid session for the user."""

    def decorator(request, *args, **kwargs):
        session = get_api_session(request)
        if session:
            return view_func(session, *args, **kwargs)

    return decorator
