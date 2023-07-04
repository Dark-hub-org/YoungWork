<script>
import Vue from 'vue';
import VueRouter from 'vue-router';

import LandingContent from '@/components/view/landing-content'
import VacancyContent from "@/components/view/vacancy-content.vue";

Vue.use(VueRouter);

export default new VueRouter({
  mode: 'history',
  base: __dirname,
  routes: [
    {path: '/', component: LandingContent},
    {path: '/vacancys', component: VacancyContent},
  ],
});
</script>
