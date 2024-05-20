<template>
  <form @submit.prevent="submitSearchVacancy" class="search">
    <input v-model="searchValue" type="search" class="search__input" placeholder="найти вакансию">
    <transition name="clear">
      <button v-if="searchValue" @click="clearSearchValue" type="button" class="search__clear"></button>
    </transition>
    <button type="submit" class="search__submit"></button>
  </form>
</template>

<script>
export default {
  name: 'the-search',
  data() {
    return {
      searchValue: '',
    }
  },
  methods: {
    submitSearchVacancy() {
      const route = this.searchValue ? { path: '/vacancy/', query: { search: this.searchValue } } : '/vacancy';
      const attributePage = this.$route.query.page

      let filter = Object.fromEntries(
          Object.entries(this.$route.query).filter(([key]) => key !== 'search' && key !== 'page')
      );

      filter = Object.keys(filter)
          .map(key => `${key}=${filter[key]}`)
          .join('&');

      const filterRoute = !filter.length ? filter : ''
      console.log(filterRoute)

      this.$emit('search-vacancy', this.searchValue, filterRoute, attributePage)
      this.$router.push(route);
    },
    clearSearchValue() {
      this.searchValue = ''
    }
  },
  mounted() {
    this.searchValue = this.$route.query.search
  }
}
</script>

<!--<style src="@/style/components/searchInput.scss" lang="scss" scoped>-->

<!--</style>-->
<style>
.clear-enter-active, .clear-leave-active {
  transition: opacity .15s;
}

.clear-enter, .clear-leave-to {
  opacity: 0;
}
</style>