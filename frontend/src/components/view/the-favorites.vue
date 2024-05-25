<template>

    <section class="favorites">
      <div class="wrapper">
        <the-heading :title=headingTitle ></the-heading>
        <template v-if="userData.usertype === 'applicant'">
          <div v-if="favoriteList.length" class="favorites__list">
            <div
                class="favorites__item"
                v-for="vacancy in favoriteList"
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
                <img v-if="vacancy.com_logo" class="favorites__item-logo" :src='"/img/" + vacancy.com_logo' alt="логотип компании">
              </div>
              <div class="favorites__item-info">
                <div class="favorites__item-block">
                  <p class="favorites__item-text favorites__item-company">{{ vacancy.company_name }}</p>
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
                <button @click="deleteFavorite(vacancy.id)" class="button-orange-another">Удалить</button>
              </div>
            </div>
          </div>
          <div v-else>
            <p class="favorites__text">Избранных вакансий нет</p>
            <router-link class="button-orange-another favorites__link" to="/vacancy" tag="a">Перейти к вакансиям</router-link>
          </div>
        </template>
        <template v-else>
          <div v-if="favoriteList.length" class="favorites__list">
            <div
                v-for="response in favoriteList"
                :key="response.id"
                class="response__item">
              <div class="response__item-left">
                <img v-if="response.avatar" :src='"/img/" + response.avatar' alt="фото соискатель" class="response__item-img">
                <div v-else class="response__item-img"></div>
                <p class="response__item-name">{{response.first_name}} {{response.last_name}}</p>
                <p v-if="response.age" class="response__item-age">{{response.age}} лет</p>
                <div class="response__item-social">
                  <div class="response__item-social__block">
                    <a v-if="response.telegram" :href="'https://t.me/' + response.telegram" class="response__item-social__link">
                      <img src="@/assets/telegram-icon.svg" alt="" class="response__item-social__img">
                      <span>@{{response.telegram}}</span>
                    </a>
                    <div v-else class="response__item-social__link">
                      <img src="@/assets/telegram-icon.svg" alt="" class="response__item-social__img">
                      <span>Не указанно</span>
                    </div>
                  </div>
                  <div class="response__item-social__block">
                    <a v-if="response.email" :href="'mailto:' + response.email" class="response__item-social__link">
                      <img src="@/assets/email-icon.svg" alt="" class="response__item-social__img">
                      <span>{{response.email}}</span>
                    </a>
                    <div v-else class="response__item-social__link">
                      <img src="@/assets/email-icon.svg" alt="" class="response__item-social__img">
                      <span>Не указанно</span>
                    </div>
                  </div>
                  <div class="response__item-social__block">
                    <a v-if="response.phone_number" :href="'tel:' + response.phone_number" class="response__item-social__link">
                      <img src="@/assets/phone-icon.svg" alt="" class="response__item-social__img">
                      <span>{{response.phone_number}}</span>
                    </a>
                    <div v-else class="response__item-social__link">
                      <img src="@/assets/phone-icon.svg" alt="" class="response__item-social__img">
                      <span>Не указанно</span>
                    </div>
                  </div>
                  <div class="response__item-social__block">
                    <a v-if="response.website" :href="response.website" target="_blank" class="response__item-social__link response__item-social__site">
                      <img src="@/assets/link-icon.svg" alt="" class="response__item-social__img">
                      <span>{{response.website}}</span>
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
                    <template v-if="response?.resume_title">{{response.resume_title}}</template>
                    <template v-else>Не заданно</template>
                  </p>
                  <p class="response__item-exp">Опыт:
                    <template v-if="response.experience">{{response.experience}}</template>
                    <template v-else>Не указанно</template>
                  </p>
                </div>
                <div class="response__item-block">
                  <p class="response__item-subtitle">Навыки:</p>
                  <div class="response__item-about">
                    <ul v-if="response.skills.length" class="response__item-skills">
                      <li
                          class="response__item-skill"
                          v-for="skill in response.skills"
                          :key="skill">
                        <p>{{skill}}</p>
                      </li>
                    </ul>
                    <p v-else>Не указанно</p>
                  </div>
                </div>
                <div class="response__item-block">
                  <p class="response__item-subtitle">Об исполнителе:</p>
                  <div v-if="response.about" class="response__item-about" v-html="response.about">
                  </div>
                  <div v-else class="response__item-about">
                    <p>Не указанно</p>
                  </div>
                </div>
                <div class="response__item-bottom">
                  <router-link :to="{ name: 'resume', params: { id: response.id} }" tag="a" class="response__item-profile">Перейти резюме</router-link>
                  <button @click="deleteFavorite(response.id)" type="button" class="button-orange response__item-response">Удалить</button>
                </div>
              </div>
            </div>
          </div>
          <div v-else>
            <p class="favorites__text">Избранных резюме нет</p>
          </div>
        </template>
      </div>
    </section>
</template>

<script>
import axios from "axios";
import TheHeading from "@/components/ui/heading.vue";

export default {
  name: 'the-favorites',
  components: {TheHeading},
  data() {
    return {
      favoriteList: [],
    }
  },
  methods: {
    async deleteFavorite(id) {
      try {
         await axios.delete(`/favorites-del/${id}/` )
          this.favoriteList = this.favoriteList.filter(item => item.id !== id)
      } catch (error) {
        console.log(error)
      }
    },
    async getFavorite() {
      try {
        const response = await axios.get('/data-favorites/')
        this.favoriteList = response.data
      } catch (error) {
        console.log(error)
      }
    },
    async SendInvitation(id, resumeId) {
      try {
        await axios.patch('/api/accept/', {vacancy_response: id, resume: resumeId, result: 'accepted_response',})
        this.favoriteList = this.favoriteList.map(item => item.id === id ? {...item, favorite: true} : {...item})
      } catch (error) {
        console.log(error)
      }
    },
  },
  computed: {
    userData() {
      return this.$store.state.userData
    },
    headingTitle() {
      return this.userData.usertype === 'applicant' ? "Избранные вакансии" : "Избранные резюме"
    }
  },
  mounted() {
    this.getFavorite()
  }
}
</script>

<!--<style src="@/style/page/favorites.scss" lang="scss" scoped>-->

<!--</style>-->