from .models import Notification

from jobs.models import Vacancies
from resume.models import Resume
from response.models import Response


def create_notification(request, type_of_notification, vacancy_id=None, resume_id=None, vacancyresponse_id=None):
    try:
        created_for = Vacancies.objects.filter(id=vacancy_id).get()
        created_for = created_for.created_by.user
    except Exception as e:
        created_for = Resume.objects.filter(id=resume_id).get()
        created_for = created_for.created_by.user

    if type_of_notification == 'vacancy_favorites':
        created_for = request.user
        body = f'Вы добавили вакансию в избранное!'
    elif type_of_notification == 'new_vacancy_response':
        body = f'На вашу вакансию откликнулись!'
    elif type_of_notification == 'resume_favorites':
        created_for = request.user
        body = f'Вы добавили резюме в избранное!'
    elif type_of_notification == 'accepted_vacancy_response':
        vacancy_response = Response.objects.get(pk=vacancyresponse_id)
        created_for = vacancy_response.created_by
        body = f'{Response.org} хочет пригласить вас на интервью. Ожидайте уведомления в социальных сетях!'
    elif type_of_notification == 'rejected_vacancy_response':
        vacancy_response = Response.objects.get(pk=vacancyresponse_id)
        created_for = vacancy_response.created_by
        body = f'{Response.org} компания не готова вас приглосить!'

    notification = Notification.objects.create(
        body=body,
        type_of_notification=type_of_notification,
        created_by=request.user,
        resume_id=resume_id,
        vacancy_id=vacancy_id,
        created_for=created_for,
        vacancyresponse_id=vacancyresponse_id,
    )

    return notification
