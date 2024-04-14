from .models import Notification

from response.models import Response
from accounts.models import User
from jobs.models import Vacancies
from resume.models import Resume


def create_notification(request, type_of_notification, vacancy_id=None, resume_id=None, vacancyresponse_id=None,
                        created_for=None):
    if type_of_notification == 'vacancy_favorites':
        created_for = request.user
        body = f'Вы добавили вакансию в избранное'
    elif type_of_notification == 'new_vacancy_response':
        created_for = Vacancies.objects.filter(id=vacancy_id).get()
        created_for = created_for.created_by.user
        body = f'На вашу вакансию откликнулись'
    elif type_of_notification == 'resume_favorites':
        created_for = Resume.objects.filter(id=resume_id).get()
        created_for = created_for.created_by.user
        body = f'Вы добавили резюме в избранное'
    elif type_of_notification == 'accepted_vacancy_response':
        vacancy_response = Response.objects.filter(pk=vacancyresponse_id).get()
        created_for = User.objects.get(pk=vacancy_response.created_by.pk)
        body = f'{vacancy_response.org.title_org}, хочет пригласить вас на интервью.' \
               f' Ожидайте уведомления в социальных сетях!'
    elif type_of_notification == 'rejected_vacancy_response':
        vacancy_response = Response.objects.filter(pk=vacancyresponse_id).get()
        created_for = vacancy_response.created_by
        body = f'{vacancy_response.org.title_org} компания не готова вас приглосить!'
    elif type_of_notification == 'view_resume':
        vacancy_response = Response.objects.filter(pk=vacancyresponse_id).get()
        created_for = User.objects.get(pk=vacancy_response.created_by.pk)
        body = f'{vacancy_response.org.title_org}, просмотрела, ваше резюме'

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
