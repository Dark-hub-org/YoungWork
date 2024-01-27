<script>
import Vue from 'vue';
import VueRouter from 'vue-router';

import LandingContent from '@/components/view/landing-content';
import VacancyContent from "@/components/view/vacancy-content.vue";
import vacancyPage from './components/view/vacancy-page.vue';
import createPage from '@/components/view/create-page.vue';
import createResume from '@/components/view/create-resume.vue';
import Applicant from '@/components/view/applicant.vue';
import Employer from '@/components/view/employer.vue';
import UserEdit from '@/components/ui/userEdit.vue';

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
      path: '/vacancy/:id', name: "vacancy", props: true, component: vacancyPage, meta: {
        breadcrumb: {
          label: 'Страница вакансии',
          parent: 'vacancies'
        }
      },
    },// Детальная вакансия
    {path: '/vacancy/:page', name: "vacancies-page", component: VacancyContent}, // вакансии хабовая
    {
      path: '/vacancy', name: "vacancies", component: VacancyContent, meta: {
        breadcrumb: {
          label: 'Вакансии',
          parent: 'home'
        }
      },
    },// вакансии
    {path: '/create-vacancy', component: createPage},//Создание вакансии
    {path: '/create-resume', component: createResume},//Создать резюме
    {
      path: '/applicant/:id',
      name: 'applicant',
      props: true,
      component: Applicant},//Профиль соискателя
    {
      path: '/employer/:id',
      name: 'employer',
      props: true,
      component: Employer},//Профиль работодателя
    {path: '/profile/edit', component: UserEdit},//Редактирование профиля
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
