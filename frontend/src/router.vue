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

Vue.use(VueRouter);

export default new VueRouter({
  mode: 'history',
  base: __dirname,
  routes: [
    {path: '/', component: LandingContent},
    {path: '/vacancy', component: VacancyContent},
    {path: '/vacancy-page', component: vacancyPage},
    {path: '/create-vacancy', component: createPage},
    {path: '/create-resume', component: createResume},
    {path: '/profile/applicant', component: Applicant},
    {path: '/profile/employer', component: Employer},
  ],
});
</script>
