from django import forms

from users.models import Profile


class ImageUploadForm(forms.ModelForm):
    # upload = forms.ImageField(
    #     widget=forms.FileInput(attrs={"class": 'account-file-input', "hidden": "true"})
    # )
    class Meta:
        model = Profile
        fields = ['image']
