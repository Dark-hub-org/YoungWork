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
    {path: '/', component: LandingContent},//Основа
    {path: '/vacancies', component: VacancyContent},//Все вакансии
    {path: '/vacancy-page', component: vacancyPage},//Полный лист вакансии
    {path: '/create-vacancy', component: createPage},//Создание вакансии
    {path: '/create-resume', component: createResume},//Создать резюме
    {path: '/profile/applicant/', component: Applicant},//Профиль соискателя
    {path: '/profile/employer/', component: Employer},//Профиль работодателя
    {path: '/profile/edit', component: UserEdit},//Редактирование профиля
  ],
});
</script>
