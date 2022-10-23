from django import forms

from .models import BusinessProfile


class BusinessRegistrationForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3})
    )
    additional_info = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3})
    )
    longitude = forms.DecimalField(
        disabled=True
    )
    latitude = forms.DecimalField(
        disabled=True
    )

    class Meta:
        model = BusinessProfile
        fields = ['name', 'description', 'additional_info', 'image', 'longitude', 'latitude']
