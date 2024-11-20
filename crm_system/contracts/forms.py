from django import forms

from .models import Contract


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = [
            "title",
            "service",
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
