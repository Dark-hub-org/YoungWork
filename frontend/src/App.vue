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

export default {
  name: 'App',
  beforeCreate() {
    this.$store.commit("initializeStore")

    const access = this.$store.state.access

    if (access) {
      axios.defaults.headers.common['Authorization'] = "JWT " + access
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  },
  mounted() {
    setInterval(() => {
      this.getAccess()
    }, 59000)
  },
  created() {
    this.setUserData()
  },
  methods: {
    getAccess() {
      const accessData = {
        refresh: this.$store.state.refresh
      }
      axios.post('/api/jwt/refresh', accessData)
          .then(response => {
            const access = response.data.access
            localStorage.setItem("access", access)
            this.$store.commit('setAccess', access)
          })
          .catch(error => {
            console.log(error)
          })
    },
    setUserData() {
      this.$store.dispatch('setUserData')
      this.$store.dispatch('getAuthorization')
    },
  }
}
</script>
