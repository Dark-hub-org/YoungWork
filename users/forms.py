from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser
from django.contrib.auth.models import Group


class CustomUserCreationForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all())

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name_1', 'last_name_1', 'short_name')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name_1', 'last_name_1', 'short_name')
