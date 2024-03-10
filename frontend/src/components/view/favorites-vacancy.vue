<template>
  <div class="wrapper">
    <section class="favorites__list">
    </section>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'favorites-vacancy',
  data() {
    return {

    }
  },
  methods: {
    async getFavoritesVacancy() {
      try {
        const response = await axios.get('/data-favorites/')
        console.log(response)
      } catch (error) {
        console.log(error)
      }
    },
  },
  mounted() {
    this.getFavoritesVacancy()
  }
}
</script>

<style src="@/style/favorites.scss" lang="scss" scoped>

</style>