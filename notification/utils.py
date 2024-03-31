from .models import Notification

from jobs.models import Vacancies
from jobs.models import Response
from accounts.models import User


def create_notification(request, type_of_notification, vacancy_id=None, vacancy_response_id=None):
    created_for = None

    user = request.user.id

    if type_of_notification == 'vacancy_favorites':
        created_for = User.objects.filter(pk=user).get()
        body = f'Вы добавили вакансию: {request.vacancy} в избранное!'
    elif type_of_notification == 'vacancy_comment':
        body = f'{request.user.name} оставил коментарий вашей вакансии!'
    elif type_of_notification == 'new_vacancy_response':
        created_for = User.objects.filter(pk=user).get()
        body = f'{request.user.first_name} откликнулся на вашу вакансию!'
    elif type_of_notification == 'accepted_vacancy_response':
        vacancyresponse = Response.objects.get(pk=vacancy_response_id)
        created_for = vacancyresponse.created_by
        body = f'{request.user.name} компания хочет пригласить вас на интервью!'
    elif type_of_notification == 'rejected_vacancy_response':
        vacancyresponse = Response.objects.get(pk=vacancy_response_id)
        created_for = vacancyresponse.created_by
        body = f'{request.user.name} компания не готова вас приглосить!'

    notification = Notification.objects.create(
        body=body,
        type_of_notification=type_of_notification,
        created_by=request.user,
        vacancy_id=vacancy_id,
        created_for=created_for
    )

    return notification
