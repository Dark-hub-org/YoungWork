<script>
import Vue from 'vue';
import VueRouter from 'vue-router';

import LandingContent from './components/view/landing-content'



Vue.use(VueRouter);

export default new VueRouter({
  mode: 'history',
  base: __dirname,
  routes: [
    {path: '/', component: LandingContent},
  ],
});
</script>


