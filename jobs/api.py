from django.conf import settings
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail
from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Vacancies
from accounts.models import User
from accounts.serializers import UserSerializer
from .serializers import VacanciesDataSerializer
from django.shortcuts import render
