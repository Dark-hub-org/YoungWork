<script>
import Vue from 'vue';
import VueRouter from 'vue-router';

import ViewHome from '@/views/home.vue';
import about from "@/views/about.vue";
import VacancyContent from "@/views/vacancy-content.vue";
import vacancyPage from './views/vacancy-page.vue';
import createResume from '@/views/create-resume.vue';
import Applicant from '@/views/applicant.vue';
import Employer from '@/views/employer.vue';
import UserEdit from '@/views/userEdit.vue';
import resume from "@/views/resume.vue";
import editVacancy from "@/views/edit-vacancy.vue";
import createVacancy from "@/views/create-vacancy.vue";
import favorites from "@/views/the-favorites.vue";
import response from "@/views/response.vue";
import editResume from "@/views/edit-resume.vue";
import privacy from "@/views/privacy.vue";
import userAgreement from "@/views/userAgreement.vue";




Vue.use(VueRouter);

export default new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: ViewHome,
      meta: {
        breadcrumb: 'Главная'
      }
    },// Хабовая
    {
      path: '/vacancy/:id',
      name: "vacancy",
      props: true,
      component: vacancyPage,
      meta: {
        breadcrumb: {
          label: 'Страница вакансии',
          parent: 'vacancies'
        }
      },
    },// Детальная вакансия
    {
      path: '/edit-vacancy/:id',
      name: 'vacancy-edit',
      props: true,
      component: editVacancy,
    }, // редактирование вакансии
    {
      path: '/vacancy/:page',
      name: "vacancies-page",
      component: VacancyContent
    }, // пагинация вакансии
    {
      path: '/vacancy/?search',
      name: "vacancies-filters",
      component: VacancyContent
    }, // поиск по вакансиям
    {
      path: '/vacancy',
      name: "vacancies",
      component: VacancyContent,
      meta: {
        breadcrumb: {
          label: 'Вакансии',
          parent: 'home'
        }
      },
    },// // вакансии хабовая
    {
      path: '/response/:id',
      name: 'response',
      component: response,
      meta: {
        breadcrumb: {
          label: 'Отклики',
          parent: 'home'
        }
      },
    } , // отклики на вакансию
    {
      path: '/favorites',
      name: "favorites-vacancy",
      component: favorites,
      meta: {
        breadcrumb: {
          label: 'Избранное',
          parent: 'home'
        }
      },
    },
    {
      path: '/create-vacancy/',
      name: 'create-vacancy',
      component: createVacancy
    },//Создание вакансии
    {
      path: '/create-resume/',
      component: createResume
    }, //Создать резюме
    {
      path: '/resume/:id',
      name: "resume",
      props: true,
      component: resume,
      meta: {
        breadcrumb: {
          label: 'Резюме',
          parent: 'home'
        }
      },
    },// Детальная резюме
    {
      path: '/edit-resume/:id',
      name: "edit-resume",
      component: editResume,
    },
    {
      path: '/applicant/',
      name: 'applicant',
      props: true,
      component: Applicant,
      meta: {
        breadcrumb: 'Профиль'
      }
    },//Профиль соискателя
    {
      path: '/applicant/edit/',
      name: 'applicant-edit',
      component: UserEdit,
      meta: {
        breadcrumb: 'Профиль'
      }
    },//Редактирование профиля соискателя
    {
      path: '/employer/',
      name: 'employer',
      props: true,
      component: Employer
    },//Профиль работодателя
    {
      path: '/employer/edit/',
      name: 'employer-edit',
      component: UserEdit
    },//Редактирование профиля работодателя
    {
      path: '/about/',
      name: 'the-about',
      component: about,
      meta: {
        breadcrumb: {
          label: 'О сервисе',
          parent: 'home',
        }
      },
    },// о сервисе
    {
      path: '/privacy/',
      name: 'the-privacy',
      component: privacy,
      meta: {
        breadcrumb: {
          label: 'Политика конфиденциальности',
          parent: 'home',
        }
      },
    },// политики конфиденциальности
    {
      path: '/agreement/',
      name: 'user-agreement',
      component: userAgreement,
      meta: {
        breadcrumb: {
          label: 'Пользовательское соглашение',
          parent: 'home',
        }
      },
    },// пользовательское соглашение
  ],
});


const originalPush = VueRouter.prototype.push;

VueRouter.prototype.push = function push(location, onComplete, onAbort) {
  const result = originalPush.call(
      this,
      location,
      onComplete,
      onAbort
  );
  if (result) {
    return result.catch(err => {
      if (err.name !== 'NavigationDuplicated') {
        throw err;
      }
    });
  }
  return result;
};

const originalReplace = VueRouter.prototype.replace;
VueRouter.prototype.replace = function replace(location, onComplete, onAbort) {
  const result = originalReplace.call(
      this,
      location,
      onComplete,
      onAbort
  );
  if (result) {
    return result.catch(err => {
      if (err.name !== 'NavigationDuplicated') {
        throw err;
      }
    });
  }
  return result;
};
</script>
