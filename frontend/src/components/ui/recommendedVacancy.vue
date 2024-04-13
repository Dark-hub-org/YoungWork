<template>
  <div class="vacancy-list">
    <template v-if="userData.usertype === 'employer'">
      <div
          v-for="response in ListLength"
          :key="response.id"
          class="vacancy-card">
        <p class="vacancy-card__title--resume">{{response.resume_title}}</p>
        <p class="vacancy-card__title--resume">{{response.last_name}} {{response.first_name}}</p>
        <p class="vacancy-card__salary">Ожидаемый доход:
          <template v-if="response.salary">{{response.salary}}</template>
          <template v-else>не указанно</template>
        </p>
        <div class="vacancy-card__btns">
          <template v-if="userData.usertype === 'employer'">
            <router-link
                :to="{ name: 'resume', params: { id: response.id} }"
                class="vacancy-card__response button-orange-another">
              Посмотреть резюме
            </router-link>
            <button
                @click="addedFavorites(response.id)"
                type="button"
                class="vacancy-card__favourites button-orange">
              В избранное
            </button>
          </template>
        </div>
      </div>
    </template>
    <template v-else>
      <div
          v-for="vacancy in ListLength"
          :key="vacancy.id"
          class="vacancy-card">
        <router-link
            :to="{ name: 'vacancy', params: { id: vacancy.id} }"
            tag="a"
            target="_blank"
            class="vacancy-card__title">
          {{ vacancy.job_title }}
        </router-link>
        <ul class="vacancy-card__list">
          <li class="vacancy-card__item">
            <span class="vacancy-card__signature">Требования:</span>
            <span class="vacancy-card__text"> {{ vacancy.requirements }}</span>
          </li>
          <li class="vacancy-card__item">
            <span class="vacancy-card__signature">Задачи:</span>
            <span class="vacancy-card__text"> {{ vacancy.tasks }}</span>
          </li>
          <li class="vacancy-card__item">
            <span class="vacancy-card__signature">Оплата:</span>
            <span v-if="vacancy.salary_min || vacancy.salary_max" class="vacancy-card__text">
          <template
              v-if="vacancy.salary_min && vacancy.salary_max">
            от {{ vacancy.salary_min }} до {{ vacancy.salary_max }}
          </template>
          <template v-else-if="vacancy.salary_min">от {{ vacancy.salary_min }}</template>
          <template v-else>до {{ vacancy.salary_max }}</template>
          рублей
        </span>
          </li>
        </ul>
        <div class="vacancy-card__btns">
          <template v-if="userData.usertype === 'applicant'">
            <button
                v-if="!vacancy.response"
                @click="sendResponse(vacancy)"
                type="button"
                class="vacancy-card__response button-orange-another">
              Откликнуться
            </button>
            <span v-else class="button-orange vacancy__item-btn">Откликнулись</span>
            <button
                v-if="!vacancy.favorite"
                @click="addedFavorites(vacancy.id)"
                type="button"
                class="vacancy-card__favourites button-orange">
              В избранное
            </button>
            <span v-else class="button-orange vacancy__item-btn">В избранном</span>
          </template>
        </div>
      </div>
    </template>
  </div>
</template>

<script>

import axios from "axios";

export default {
  name: 'recommended-vacancy',

  data() {
    return {
      recommendedList: [],
    }
  },
  methods: {

    async sendResponse(vacancy) {
      try {
        const data = {
          vacancy: vacancy.id,
          org: vacancy.created_by,
          created_by: this.userData.usertype,
        }
        await axios.post('/api/response/', data)
        this.recommendedList = this.recommendedList.map(item => item.id === vacancy.id ? {...item, response: true} : {...item})
      } catch(error) {
        console.log(error)
      }
    },

    async addedFavorites(id) {
      try {
        if(this.userData.usertype === 'applicant') {
          await axios.post('/data-favorites/', {vacancy: id})
        } else {
          await axios.post('/data-favorites/', {resume: id})
        }
        this.recommendedList = this.recommendedList.map(item => item.id === id ? {...item, favorite: true} : {...item})
      } catch (error) {
        console.log(error)
      }
    },

    convertVacancies(vacancy, responseVacancy, favoriteVacancy) {
      this.recommendedList = vacancy.map(item => {
        const isVacancy = responseVacancy.includes(item.id)
        const isFavorite = favoriteVacancy.includes(item.id)
        return { ...item, response: isVacancy, favorite: isFavorite};
      });
    },
    async getRecommended() {
      try {
        const response = await axios.get('/api/recommend/')
        if(this.userData.usertype === 'applicant') {
          const responseVacancy = await axios.get(`/applicant/data/${this.userData.id}/`)
          const responseFavoriteVacancy  = await axios.get('/data-favorites/')

          const favoritesVacancy = responseFavoriteVacancy.data.length ? responseFavoriteVacancy.data.map(vacancy => vacancy.id) : []

          this.convertVacancies(response.data, responseVacancy.data.response, favoritesVacancy)
        } else {
          this.recommendedList = response.data
        }
      } catch(error) {
        console.log(error)
      }
    },
  },
  computed: {
    userData() {
      return this.$store.state.userData
    },
    ListLength() {
      if (window.innerWidth > 1440) {
        return this.recommendedList.slice(0, 6)
      }
      return this.recommendedList.slice(0, 4)
    },
  },
  mounted() {
    this.getRecommended()
  }
}
</script>

<style src="@/style/ui/recommendedVacancy.scss" lang="scss" scoped>

</style>
