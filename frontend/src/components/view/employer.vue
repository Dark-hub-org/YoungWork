<template>
  <user-profile
      :userData="userData"
      :profileText="profileText"
      :userAge="userAge">
    <template v-slot:modal-window>
      <modal-window
          :isVisible="isModalVisible"
          @close="onCloseModalWin">
        <div class="profile__modal-verification">
          <form class="modal-verification__form" :class="{'stepTwo': isVerificationModal}">
            <template v-if="!isVerificationModal">
              <p class="modal-verification__title">Мы заботимся о безопасности наших пользователей.</p>
              <p class="modal-verification__text">Подтверждение ИНН повысит доверие к вашей организации со стороны
                соискателей.</p>
              <p class="modal-verification__text">Введите идентификационный номер налогоплательщика (ИНН):</p>
              <div class="modal-verification__input-wrapper">
                <input
                    v-model="userINN"
                    @input="handlerInput"
                    type="text"
                    placeholder="Например, 987654321098"
                    class="modal-verification__input"
                    :class="{error: isUserINNError}">
                <img v-if="isUserINNError" src="@/assets/error-icon.svg" alt="иконка ошибка" class="modal-verification__error-icon">
                <p v-if="isUserINNError" class="modal-verification__error">Неправильно заполнено поле</p>
                <p class="modal-verification__label">10 цифр</p>
              </div>
              <button @click="checkValidOrganization" type="button" class="modal-verification__btn">Отправить на проверку</button>
            </template>
            <template v-else>
              <p class="modal-verification__title">Отправлено на проверку</p>
              <p class="modal-verification__text">Заявление будет рассмотрено в течение 24 часов.</p>
            </template>
          </form>
        </div>
      </modal-window>
    </template>
    <template v-slot:twoTub>
      <div class="profile__vacancy">
        <p class="profile__subtitle">Активные:</p>
        <swiper
            :slides-per-view="2"
            :space-between="16"
            :loop="false"
            :navigation="true"
            class="profile__slider">
          <swiper-slide
              v-for="vacancy in activeVacancy"
              :key="vacancy.id"
              class="profile__slider-item">
            <p class="profile__slider-title">{{vacancy.job_title}}</p>
            <div class="profile__slider-btns">
              <router-link to="/" tag="a" class="profile__slider-link button-orange-another">Редактировать</router-link>
              <router-link to="/" tag="a" class="button-orange">Отклики</router-link>
            </div>
          </swiper-slide>
        </swiper>
      </div>
      <div class="profile__vacancy">
        <p class="profile__subtitle">Завершенные:</p>
        <swiper
            :slides-per-view="2"
            :space-between="16"
            :loop="false"
            :navigation="true"
            class="profile__slider">
          <swiper-slide
              v-for="vacancy in inactiveVacancy"
              :key="vacancy.id"
              class="profile__slider-item profile__slider-item--inactive">
            <p class="profile__slider-title">{{vacancy.job_title}}</p>
            <div class="profile__slider-btns">
              <router-link  :to="{ name: 'edit-vacancy', params: { id: vacancy.id} }" tag="a" class="profile__slider-link button-orange-another">Редактировать</router-link>
              <router-link to="/" tag="a" class="button-orange">Отклики</router-link>
            </div>
          </swiper-slide>
        </swiper>
      </div>
    </template>
    <template v-slot:verification>
      <div class="profile-verification">
        <template v-if="!userData.status_valid">
          <p class="profile-verification__title">Подтвердите профиль</p>
          <p class="profile-verification__text">Так вы обеспечиваете дополнительную безопасность и доверие пользователя
            к вашей организации</p>
          <button @click="isModalVisible = true" class="profile-verification__button">Подтвердить</button>
        </template>
        <template v-else>
          <p class="profile-verification__title verification">Профиль подтвержден</p>
          <p class="profile-verification__text">Это проверенный работодатель</p>
        </template>
      </div>
    </template>
  </user-profile>
</template>

<script>
import UserProfile from "@/components/ui/userProfile.vue";
import ModalWindow from "@/components/ui/modalWin.vue";

import { Navigation} from 'swiper'
import { SwiperCore, Swiper, SwiperSlide } from 'swiper-vue2'
SwiperCore.use([Navigation])


import axios from "axios";
import 'swiper/swiper-bundle.css'
export default {
  name: 'employer-profile',
  components: {ModalWindow, UserProfile, Swiper, SwiperSlide},
  data() {
    return {
      profileText: {
        buttonText: 'Вакансии',
        placeholders: {
          about: 'Расскажите, где работали, какие у вас качества, которые могли бы заинтересовать работодателя',
          aboutWork: 'Описание выполненных работ',
        },
        portfolioTitle: 'Награды и достижения:',
      },
      breakpoints: {
        850: {
          slidesPerView: 1
        }
      },
      isVerificationModal: false,
      userINN: '',
      keyAPI: '905cbd0ecbf3cfba0e900cbd13edc74e17424177',
      isUserINNError: false,
      isModalVisible: false,
      activeVacancy: [],
      inactiveVacancy: [],
    }
  },
  methods: {
    async checkValidOrganization() {
      try {
        const response = await axios.get(`https://api-fns.ru/api/egr?req=${this.userINN}&key=${this.keyAPI}`)
        const result = response.data.items[0].ЮЛ.Статус
        if(result === 'Действующее') {
          axios.patch(`employer/edit-data/${this.userData.id}/`, JSON.stringify({status_valid: true, inn: this.userINN}))
        } else {
          alert('Error')
        }

      } catch(error) {
        console.log({req: this.userINN,  key: this.keyAPI})
        console.log(error)
      }
    },
    async getVacancyUser() {
        try {
          const activeVacancy = await axios.get('/api/active/vac/')
          const inactiveVacancy = await axios.get('/api/inactive/vac/')
          this.activeVacancy = activeVacancy.data
          this.inactiveVacancy = inactiveVacancy.data
        } catch(error) {
          console.log(error)
        }
    },
    onCloseModalWin() {
      this.isModalVisible = false;
      this.userINN = '';
      this.isUserINNError = false;
      this.isVerificationModal = false
    },
    handlerInput() {
      console.log(new Date())
      if (this.userINN.length > 10) {
        this.userINN = this.userINN.slice(0, 10)
      } else {
        if(this.isUserINNError) {
          this.isUserINNError = false
        }
        this.userINN = this.userINN.replace(/[^0-9]/g, '');
      }

    },
  },
  computed: {
    userAge() {
      const now = new Date();
      const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
      const userBirth = new Date(this.userData.dateOfBirth);
      const dateBirth = new Date(today.getFullYear(), userBirth.getMonth(), userBirth.getDate());
      const age = today.getFullYear() - userBirth.getFullYear();

      return today < dateBirth ? age - 1 : age
    },
    userData() {
      return this.$store.state.userData
    },
  },
  mounted() {
    this.getVacancyUser()
  }
}
</script>

<style src="@/style/employer.scss" lang="scss">

</style>