<template>
  <div>
    <section class="inner">
      <div class="wrapper wrapper-inner">
        <h1 class="inner-title">Сервис по поиску работы для подростков </h1>
        <div class="inner-slider">
          <div class="inner-slider__item">
            <img src="@/assets/vacancy/vacancy-1.png" alt="it профессии" class="slider-item__img">
            <div class="inner-slider__content">
              <router-link
                  to="/"
                  tag="a"
                  active-class="active"
                  class="button-orange-another slider-item__link">
                Перейти
              </router-link>
              <h3 class="inner-slider__title">IT-профессии</h3>
            </div>
          </div>
          <div class="inner-slider__item">
            <img src="@/assets/vacancy/vacancy-2.png" alt="строительные профессии" class="slider-item__img">
            <div class="inner-slider__content">
              <router-link
                  to="/"
                  tag="a"
                  active-class="active"
                  class="button-orange-another slider-item__link">
                Перейти
              </router-link>
              <h5 class="inner-slider__title white">Строительные профессии</h5>
            </div>
          </div>
          <div class="inner-slider__item">
            <img src="@/assets/vacancy/vacancy-3.png" alt="работа с детьми" class="slider-item__img">
            <div class="inner-slider__content">
              <router-link
                  to="/"
                  tag="a"
                  active-class="active"
                  class="button-orange-another slider-item__link">
                Перейти
              </router-link>
              <h5 class="inner-slider__title white">Работа с детьми</h5>
            </div>
          </div>
        </div>
        <div class="inner-search">
          <div class="inner-search__wrapper">
            <input type="text" class="inner-search__input" placeholder="найти вакансию">
            <button type="button" class="inner-search__btn"></button>
          </div>
          <button
              @click="isFilterVisible = true"
              type="button"
              class="inner-filter-btn">
            <span class="text">Фильтр</span>
          </button>
        </div>
      </div>
    </section>
    <section class="vacancy">
      <div class="wrapper vacancy-wrapper">
        <h3 class="vacancy-quantity">
          {{quantityVacancies}} вакансий <template v-if="requestValue !== ''">“{{requestValue}}”</template>
        </h3>
        <div class="vacancy-filter-and-list">
          <the-filters
              :class="{active: isFilterVisible}"
              @click="openFilters"
              @closeFilters="closeFilters">
          </the-filters>
          <div class="vacancy-list">
            <div class="vacancy-item"
                 v-for="vacancy in vacancies"
                 :key="vacancy.id">
              <div class="vacancy-item__header">
                <div class="vacancy-item__block">
                  <p class="vacancy-item__title" >{{ vacancy.job_title }}</p>
                  <p class="vacancy-item__salary" >
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
              <div class="vacancy-item__info">
                <div class="vacancy-item__block">
                  <p class="vacancy-item__text vacancy-item__company">ООО ЦТД</p>
                  <p class="vacancy-item-text">Владивосток</p>
                </div>
                <div class="vacancy-item__block">
                  <p class="vacancy-item__text">Опыт работы: {{vacancy.required_experience}}</p>
                  <p class="vacancy-item__text vacancy-item__experince">{{ vacancy.type }}</p>
                </div>
                <div class="vacancy-item__block">
                  <p class="vacancy-item__text">
                    <pre class="vacancy-item__subtitle">Задачи: </pre>
                    <span class="vacancy-item__subtitle-text" v-html="vacancy.description"> </span>
                  </p>
                  <p class="vacancy-item__text"><span class="vacancy-item__subtitle">Требования:</span> хорошее
                    понимание UI/UX базы; понимание всех нюансов разработки современных сайтов.</p>
                </div>
              </div>
              <div class="vacancy-item__btns">
                <button class="button-orange-another">Откликнуться</button>
                <button class="button-orange">В избранное</button>
              </div>
            </div>
            <div class="vacancy-list__pagination">
              <button
                  v-for="pageNumber in totalPage"
                  :key="pageNumber"
                  @click="getVacanciesPage(pageNumber)"
                  :class="{active: pageNumber === Number(currentPage)}"
                  class="vacancy-list__page">{{pageNumber}}</button>
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
      pageQuantityMax: 0,
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
    getVacanciesPage(page) {
      axios.get(`/api/v1/vac?page=${page}`)
          .then(response => {
            this.vacancies = response.data.results
            this.quantityVacancies = response.data.count
            this.pageQuantityMax = response.data.results.length
            this.currentPage = page
          })
          .catch(error => {
            console.log(error)
          })
    },
  },
  computed: {
    // totalPage() {
    //   return Math.ceil(this.quantityVacancies / this.pageQuantityMax)
    // },
  },
  mounted() {
    this.getVacanciesPage(this.currentPage);
  },
}

</script>

<style src="@/style/vacancy.scss" lang="scss" scoped>

</style>