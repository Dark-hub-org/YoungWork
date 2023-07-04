<template>
  <main class="main">
    <router-view></router-view>
    <span :src="user_data">{{user_data}}</span>
  </main>
</template>
<script>
import axios from "axios"

export default {
  name: "site-content",
  data() {
    return {
        user_data: ''
    }
  },
  mounted(){
    this.getMe()
  },
  methods: {
    getMe() {
        axios.get('/api/v1/users/me')
            .then(response => {
                console.log(response)
                this.user_data = response.data.username
            })
            .catch(error =>{
                console.log(error)
            })
    }
  }
}
</script>

<style lang="scss" scoped>
@import "@/style/main";

.main {
  margin-bottom: 158px;
}

</style>
