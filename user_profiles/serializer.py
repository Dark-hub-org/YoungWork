from rest_framework import serializers

from .models import Applicant


class ApplicantDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = "__all__"
