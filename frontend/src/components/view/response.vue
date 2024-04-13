<template>
  <section class="response">
    <div class="wrapper">
      <the-heading title="Отклики на вакансию"></the-heading>
      <p class="response__quantity">Количество откликов: {{responseUser.length}}</p>
      <div class="response__list">
        <div
            v-for="response in responseUser"
            :key="response.id"
            class="response__item">
          <div class="response__item-left">
            <img v-if="response.avatar" :src='"/img/" + response.avatar' alt="фото соискатель" class="response__item-img">
            <div v-else class="response__item-img"></div>
            <p class="response__item-name">{{response.first_name}} {{response.last_name}}</p>
            <p class="response__item-age">{{response.age}} лет</p>
            <div class="response__item-social">
              <div class="response__item-social__block">
                <img src="@/assets/telegram-icon.svg" alt="" class="response__item-social__img">
                <a :href="'https://t.me/' + response.telegram" class="response__item-social__link">
                  <template v-if="response.telegram">@{{response.telegram}}</template>
                  <template v-else>Не указанно</template>
                </a>
              </div>
              <div class="response__item-social__block">
                <img src="@/assets/email-icon.svg" alt="" class="response__item-social__img">
                <a :href="'mailto:' + response.email" class="response__item-social__link">
                  <template v-if="response.email">{{response.email}}</template>
                  <template v-else>Не указанно</template>
                </a>
              </div>
              <div class="response__item-social__block">
                <img src="@/assets/phone-icon.svg" alt="" class="response__item-social__img">
                <a :href="'tel:' + response.phone_number" class="response__item-social__link">
                  <template v-if="response.phone_number">{{response.phone_number}}</template>
                  <template v-else>Не указанно</template>
                </a>
              </div>
              <div class="response__item-social__block">
                <img src="@/assets/link-icon.svg" alt="" class="response__item-social__img">
                <a :href="response.website" target="_blank" class="response__item-social__link response__item-social__site">
                  <template v-if="response.website">{{response.website}}</template>
                  <template v-else>Не указанно</template>
                </a>

              </div>
            </div>
          </div>
          <div class="response__item-right">
            <div class="response__item-top">
              <p class="response__item-title">
                <template v-if="response.resume?.resume_title">{{response.resume?.resume_title}}</template>
                <template v-else>Не заданно</template>
                {{response.resume?.resume_title}}
              </p>
              <p class="response__item-exp">Опыт:
                <template v-if="response.resume?.experience">{{response.resume?.experience}}</template>
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
                    <p>{{skill}}</p>
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
              <button type="button" class="button-orange-another response__item-response">Пригласить на интервью</button>
              <button type="button" class="button-orange-another response__item-response">В избранное</button>
              <router-link :to="{ name: 'resume', params: { id: response.resume?.id} }" tag="a" class="response__item-profile">Перейти в профиль</router-link>
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
    }
  },
  methods: {
    async getResponse(id) {
      try {
        const response = await axios.get(`/api/all-response/${id}`)
        console.log(response)
        this.formatterResponseUsers(response.data)
      } catch (error) {
        console.log(error)
      }
    },
    formatterResponseUsers(response) {
      this.responseUser = response.users.map(item => {
        const age = this.computedUserAge(item)
        return {...item, age: age}
      })
      this.responseUser.map(item => {
        const matchingResume = response.resumes.find(resume => resume.created_by === item.id);
        if (matchingResume) {
          item.resume = matchingResume;
        }
      })
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

<style src="@/style/response.scss" lang="scss">

</style>