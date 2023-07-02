<template>
  <div id="app">
    <site-header></site-header>
    <site-content></site-content>
    <site-footer></site-footer>
  </div>
</template>

<style lang="scss">

</style>
<script setup>
import SiteHeader from "@/components/view/site-header.vue"
import SiteContent from "@/components/view/site-content.vue"
import SiteFooter from "@/components/view/site-footer.vue"
</script>

<script>
import axios from "axios"

export default{
    name: 'App',
    beforeCreate(){
        this.$store.commit("initializeStore")

        const access = this.$store.state.access

        if ( access ) {
            axios.defaults.headers.common['Authorization'] = "JWT " + access
        } else {
            axios.defaults.headers.common['Authorization'] = ''
        }

    }
}
</script>
