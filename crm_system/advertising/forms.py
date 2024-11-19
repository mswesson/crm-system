from django import forms

from .models import AdvertisingCompany


class AdvertisingCompanyForm(forms.ModelForm):
    class Meta:
        model = AdvertisingCompany
        fields = ["title", "service", "promotion_channel", "budget"]
