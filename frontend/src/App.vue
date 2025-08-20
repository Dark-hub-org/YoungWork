<template>
  <div id="app">
    <site-header></site-header>
    <site-content></site-content>
    <site-footer></site-footer>
  </div>
</template>

<script setup>
import SiteHeader from "@/components/layout/site-header.vue"
import SiteContent from "@/components/layout/site-content.vue"
import SiteFooter from "@/components/layout/site-footer.vue"
</script>

<script>
import axios from "axios"

export default {
  name: 'App',
  data() {
    return {
      connection: null,
    }
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
  },
  mounted() {
    if (this.$store.state.access.length) {
      setInterval(() => {
        this.getAccess()
      }, 149000)
    }

  },
  created() {
    if (this.$store.state.access.length) {
      this.setUserData()
    }
  },
  beforeCreate() {

    this.$store.commit("initializeStore")

    const access = this.$store.state.access

    if (access) {
      axios.defaults.headers.common['Authorization'] = "JWT " + access
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  },
}
</script>
<style src="@/style/style.scss" lang="scss"></style>
