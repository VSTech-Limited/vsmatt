from django import forms

from .models import BranchReview, BusinessProfile, BusinessBranch, Contact


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
        fields = ['name', 'description', 'customer_service_number', 'category', 'additional_info', 'image', 'latitude',
                  'longitude']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        exclude = ('is_addressed','business')


class BranchReviewForm(forms.ModelForm):
    class Meta:
        model = BranchReview
        fields = ('rating', "review")
