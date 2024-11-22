from django import forms

from .models import Contract
from clients.models import Client


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = [
            "title",
            "service",
            "documentation",
            "end_date",
            "budget",
            "client",
        ]
        widgets = {
            "documentation": forms.FileInput(attrs={"class": "custom-upload"}),
        }

    end_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
    )

    client = forms.ModelChoiceField(
        queryset=Client.objects.filter(is_active=False),
    )


class ContractUpdateForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = [
            "title",
            "documentation",
            "end_date",
            "budget",
        ]
        widgets = {
            "documentation": forms.FileInput(attrs={"class": "custom-upload"}),
        }

    end_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
    )
