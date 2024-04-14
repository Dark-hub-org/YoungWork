from rest_framework import serializers
from .models import Applicant, Employer, Employer_image, Applicant_image


class ApplicantDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ["portfolio", "response"]


class ApplicantDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = ["portfolio", "response"]


class EmployerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer_image
        fields = ['employer_image']


class EmployerDetailSerializer(serializers.ModelSerializer):
    achievements = EmployerImageSerializer(many=True, read_only=True)

    class Meta:
        model = Employer
        fields = ["title_org", "photo_org", "inn", "status_valid", "achievements", ]


class EmployerDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = ["title_org", ]


class CreateApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = "__all__"


class CreateEmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = "__all__"
