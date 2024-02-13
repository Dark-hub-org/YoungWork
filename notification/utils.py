from .models import Notification

from jobs.models import Vacancies
from accounts.models import VacancyResponse


def create_notification(request, type_of_notification, vacancy_id=None, vacancyresponse_id=None):
    created_for = None

    if type_of_notification == 'vacancy_favorites':
        body = f'{request.user.name} добавил вакансию: {Vacancies.job_title} в избранное!'
        vacancy = Vacancies.objects.get(pk=vacancy_id)
        created_for = vacancy.created_by
    elif type_of_notification == 'vacancy_comment':
        body = f'{request.user.name} оставил коментарий вашей вакансии!'
        vacancy = Vacancies.objects.get(pk=vacancy_id)
        created_for = vacancy.created_by
    elif type_of_notification == 'new_vacancy_response':
        vacancyresponse = VacancyResponse.objects.get(pk=vacancyresponse_id)
        created_for = vacancyresponse.created_for
        body = f'{request.user.name} откликнулся на вашу вакансию!'
    elif type_of_notification == 'accepted_vacancy_response':
        vacancyresponse = VacancyResponse.objects.get(pk=vacancyresponse_id)
        created_for = vacancyresponse.created_for
        body = f'{request.user.name} компания хочет пригласить вас на интервью!'
    elif type_of_notification == 'rejected_vacancy_response':
        vacancyresponse = VacancyResponse.objects.get(pk=vacancyresponse_id)
        created_for = vacancyresponse.created_for
        body = f'{request.user.name} компания не готова вас приглосить!'

    notification = Notification.objects.create(
        body=body,
        type_of_notification=type_of_notification,
        created_by=request.user,
        vacancy_id=vacancy_id,
        created_for=created_for
    )

    return notification
