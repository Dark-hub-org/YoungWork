<template>
  <section class="vacancy">
    <div class="wrapper vacancy__wrapper">
      <the-heading title="Сервис по поиску работы для молодежи"></the-heading>
      <div class="vacancy__main">
        <div class="vacancy__info">
          <p class="vacancy__info-title">{{vacancyData.job_title}}</p>
          <p class="vacancy__info-salary">
            <template
                v-if="vacancyData.salary_min && vacancyData.salary_max">
              от {{ vacancyData.salary_min }} до {{ vacancyData.salary_max }}
            </template>
            <template v-else-if="vacancyData.salary_min">от {{ vacancyData.salary_min }}</template>
            <template v-else>до {{ vacancyData.salary_max }}</template>
            рублей
          </p>
          <div class="vacancy__info-block">
            <p class="vacancy__info-text">Опыт работы: {{vacancyData.required_experience}}</p>
            <p class="vacancy__info-text">{{vacancyData.type}}</p>
          </div>
          <div v-if="userData.usertype === 'applicant'" class="vacancy__info-btns">
            <button v-if="!vacancyData.response" @click="sendResponse(vacancyData)" class="button-orange-another">Откликнуться</button>
            <span v-else class="button-orange vacancy__item-btn">Вы уже откликнулись</span>
            <button v-if="!vacancyData.favorite" @click="addedFavorites(vacancyData.id)" class="button-orange">В избранное</button>
            <span v-else class="button-orange vacancy__item-btn">Добавленно в избранное</span>
          </div>
        </div>
        <div class="vacancy__employer">
          <img v-if="vacancyData.com_logo" :src='"/img/" + vacancyData.com_logo' alt="логотип компании" class="vacancy__employer-img">
          <p class="vacancy__employer-company">{{vacancyData.title_org}}</p>
          <p class="vacancy__info-text">{{vacancyData.citizenship}}</p>
          <p class="vacancy__info-text">{{vacancyData.phone_number}}</p>
          <p class="vacancy__info-text text--green">{{vacancyData.last_name}} {{vacancyData.first_name}}</p>
        </div>
        <div class="vacancy__description" v-html="vacancyData.description"></div>
        <div class="vacancy__bottom">
          <p class="vacancy__bottom-date">Вакансия была опубликована {{vacancyData.timestamp}}</p>
          <template v-if="userData.usertype === 'applicant'">
            <button v-if="!vacancyData.response" class="button-orange-another">Откликнуться</button>
            <span v-else class="button-orange vacancy__item-btn">Вы уже откликнулись</span>
          </template>
        </div>
      </div>
      <h3 class="section-title">Рекомендуем вам</h3>
      <the-recommendations></the-recommendations>
    </div>
  </section>
</template>
<script>
import axios from "axios";
import TheHeading from "@/components/ui/heading.vue";
import TheRecommendations from "@/components/ui/recommendations.vue";

export default {
  name: 'vacancy-page',
  components: {TheRecommendations, TheHeading},
  props: ['id'],
  data() {
    return {
      vacancyData: {},
    };
  },
  methods: {
    convertVacancy(vacancy, responseVacancy, favoriteVacancy) {
      const isVacancy = responseVacancy.includes(vacancy.id)
      const isFavorite = favoriteVacancy.includes(vacancy.id)
      this.vacancyData = {...vacancy, response: isVacancy, favorite: isFavorite}
    },
    async getVacancyData(id) {
      try {
        const response = await axios.get(`/api/vac/${id}`);
        if(this.userData.usertype === 'applicant') {
          const responseVacancy = await axios.get(`/applicant/data/${this.userData.id}/`)
          const responseFavoriteVacancy  = await axios.get('/data-favorites/')
          const favoritesVacancy = responseFavoriteVacancy.data.length ? responseFavoriteVacancy.data.map(vacancy => vacancy.id) : []
          this.convertVacancy(response.data, responseVacancy.data.response, favoritesVacancy)
        } else {
          this.vacancyData = response.data
        }

      } catch (error) {
        console.log(error)
      }
    },
    async sendResponse(vacancy) {
      try {
        this.$store.dispatch('sendResponse', vacancy)
        this.vacancyData = {...this.vacancyData, response: true}
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
    userData() {
      return this.$store.state.userData
    }
  },
  mounted() {
    this.getVacancyData(this.id)

  },
}
</script>
<style src="@/style/vacancy-page.scss" lang="scss" scoped>

</style>
<style>
.vacancy__description {
  h2 {
    font-size: 32px;
    font-weight: 600;
    line-height: 98.023%;
    letter-spacing: -1.6px;
    &:not(:first-of-type) {
      margin-top: 64px;
    }
  }
  p {
    margin-top: 32px;
    font-size: 24px;
    line-height: 120%;
    letter-spacing: -1.2px;
  }
  @media(max-width: 1024px) {
    h2 {
      font-size: 32px;
      font-weight: 600;
      line-height: 98.023%;
      letter-spacing: -1.6px;
      &:not(:first-of-type) {
        margin-top: 48px;
      }
    }
  }
  @media(max-width: 450px) {
    h2 {
      font-size: 18px;
      letter-spacing: -0.9px;
      &:not(:first-of-type) {
        margin-top: 24px;
      }
    }
    p {
      margin-top: 16px;
      font-size: 14px;
      letter-spacing: -0.7px;
    }
  }
}
</style>