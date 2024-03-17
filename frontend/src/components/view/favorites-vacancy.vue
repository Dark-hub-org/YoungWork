<template>

    <section class="favorites">
      <div class="wrapper">
        <h1 class="favorites__title">Избранные вакансии</h1>
        <div class="favorites__list">
          <div
              class="favorites__item"
              v-for="vacancy in favoritesVacancy"
              :key="vacancy.id">
            <div class="favorites__item-header">
              <div class="favorites__item-content">
                <router-link
                    :to="{ name: 'vacancy', params: { id: vacancy.id} }"
                    tag="a"
                    target="_blank"
                    class="favorites__item-title">
                  {{ vacancy.job_title }}
                </router-link>
                <p v-if="vacancy.salary_min || vacancy.salary_max" class="favorites__item-salary">
                  <template
                      v-if="vacancy.salary_min && vacancy.salary_max">
                    от {{ vacancy.salary_min }} до {{ vacancy.salary_max }}
                  </template>
                  <template v-else-if="vacancy.salary_min">от {{ vacancy.salary_min }}</template>
                  <template v-else>до {{ vacancy.salary_max }}</template>
                  рублей
                </p>
              </div>
              <img src="@/assets/vacancy/company-logo.svg" alt="логотип компании" class="favorites__item-logo">
            </div>
            <div class="favorites__item-info">
              <div class="favorites__item-block">
                <p class="favorites__item-text favorites__item-company">ООО ЦТД</p>
                <p class="favorites__item-text">Владивосток</p>
              </div>
              <div class="favorites__item-block">
                <p class="favorites__item-text">Опыт работы: {{ vacancy.required_experience }}</p>
                <div class="favorites__item-list">
                  <p v-for="item in vacancy.graph" :key="item" class="favorites__item-text favorites__item-text--type">{{ item }}</p>
                </div>
              </div>
              <div class="favorites__item-block favorites__item-block--description">
                <p class="favorites__item-text">
                  <pre class="favorites__item-subtitle">Задачи: </pre>
                  <span class="favorites__item-subtitle-text" v-html="vacancy.tasks"> </span>
                </p>
                <p class="favorites__item-text">
                  <pre class="favorites__item-subtitle">Требования: </pre>
                  <span class="favorites__item-subtitle-text" v-html="vacancy.requirements"> </span>
                </p>
              </div>
            </div>
            <div class="favorites__item-btns">

            </div>
          </div>
        </div>
      </div>
    </section>
</template>

<script>
import axios from "axios";

export default {
  name: 'favorites-vacancy',
  data() {
    return {
      favoritesVacancy: [],
    }
  },
  methods: {
    async getFavoritesVacancy() {
      try {
        const response = await axios.get('/data-favorites/')
        this.favoritesVacancy = response.data
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