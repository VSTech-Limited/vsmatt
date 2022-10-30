from django import forms

from core.models import Contact, MyLocation


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

class MyLocationForm(forms.ModelForm):
    class Meta:
        model = MyLocation
        fields = "__all__"