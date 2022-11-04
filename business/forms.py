from django import forms

from .models import BusinessProfile, BusinessBranch


class BusinessRegistrationForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3})
    )
    additional_info = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3})
    )
    longitude = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': True})
        # disabled=True
    )
    latitude = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': True})
        # disabled=True
    )

    class Meta:
        model = BusinessProfile
        fields = ['name', 'description', 'additional_info', 'image', 'latitude', 'longitude']


class BranchRegistrationForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}), required=False
    )
    additional_info = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}), required=False
    )
    longitude = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': True})
        # disabled=True
    )
    latitude = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': True})
        # disabled=True
    )

    class Meta:
        model = BusinessBranch
        fields = ['name', 'description', 'category', 'additional_info', 'image', 'latitude', 'longitude']
