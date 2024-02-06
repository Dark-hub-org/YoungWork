from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserDataSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    surname = serializers.CharField()
    date_of_birth = serializers.CharField()
    citizenship = serializers.CharField()
    region = serializers.CharField()
    city = serializers.CharField()
    about = serializers.CharField()
    about_work = serializers.CharField()
    telegram = serializers.CharField()
    website = serializers.CharField()
    phone_number = serializers.CharField()

    def update(self, instance, validated_data):
        instance.first_name = validated_data.first_name.get("first_name", instance.first_name)
        instance.last_name = validated_data.last_name.get("last_name", instance.last_name)
        instance.surname = validated_data.surname.get("surname", instance.surname)
        instance.date_of_birth = validated_data.date_of_birth.get("date_of_birth", instance.date_of_birth)
        instance.citizenship = validated_data.citizenship.get("citizenship", instance.citizenship)
        instance.region = validated_data.region.get("region", instance.region)
        instance.city = validated_data.city.get("city", instance.city)
        instance.about = validated_data.about.get("about", instance.about)
        instance.about_work = validated_data.about_work.get("about_work", instance.about_work)
        instance.telegram = validated_data.telegram.get("telegram", instance.telegram)
        instance.website = validated_data.website.get("website", instance.website)
        instance.phone_number = validated_data.phone_number.get("phone_number", instance.phone_number)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = "__all__"
