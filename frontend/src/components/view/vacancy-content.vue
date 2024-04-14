<template>
  <div>
    <section class="top">
      <div class="wrapper top__wrapper">
        <the-heading title="Сервис по поиску работы для молодежи"></the-heading>
        <div class="top__search">
          <the-search @search-vacancy="fetchVacancies"></the-search>
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
          <template v-if="requestValue"> “{{ requestValue }}”</template>
        </p>
        <div class="vacancy__content">
          <the-filters
              :class="{active: isFilterVisible}"
              @click="openFilters"
              @closeFilters="closeFilters"
              @filter-vacancy="fetchVacancies"
              class="vacancy__filters">
          </the-filters>
          <div class="vacancy__list" :class="{hidden: isFilterVisible}">
            <div
                class="vacancy__item"
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
                  <p v-if="vacancy.salary_min || vacancy.salary_max" class="vacancy__item-salary">
                    <template
                        v-if="vacancy.salary_min && vacancy.salary_max">
                      от {{ vacancy.salary_min }} до {{ vacancy.salary_max }}
                    </template>
                    <template v-else-if="vacancy.salary_min">от {{ vacancy.salary_min }}</template>
                    <template v-else>до {{ vacancy.salary_max }}</template>
                    рублей
                  </p>
                </div>
                <img v-if="vacancy.com_logo" class="vacancy__item-logo" :src='"/img/" + vacancy.com_logo' alt="логотип компании">
              </div>
              <div class="vacancy__item-info">
                <div class="vacancy__item-block">
                  <p class="vacancy__item-text vacancy__item-company">{{ vacancy.company_name }}</p>
                  <p class="vacancy__item-text">{{vacancy.region}}</p>
                </div>
                <div class="vacancy__item-block">
                  <p class="vacancy__item-text">Опыт работы: {{ vacancy.required_experience }}</p>
                  <div class="vacancy__item-list">
                    <p v-for="item in vacancy.graph" :key="item" class="vacancy__item-text vacancy__item-text--type">{{ item }}</p>
                  </div>
                </div>
                <div class="vacancy__item-block vacancy__item-block--description">
                  <p class="vacancy__item-text">
                    <pre class="vacancy__item-subtitle">Задачи: </pre>
                    <span class="vacancy__item-subtitle-text" v-html="vacancy.tasks"> </span>
                  </p>
                  <p class="vacancy__item-text">
                    <pre class="vacancy__item-subtitle">Требования: </pre>
                    <span class="vacancy__item-subtitle-text" v-html="vacancy.requirements"> </span>
                  </p>
                </div>
              </div>
              <div class="vacancy__item-btns">
                <template v-if="userData.usertype === 'applicant'">
                  <button v-if="!vacancy.response" @click="sendResponse(vacancy)" class="button-orange-another vacancy__item-btn">
                    Откликнуться</button>
                  <span v-else class="button-orange vacancy__item-btn">Вы уже откликнулись</span>
                  <button v-if="!vacancy.favorite" @click="addedFavorites(vacancy.id)" class="button-orange vacancy__item-btn">В избранное</button>
                  <span v-else class="button-orange vacancy__item-btn">Добавленно в избранное</span>
                </template>
              </div>
            </div>
            <paginate
                v-if="vacancies.length > 0"
                v-model="currentPage"
                :pageCount="totalPage"
                :prevText="''"
                :nextText="''"
                :click-handler="paginateHandler"
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
import TheSearch from "@/components/ui/searchInput.vue";

export default {
  name: 'vacancy-content',
  components: {TheSearch, TheHeading, TheFilters, Paginate},

  data() {
    return {
      id: null,
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
    convertVacancies(vacancy, responseVacancy, favoriteVacancy) {
      this.vacancies = vacancy.map(item => {
        const isVacancy = responseVacancy.includes(item.id)
        const isFavorite = favoriteVacancy.includes(item.id)
        return { ...item, response: isVacancy, favorite: isFavorite};
      });

    },

    async fetchVacancies(searchValue, filtersValue, pageNum = 1) {
      try {
        const route = searchValue ? `search=${searchValue}&` : '';
        const pageRoute = pageNum === 1 ? '' : `page=${pageNum}&`
        const response = await axios.get(`/api/vac/?${pageRoute}${route}${filtersValue}`);
        if(this.userData.usertype === 'applicant') {
          const responseVacancy = await axios.get(`/applicant/data/${this.userData.id}/`)
          const responseFavoriteVacancy  = await axios.get('/data-favorites/')

          const favoritesVacancy = responseFavoriteVacancy.data.length ? responseFavoriteVacancy.data.map(vacancy => vacancy.id) : []

          this.convertVacancies(response.data.results, responseVacancy.data.response, favoritesVacancy)
        } else {
          this.vacancies = response.data.results
        }
        this.quantityVacancies = response.data.count;
        this.currentPage = pageNum;
        this.requestValue = searchValue;
        this.$router.push(`/vacancy/?${pageRoute}${route}${filtersValue}`);
      } catch(error) {
        console.error(error);
      }
    },
    paginateHandler(pageNum) {
      let filter = Object.fromEntries(
          Object.entries(this.$route.query).filter(([key]) => key !== 'search' && key !== 'page')
      );

      filter = Object.keys(filter)
          .map(key => `${key}=${filter[key]}`)
          .join('&');

      const filterRoute = filter !== '=null' ? filter : ''

      this.fetchVacancies(this.$route.query.search, filterRoute, pageNum);
    },
    async sendResponse(vacancy) {
      const data = {
        vacancy: vacancy.id,
        org: vacancy.created_by,
        created_by: this.userData.id,
      }
      try {
        await axios.post('/api/response/', data)
        this.vacancies = this.vacancies.map(item => item.id === vacancy.id ? {...item, response: true} : {...item})
      } catch(error) {
        console.log(error)
      }
    },
    async addedFavorites(id) {
      try {
        await axios.post('/data-favorites/', {vacancy: id})
        this.vacancies = this.vacancies.map(item => item.id === id ? {...item, favorite: true} : {...item})
      } catch (error) {
        console.log(error)
      }
    },
  },
  computed: {
    totalPage() {
      return Math.ceil(this.quantityVacancies / this.pageQuantityMax)
    },
    userData() {
      return this.$store.state.userData
    },
  },

  mounted() {
    const attributeSearch = this.$route.query.search
    const attributePage = this.$route.query.page

    const filter = Object.fromEntries(
        Object.entries(this.$route.query).filter(([key]) => key !== 'search' && key !== 'page')
    );

    const filterRoute = Object.keys(filter)
        .map(key => `${key}=${filter[key]}`)
        .join('&');

    if(attributePage) {
      this.currentPage = +attributePage
    }

    this.fetchVacancies(attributeSearch, filterRoute, this.currentPage);
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

.button-enter-active, .button-leave-active {
  transition: opacity .3s;
}

.button-enter, .button-leave-to {
  opacity: 0;
}
</style>

