from django import forms
from django.contrib.auth.models import User

from users.models import Profile


class ImageUploadForm(forms.ModelForm):
    # upload = forms.ImageField(
    #     widget=forms.FileInput(attrs={"class": 'account-file-input', "hidden": "true"})
    # )
    class Meta:
        model = Profile
        fields = ['image']


class UserEditForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, max_length=50)
    last_name = forms.CharField(required=True, max_length=50)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class UserProfileInfo(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_number', 'gender')



