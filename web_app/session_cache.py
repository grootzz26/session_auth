from django.core.cache import caches
from session_auth.settings import CACHES
from .models import Session


def default_cache():
    return True if "default" in CACHES else False


def get_cache(cache_key):
    ecache = default_cache()
    if ecache:
        return ecache.get(cache_key)


def set_cache(key, value, ttl=3600):
    ecache = default_cache()
    if ecache:
        return ecache.set(key, value, ttl)


def get_api_session(request):
    client_key = request.META.get("client_key")
    cache_key = Session.api_session.format(client_key)
    session = get_cache(cache_key)
    if session:
        return session
    session_obj = Session.objects.get(client_key=client_key)
    if session_obj:
        set_cache(cache_key, session)
    return session
