<template>
  <div>
    <section class="top">
      <div class="wrapper top__wrapper">
        <the-heading title="Сервис по поиску работы для подростков"></the-heading>
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
          {{ quantityVacancies }}
          <template v-if="quantityVacancies <= 4 && quantityVacancies !== 0">вакансии</template>
          <template v-else>вакансий</template>
          <template v-if="requestValue !== ''">“{{ requestValue }}”</template>
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
                  <p class="vacancy__item-salary">
                    <template
                        v-if="vacancy.salary_min && vacancy.salary_max">
                      от {{ vacancy.salary_min }} до {{ vacancy.salary_max }}
                    </template>
                    <template v-else-if="vacancy.salary_min">от {{ vacancy.salary_min }}</template>
                    <template v-else>до {{ vacancy.salary_max }}</template>
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
                  <p class="vacancy__item-text">Опыт работы: {{ vacancy.required_experience }}</p>
                  <p class="vacancy__item-text vacancy__item-text--type">{{ vacancy.type }}</p>
                </div>
                <div class="vacancy__item-block vacancy__item-block--description">
                  <p class="vacancy__item-text">
                    <pre class="vacancy__item-subtitle">Задачи: </pre>
                    <span class="vacancy__item-subtitle-text" v-html="vacancy.description"> </span>
                  </p>
                  <p class="vacancy__item-text"><span class="vacancy__item-subtitle">Требования:</span> хорошее
                    понимание UI/UX базы; понимание всех нюансов разработки современных сайтов.</p>
                </div>
              </div>
              <div class="vacancy__item-btns">
                <button class="button-orange-another vacancy__item-btn">Откликнуться</button>
                <button class="button-orange vacancy__item-btn">В избранное</button>
              </div>
            </div>
            <paginate
                v-model="currentPage"
                :pageCount="totalPage"
                :prevText="''"
                :nextText="''"
                :click-handler="getVacancy"
                :containerClass="'vacancy__pagination'"
                :page-class="'vacancy__pagination-page'"
                :page-link-class="'vacancy__pagination-link'"
                :prev-class="'vacancy__pagination-prev'"
                :next-class="'vacancy__pagination-next'">
            </paginate>
          </div>
        </div>
      </div>
    </section>
    <section class="recommendation">
      <div class="wrapper">
        <div class="recommendation__block">
          <div class="recommendation__block-item">
            <img src="@/assets/vacancy/vacancy-1.png" alt="it профессии" class="recommendation__block-img">
            <div class="recommendation__block-content">
              <router-link
                  to="/"
                  tag="a"
                  active-class="active"
                  class="button-orange-another top__block-content__link">
                Перейти
              </router-link>
              <h3 class="recommendation__block-content__title">IT-профессии</h3>
            </div>
          </div>
          <div class="recommendation__block-item">
            <img src="@/assets/vacancy/vacancy-2.png" alt="строительные профессии" class="recommendation__block-img">
            <div class="recommendation__block-content">
              <router-link
                  to="/"
                  tag="a"
                  active-class="active"
                  class="button-orange-another recommendation__block-content__link">
                Перейти
              </router-link>
              <h5 class="recommendation__block-content__title white">Строительные профессии</h5>
            </div>
          </div>
          <div class="recommendation__block-item">
            <img src="@/assets/vacancy/vacancy-3.png" alt="работа с детьми" class="recommendation__block-img">
            <div class="recommendation__block-content">
              <router-link
                  to="/"
                  tag="a"
                  active-class="active"
                  class="button-orange-another recommendation__block-content__link">
                Перейти
              </router-link>
              <h5 class="recommendation__block-content__title white">Работа с детьми</h5>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>

import TheFilters from "@/components/ui/filter.vue";
import Paginate from 'vuejs-paginate'
import axios from "axios";
import TheHeading from "@/components/ui/heading.vue";

export default {
  name: 'vacancy-content',
  components: {TheHeading, TheFilters, Paginate},

  data() {
    return {
      isFilterVisible: false,
      vacancies: [],
      quantityVacancies: 0,
      currentPage: 1,
      pageQuantityMax: 10,
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
    async fetchVacancies(pageNum) {
      try {
        const response = await axios.get(`/api/v1/vac?page=${pageNum}`)
        this.vacancies = response.data.results
        this.quantityVacancies = response.data.count
        this.currentPage = pageNum;
      } catch(error) {
        console.log(error)
      }
    },
    async changePage(pageNum) {
      try {
        const route = pageNum === 1 ? '/vacancy' : `/vacancy/?page=${pageNum}`;
        if (this.$route.path !== route) {
          await this.$router.replace(route);
          window.scrollTo(0, 0);
        }
      } catch(error) {
        console.log(error)
      }
    },
    getVacancy(page) {
      this.fetchVacancies(page);
      this.changePage(page)
    },
  },
  computed: {
    totalPage() {
      return Math.ceil(this.quantityVacancies / this.pageQuantityMax)
    },
  },
  mounted() {
    if(this.$route.query.page) {
      this.currentPage = +this.$route.query.page
      this.getVacancy(this.currentPage);
    } else {
      this.getVacancy(this.currentPage);
    }
  },
}

</script>

<style src="@/style/vacancy.scss" lang="scss" scoped>

</style>
<style lang="scss">
@import "../../style/varibles";
.vacancy__pagination-page {
  height: 45px;
  border-radius: 10px;
  border: 3px solid $colorOrangeM;
  font-size: 20px;
  font-weight: 600;
  color: $colorBlack;
  transition: all .3s ease;
  &:hover {
    background-color: $colorOrangeM;
    color: $colorWhite;
  }

  &.active {
    background-color: $colorOrangeM;
    color: $colorWhite;
  }
}

.vacancy__pagination-link {
  display: block;
  padding: 8px;
}

.vacancy__pagination-prev, .vacancy__pagination-next {
  width: 45px;
  height: 45px;
  border-radius: 10px;
  background-color: $colorOrangeM;
  transition: all .3s ease;

  a {
    display: block;
    padding: 10px 15px;
    width: 100%;
    height: 100%;
    background-image: url("../../assets/arrow.svg");
    background-position: center;
    background-repeat: no-repeat;
  }

  &.disabled {
    opacity: .3;
  }

  &:hover {
    background-color: $colorOrangeLight;
  }
}

.vacancy__pagination-prev {
  a {
    transform: rotate(180deg);
  }
}
</style>