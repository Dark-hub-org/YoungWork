<script>
import Vue from 'vue';
import VueRouter from 'vue-router';

import LandingContent from '@/components/view/landing-content';
import VacancyContent from "@/components/view/vacancy-content.vue";
import vacancyPage from './components/view/vacancy-page.vue';
import createResume from '@/components/view/create-resume.vue';
import Applicant from '@/components/view/applicant.vue';
import Employer from '@/components/view/employer.vue';
import UserEdit from '@/components/view/userEdit.vue';
import resume from "@/components/view/resume.vue";
import editVacancy from "@/components/view/edit-vacancy.vue";
import createVacancy from "@/components/view/create-vacancy.vue";
import favorites from "@/components/view/the-favorites.vue";
import response from "@/components/view/response.vue";
import editResume from "@/components/view/edit-resume.vue";
import about from "@/components/view/about.vue";


Vue.use(VueRouter);

export default new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: LandingContent,
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
