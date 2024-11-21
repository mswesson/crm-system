from rest_framework import serializers

from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            "first_name",
            "last_name",
            "middle_name",
            "phone_number",
            "email",
            "advertising_company",
        ]

    def validate(self, attrs):
        if Client.objects.filter(
            first_name=attrs["first_name"],
            last_name=attrs["last_name"],
            middle_name=attrs["middle_name"],
            phone_number=attrs["phone_number"],
            email=attrs["email"],
            advertising_company=attrs["advertising_company"],
        ).exists():
            raise serializers.ValidationError(
                "A record with these values already exists"
            )
        return attrs
