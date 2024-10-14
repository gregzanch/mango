from django import forms
from django.core.exceptions import ValidationError
from .models import Country, Mango

def validate_name(value):
    if value == '':
        raise ValidationError("The name must not be empty")


class NewMangoForm(forms.Form):
    class Meta:
        model = Mango
        fields = ["name", "country"]

    _all_countries = Country.objects.all()
    name = forms.CharField(max_length=200, min_length=1, strip=True, empty_value='New Mango')
    country = forms.ChoiceField(choices=_all_countries)

    def clean(self):
        cleaned_data = super().clean()
