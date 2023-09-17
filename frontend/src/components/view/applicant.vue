<template>
  <section class="applicant-profile">
    <div class="applicant-profile__wrapper">
      <div class="applicant-profile__left">
        <div class="applicant-profile__top">
          <div class="applicant-profile__photo-wrapper">
            <div
                class="applicant-profile__photo" style="background: #DFDFDF">
            </div>
            <button type="button" class="applicant-profile__edit-btn"></button>
          </div>
          <div class="applicant-profile__data">
            <p class="applicant-profile__data__name text-margin">Александра Андреева</p>
            <p class="applicant-profile__data__age text-margin">19 лет</p>
            <p class="applicant-profile__data__geo">Алтайский край, Барнаул</p>
          </div>
        </div>
        <div class="applicant-profile__line"></div>
        <div class="applicant-profile__main">
          <div class="applicant-profile__btns">
            <button @click="applicantStab = 1" class="applicant-profile__btn" :class="{active: applicantStab === 1}">Обо мне</button>
            <button @click="applicantStab = 2" class="applicant-profile__btn" :class="{active: applicantStab === 2}">Личные данные</button>
          </div>
          <template v-if="applicantStab === 1">
            <div class="applicant-profile__block">
              <h3 class="applicant-profile__subtitle">О вас:</h3>
              <textarea
                  class="applicant-profile__about__text"
                  placeholder="Расскажите, где работали, какие у вас качества, которые могли бы заинтересовать работодателя "
              ></textarea>
              <button type="button" class="applicant-profile__edit-btn field"></button>
            </div>
            <div class="applicant-profile__block">
              <h3 class="applicant-profile__subtitle">Примеры выполненных работ:</h3>
              <div class="applicant-profile__portfolio"></div>
            </div>
          </template>
          <template v-else>
            <div class="applicant-profile__block data">
              <div class="applicant-profile__field">
                <p class="applicant-profile__field__name">Фамилия:</p>
                <input v-model="applicantLastName" type="text" class="applicant-profile__input">
              </div>
              <div class="applicant-profile__field">
                <p class="applicant-profile__field__name">Имя:</p>
                <input v-model.trim="applicantFirstName" type="text" class="applicant-profile__input">
              </div>
              <div class="applicant-profile__field">
                <p class="applicant-profile__field__name">Отчество:</p>
                <input v-model="applicantPatronymic" type="text" class="applicant-profile__input">
              </div>
              <button type="button" class="applicant-profile__edit-btn field"></button>
            </div>
            <div class="applicant-profile__block data">
              <div class="applicant-profile__field">
                <p class="applicant-profile__field__name">День рождения:</p>
                <input v-model="applicantBirthday" type="text" class="applicant-profile__input" v-mask="'##/##/####'">
              </div>
            </div>
            <div class="applicant-profile__block data">
              <div class="applicant-profile__field">
                <p class="applicant-profile__field__name">Пол:</p>
                <div class="applicant-profile__radio-wrapper">
                  <input v-model="applicationSex" type="radio" name="exp" value="men" class="applicant-profile__radio" id="men"
                         checked>
                  <label for="men" class="applicant-profile-filter-label">Мужской</label>
                </div>
                <div class="applicant-profile__radio-wrapper">
                  <input v-model="applicationSex" type="radio" name="exp" value="women" class="applicant-profile__radio" id="women">
                  <label for="women" class="applicant-profile-filter-label">Женщина</label>
                </div>
              </div>
            </div>
            <div class="applicant-profile__block data start">
              <div class="applicant-profile__field">
                <p class="applicant-profile__field__name">Регион:</p>
                <input v-model="applicantRegion" type="text" class="applicant-profile__input">
              </div>
              <div class="applicant-profile__field">
                <p class="applicant-profile__field__name">Город проживания:</p>
                <input v-model="applicantCity" type="text" class="applicant-profile__input">
              </div>
              <button type="button" class="applicant-profile__edit-btn field"></button>
            </div>
            <div class="applicant-profile__block">
              <p class="applicant-profile__field__name">Контакты:</p>
              <div class="applicant-profile__block grid">
                <div class="applicant-profile__field contact">
                  <img
                      src="@/assets/phone-icon.svg"
                      alt="иконка телефона"
                      class="applicant-profile__connection__img">
                  <input
                      v-mask="'+7 (###) ### ##-##'"
                      placeholder="Номер телефона"
                      class="applicant-profile__input connect"
                  v-model="applicantPhoneNumber"/>
                </div>
                <div class="applicant-profile__field contact">
                  <img
                      src="@/assets/email-icon.svg"
                      alt="иконка e-mail"
                      class="applicant-profile__connection__img">
                  <input type="text" class="applicant-profile__input connect" placeholder="Адрес эл.почты" v-model.trim="applicantEmail">
                </div>
                <div class="applicant-profile__field contact">
                  <img
                      src="@/assets/telegram-icon.svg"
                      alt="иконка телеграмма"
                      class="applicant-profile__connection__img">
                  <input type="text" class="applicant-profile__input connect" placeholder="Telegram" v-model="applicantTelegram">
                </div>
                <div class="applicant-profile__field contact">
                  <img
                      src="@/assets/link-icon.svg"
                      alt="иконка ссылки"
                      class="applicant-profile__connection__img">
                  <input type="text" class="applicant-profile__input connect" placeholder="Личный сайт" v-model.trim="applicantWebsite">
                </div>
              </div>
              <button type="button" class="applicant-profile__edit-btn field "></button>
            </div>
          </template>
        </div>
      </div>
      <aside class="applicant-profile__contacts">
        <h3 class="applicant-profile__subtitle">Контакты</h3>
        <div class="applicant-profile__contacts__block">
          <img src="@/assets/telegram-icon.svg" alt="телеграмм иконка" class="applicant-profile__contacts__img">
          <a href="https://t.me" target="_blank" class="applicant-profile__contacts__link">@as8691_1</a>
        </div>
        <div class="applicant-profile__contacts__block">
          <img src="@/assets/email-icon.svg" alt="email иконка" class="applicant-profile__contacts__img">
          <a href="mailto:" class="applicant-profile__contacts__link">sasha-andreeva-1998@list.ru</a>
        </div>
        <div class="applicant-profile__contacts__block">
          <img src="@/assets/telegram-icon.svg" alt="иконка телефона" class="applicant-profile__contacts__img">
          <a href="tel: " class="applicant-profile__contacts__link">+7 999 888 77 66</a>
        </div>
        <div class="applicant-profile__contacts__block">
          <img src="@/assets/link-icon.svg" alt="иконка ссылки" class="applicant-profile__contacts__img">
          <a href="https://dprofile.ru/andreeva_design" target="_blank" class="applicant-profile__contacts__link">https://dprofile.ru/andreeva_design</a>
        </div>
      </aside>
    </div>
  </section>
</template>

<script>
import axios from "axios";
import Vue from "vue";
import VueTheMask from 'vue-the-mask';
Vue.use(VueTheMask);

export default {
name: 'applicant-profile',
  data() {
    return {
      applicantStab: 1,

      applicantPhoto: '',
      applicantFirstName: '',
      applicantLastName: '',
      applicantPatronymic: '',
      applicantBirthday: '',
      applicantRegion: '',
      applicantCity: '',
      applicantPhoneNumber: '',
      applicantTelegram: '',
      applicantWebsite: '',
      applicantEmail: '',
      applicationSex: '',
    }
  },
  methods: {
    submitForm() {
      const applicantData = JSON.stringify({
        applicantPhoto: this.applicantPhoto,
        applicantFirstName: this.applicantFirstName,
      })
      axios.post('', applicantData)
          .then(response => {
            console.log(response)
          })
          .catch(error => {
            console.log(error)
          });
    }
  }
}
</script>

<style src="@/style/applicant.scss" lang="scss" scoped>

</style>