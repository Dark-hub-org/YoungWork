<template>
  <div>
    <section class="top">
      <div class="wrapper top__wrapper">
        <h1 class="top__title">Сервис по поиску работы для подростков </h1>
        <div class="top__block">
          <div class="top__block-item">
            <img src="@/assets/vacancy/vacancy-1.png" alt="it профессии" class="top__block-img">
            <div class="top__block-content">
              <router-link
                  to="/"
                  tag="a"
                  active-class="active"
                  class="button-orange-another top__block-content__link">
                Перейти
              </router-link>
              <h3 class="top__block-content__title">IT-профессии</h3>
            </div>
          </div>
          <div class="top__block-item">
            <img src="@/assets/vacancy/vacancy-2.png" alt="строительные профессии" class="top__block-img">
            <div class="top__block-content">
              <router-link
                  to="/"
                  tag="a"
                  active-class="active"
                  class="button-orange-another top__block-content__link">
                Перейти
              </router-link>
              <h5 class="top__block-content__title white">Строительные профессии</h5>
            </div>
          </div>
          <div class="top__block-item">
            <img src="@/assets/vacancy/vacancy-3.png" alt="работа с детьми" class="top__block-img">
            <div class="top__block-content">
              <router-link
                  to="/"
                  tag="a"
                  active-class="active"
                  class="button-orange-another top__block-content__link">
                Перейти
              </router-link>
              <h5 class="top__block-content__title white">Работа с детьми</h5>
            </div>
          </div>
        </div>
        <div class="top__search">
          <div class="top__search-wrapper">
            <input type="text" class="top__search-input" placeholder="найти вакансию">
            <button type="button" class="top__search-btn"></button>
          </div>
          <button
              @click="isFilterVisible = true"
              type="button"
              class="top__search-filter-btn">
            <span class="text">Фильтр</span>
          </button>
        </div>
      </div>
    </section>
    <section class="vacancy">
      <div class="wrapper">
        <p class="vacancy__quantity">
          {{quantityVacancies}} <template v-if="quantityVacancies <= 4 && quantityVacancies !== 0">вакансии</template> <template v-else>вакансий</template> <template v-if="requestValue !== ''">“{{requestValue}}”</template>
        </p>
        <div class="vacancy__content">
          <the-filters
              :class="{active: isFilterVisible}"
              @click="openFilters"
              @closeFilters="closeFilters"
              class="vacancy__filters">
          </the-filters>
          <div class="vacancy__list" :class="{hidden: isFilterVisible}">
            <div v-if="vacancies === []" class="vacancy__preloader"></div>
            <div
                v-else class="vacancy__item"
                v-for="vacancy in vacancies"
                :key="vacancy.id">
              <div class="vacancy__item-header">
                <div class="vacancy__item-content">
                  <router-link
                      :to="{ name: 'vacancy', params: { id: vacancy.id} }"
                      tag="a"
                      target="_blank"
                      class="vacancy__item-title">
                    {{ vacancy.job_title }}
                  </router-link>
                  <p class="vacancy__item-salary" >
                    <template
                        v-if="vacancy.salary_min && vacancy.salary_max">
                        от {{ vacancy.salary_min }} до {{vacancy.salary_max}}
                    </template>
                    <template v-else-if="vacancy.salary_min">от {{ vacancy.salary_min }}</template>
                    <template v-else>до {{vacancy.salary_max}}</template>
                     рублей
                  </p>
                </div>
                <img src="@/assets/vacancy/company-logo.svg" alt="логотип компании">
              </div>
              <div class="vacancy__item-info">
                <div class="vacancy__item-block">
                  <p class="vacancy__item-text vacancy__item-company">ООО ЦТД</p>
                  <p class="vacancy__item-text">Владивосток</p>
                </div>
                <div class="vacancy__item-block">
                  <p class="vacancy__item-text">Опыт работы: {{vacancy.required_experience}}</p>
                  <p class="vacancy__item-text vacancy__item-text--type">{{ vacancy.type }}</p>
                </div>
                <div class="vacancy__item-block vacancy__item-block--description">
                  <p class="vacancy__item-text">
                    <pre class="vacancy__item-subtitle">Задачи: </pre>
                    <span class="vacancy__item-subtitle-text" v-html="vacancy.description"> </span>
                  </p>
                  <p class="vacancy__item-text"><span class="vacancy__item-subtitle">Требования:</span> хорошее понимание UI/UX базы; понимание всех нюансов разработки современных сайтов.</p>
                </div>
              </div>
              <div class="vacancy__item-btns">
                <button class="button-orange-another vacancy__item-btn">Откликнуться</button>
                <button class="button-orange vacancy__item-btn">В избранное</button>
              </div>
            </div>
            <div class="vacancy__list-pagination">
              <button
                  v-for="pageNumber in totalPage"
                  :key="pageNumber"
                  @click="getVacancies(pageNumber)"
                  :class="{active: pageNumber === Number(currentPage)}"
                  class="vacancy__list-page">{{pageNumber}}</button>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>

import TheFilters from "@/components/ui/filter.vue";
import axios from "axios";

export default {
  name: 'vacancy-content',
  components: {TheFilters},

  data() {
    return {
      isFilterVisible: false,
      vacancies: [],
      quantityVacancies: 0,
      currentPage: 1,
      pageQuantityMax: 2,
      requestValue: '',
    }
  },
  methods: {
    openFilters() {
      this.isFilterVisible = true
    },
    closeFilters() {
      this.isFilterVisible = false
    },
    async getVacancies(page) {
      try {
        const response = await axios.get(`/api/v1/vac?page=${page}`);
        this.vacancies = response.data.results;
        this.quantityVacancies = response.data.count;
        this.currentPage = page;

        // Проверка, изменился ли маршрут
        const route = page === 1 ? '/vacancy/' : `/vacancy/page/${this.currentPage}/`;
        if (this.$route.path !== route) {
          this.$router.push(route);
        }

        window.scrollTo(0, 0);
      } catch (error) {
        console.error(error);
      }
    },
  },
  computed: {
    totalPage() {
      return Math.ceil(this.quantityVacancies / this.pageQuantityMax)
    },
  },
  mounted() {
    this.getVacancies(this.currentPage);
  },
}

</script>

<style src="@/style/vacancy.scss" lang="scss" scoped>

</style>