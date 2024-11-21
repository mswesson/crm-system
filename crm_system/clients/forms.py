from django import forms

from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            "first_name",
            "last_name",
            "middle_name",
            "phone_number",
            "email",
            "advertising_company",
            "notes",
            "next_interaction_date",
        ]
