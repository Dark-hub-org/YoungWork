<template>
  <section class="response">
    <div class="wrapper">
      <the-heading title="Отклики на вакансию"></the-heading>
      <p class="response__quantity">Количество откликов: {{ responseUser.length }}</p>
      <div class="response__list">
        <div
            v-for="response in responseUser"
            :key="response.id"
            class="response__item">
          <div class="response__item-left">
            <img v-if="response.avatar" :src='"/img/" + response.avatar' alt="фото соискатель"
                 class="response__item-img">
            <div v-else class="response__item-img"></div>
            <p class="response__item-name">{{ response.first_name }} {{ response.last_name }}</p>
            <p class="response__item-age">{{ response.age }} лет</p>
            <div class="response__item-social">
              <div class="response__item-social__block">
                <a v-if="response.telegram" :href="'https://t.me/' + response.telegram"
                   class="response__item-social__link">
                  <img src="@/assets/telegram-icon.svg" alt="" class="response__item-social__img">
                  <span>@{{ response.telegram }}</span>
                </a>
                <div v-else class="response__item-social__link">
                  <img src="@/assets/telegram-icon.svg" alt="" class="response__item-social__img">
                  <span>Не указанно</span>
                </div>
              </div>
              <div class="response__item-social__block">
                <a v-if="response.email" :href="'mailto:' + response.email" class="response__item-social__link">
                  <img src="@/assets/email-icon.svg" alt="" class="response__item-social__img">
                  <span>{{ response.email }}</span>
                </a>
                <div v-else class="response__item-social__link">
                  <img src="@/assets/email-icon.svg" alt="" class="response__item-social__img">
                  <span>Не указанно</span>
                </div>
              </div>
              <div class="response__item-social__block">
                <a v-if="response.phone_number" :href="'tel:' + response.phone_number"
                   class="response__item-social__link">
                  <img src="@/assets/phone-icon.svg" alt="" class="response__item-social__img">
                  <span>{{ response.phone_number }}</span>
                </a>
                <div v-else class="response__item-social__link">
                  <img src="@/assets/phone-icon.svg" alt="" class="response__item-social__img">
                  <span>Не указанно</span>
                </div>
              </div>
              <div class="response__item-social__block">
                <a v-if="response.website" :href="response.website" target="_blank"
                   class="response__item-social__link response__item-social__site">
                  <img src="@/assets/link-icon.svg" alt="" class="response__item-social__img">
                  <span>{{ response.website }}</span>
                </a>
                <div v-else class="response__item-social__link">
                  <img src="@/assets/link-icon.svg" alt="" class="response__item-social__img">
                  <span>Не указанно</span>
                </div>
              </div>
            </div>
          </div>
          <div class="response__item-right">
            <div class="response__item-top">
              <p class="response__item-title">
                <template v-if="response.resume?.resume_title">{{ response.resume?.resume_title }}</template>
                <template v-else>Не заданно</template>
              </p>
              <p class="response__item-exp">Опыт:
                <template v-if="response.resume?.experience">{{ response.resume?.experience }}</template>
                <template v-else>Не заданно</template>
              </p>
            </div>
            <div class="response__item-block">
              <p class="response__item-subtitle">Навыки:</p>
              <div class="response__item-about">
                <ul class="response__item-skills">
                  <li
                      class="response__item-skill"
                      v-for="skill in response.resume?.skills"
                      :key="skill">
                    <p>{{ skill }}</p>
                  </li>
                </ul>
              </div>
            </div>
            <div class="response__item-block">
              <p class="response__item-subtitle">Об исполнителе:</p>
              <div v-if="response.about" class="response__item-about" v-html="response.about">
              </div>
              <div v-else class="response__item-about">
                <p>Не заданно</p>
              </div>
            </div>
            <div class="response__item-bottom">
              <button
                  v-if="response.response.result === 'new_response'"
                  @click="SendInvitation(response)"
                  type="button"
                  class="button-orange-another response__item-response">Пригласить на интервью
              </button>
              <span v-else class="button-orange response__item-response">Приглашение отправленно</span>
              <button
                  v-if="!response.favorite"
                  @click="addedFavorites(response.resume.id)"
                  type="button"
                  class="button-orange-another response__item-response">В избранное
              </button>
              <span v-else class="button-orange response__item-response">В избранном</span>
              <button @click="goResume(response.response.id, response.resume.id)" class="response__item-profile">
                Резюме
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "axios";
import TheHeading from "@/components/ui/heading.vue";

export default {
  name: 'response-vacancy',
  components: {TheHeading},
  data() {
    return {
      responseUser: [],
      vacancyId: this.$route.params.id,
    }
  },
  methods: {
    async getResponse(id) {
      try {
        const response = await axios.get(`/api/all-response/${id}`)
        const responseFavorite = await axios.get('/data-favorites/')
        const favoritesList = responseFavorite.data.length ? responseFavorite.data.map(item => item.id) : []
        this.formatterResponseUsers(response.data, favoritesList)
      } catch (error) {
        console.log(error)
      }
    },
    formatterResponseUsers(response, favorite) {
      this.responseUser = response.users.map(item => {
        const age = this.computedUserAge(item)
        return {...item, age: age}
      })

      this.responseUser.map(item => {
        const matchingResume = response.resumes.find(resume => resume.created_by === item.id);
        const matchingResponse = response.response.find(response => response.created_by === item.id)
        if (matchingResume) {
          item.resume = matchingResume;
        }
        if (matchingResponse) {
          item.response = matchingResponse
        }
        const isFavorite = favorite.includes(item.resume.id)
        item.favorite = isFavorite
        console.log(isFavorite)
      })
    },
    async SendInvitation(response) {
      try {
        await axios.get(`/api/chat/${response.id}/get-or-create/`)
        await axios.patch('/api/accept/', {vacancy_response: response.response.id, resume: response.resume.id, result: 'accepted_response',})
        this.responseUser = this.responseUser.map(item => {
          if (item.id === response.id) {
            return { ...item, response: { ...item.response, result: 'accepted_response' } };
          } else {
            return item;
          }
        });
        console.log(response)
      } catch (error) {
        console.log(response)
        console.log(error)
      }
    },
    async addedFavorites(id) {
      try {
        await axios.post('/data-favorites/', {resume: id})
        this.responseUser = this.responseUser.map(item => item.resume.id === id ? {...item, favorite: true} : {...item})
      } catch (error) {
        console.log(error)
      }
    },
    async goResume(id, resumeId) {
      try {
        await axios.post('/api/view/', {vacancy_response: id})
        this.$router.push(`/resume/${resumeId}`)
      } catch (error) {
        console.log(error)
      }
    },
    computedUserAge(user) {
      const now = new Date();
      const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
      const userBirth = new Date(user.date_of_birth);
      const dateBirth = new Date(today.getFullYear(), userBirth.getMonth(), userBirth.getDate());
      const age = today.getFullYear() - userBirth.getFullYear();
      return today < dateBirth ? age - 1 : age
    },
  },
  mounted() {
    this.getResponse(this.$route.params.id)
  },

}
</script>

<!--<style src="@/style/page/response.scss" lang="scss">-->

<!--</style>-->