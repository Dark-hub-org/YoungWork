<template>
  <div id="app">
    <site-header/>
    <site-content></site-content>
    <site-footer></site-footer>
  </div>
</template>

<script>

import SiteHeader from "@/components/view/site-header.vue";
import SiteContent from './components/view/site-content';
import SiteFooter from './components/view/site-footer';

export default {
  name: 'App',
  components: {
    SiteHeader,
    SiteContent,
    SiteFooter,
  },
}
</script>

<style>
</style>
