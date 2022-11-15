from django.db import models

# Create your models here.


class User(models.Model):
    """ This model class holds the data of user. """

    name = models.CharField(max_length=50, null=True, blank=True)
    mobile_no = models.CharField(max_length=20, null=True, blank=True)
    smc = models.CharField(max_length=30, null=True, blank=True)
    email_id = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now_add=True)


class Device(models.Model):
    """ This models holds the details of devices. """

    name = models.CharField(max_length=50, null=True, blank=True)
    make = models.CharField(max_length=50, null=True, blank=True)
    os_version = models.CharField(max_length=50, null=True, blank=True)
    model = models.CharField(max_length=50, null=True, blank=True)
    serial_no = models.CharField(max_length=50, null=True, blank=True)
    profile = models.CharField(max_length=50, null=True, blank=True)
    device_id = models.CharField(max_length=50, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now_add=True)


class Session(models.Model):
    """ This model class holds the session details for the client. """

    api_session = "authentication.session_auth.web_app.api.{}"

    device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True)
    client_key = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    ip_address = models.CharField(max_length=50, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
