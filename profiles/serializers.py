from rest_framework import serializers

from .models import Applicant, Employer


class ApplicantDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = "__all__"


class ApplicantDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = "__all__"


class EmployerDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = "__all__"


class EmployerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = "__all__"
