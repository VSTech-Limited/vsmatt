from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-sm bg-secondary border-0 text-center",
                "value": 1
            }
        )
    )
    override = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )


class CartAddSingleProduct(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int,
        widget=forms.HiddenInput,
        initial=1
    )
    override = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )


class CreditCardForm(forms.Form):
    card_number = forms.CharField(max_length=100, required=True)
    card_holder_name = forms.CharField(max_length=100, required=True)
    expiration = forms.CharField(max_length=100, required=True)
    CVV = forms.CharField(max_length=100, required=True)
