from django.urls import path
from .views import register_device, sign_in, sign_up, sign_out

urlpatterns = [
    path("registerDevice/", register_device),
    path("signUp", sign_up),
    path("signIn", sign_in),
    path("signOut", sign_out),
]