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
      this.$emit('search-vacancy', this.searchValue)
      this.$router.push(route);
      console.log('1')
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

<style src="@/style/ui/searchInput.scss" lang="scss">

</style>
<style>
.clear-enter-active, .clear-leave-active {
  transition: opacity .15s;
}

.clear-enter, .clear-leave-to {
  opacity: 0;
}
</style>