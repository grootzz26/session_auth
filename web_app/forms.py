from django import forms


class DeviceRegisterForm(forms.Form):
    """Form to hold the payload data of device."""

    os = forms.CharField(max_length=50)
    os_version = forms.CharField(max_length=50)
    make = forms.CharField(max_length=50)
    model = forms.CharField(max_length=50)
    serial_no = forms.CharField(max_length=50)
    profile = forms.CharField(max_length=50)


class UserCreationForm(forms.Form):

    name = forms.CharField(max_length=50)
    email_id = forms.CharField(max_length=50)
    mobile_no = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
    smc = forms.CharField(max_length=50)
