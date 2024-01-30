<template>
  <section class="edit">
    <div class="wrapper edit__wrapper">
      <form class="edit__data">
        <h2 class="edit__data-title">Личные данные</h2>
        <div class="edit__data-block">
          <div class="edit__data-field">
            <p class="edit__data-field__name">Фамилия:</p>
            <input
                v-model="userData.lastName"
                :class="{'error': errorFields.lastname}"
                v-restrict-input-length="120"
                type="text"
                class="edit__data-input">
            <span
                class="edit__data-field__error"
                :class="{ active: errorFields.lastname }">Заполните поле</span>
          </div>
          <div class="edit__data-field">
            <p class="edit__data-field__name">Имя:</p>
            <input
                v-model="userData.firstName"
                :class="{'error': errorFields.firstname}"
                v-restrict-input-length="120"
                type="text"
                class="edit__data-input">
            <span
                class="edit__data-field__error"
                :class="{ active: errorFields.firstname }">Заполните поле</span>
          </div>
          <div class="edit__data-field">
            <p class="edit__data-field__name">Отчество:</p>
            <input
                v-model="userData.surname"
                :class="{'error': errorFields.surname}"
                v-restrict-input-length="120"
                type="text"
                class="edit__data-input">
            <span
                class="edit__data-field__error"
                :class="{ active: errorFields.surname }">Заполните поле</span>
          </div>
        </div>
        <div class="edit__data-block">
          <div class="edit__data-field">
            <p class="edit__data-field__name">Дата рождения:</p>
            <input
                v-model="userData.dateOfBirth"
                :class="{'error': errorFields.dateOfBirth}"
                placeholder="0000/00/00"
                type="text"
                class="edit__data-input"
                v-mask="'####/##/##'">
            <span
                class="edit__data-field__error"
                :class="{ active: errorFields.dateOfBirth}">Заполните поле</span>
          </div>
        </div>
        <div class="edit__data-block">
          <div class="edit__data-field">
            <p class="edit__data-field__name">Гражданство:</p>
            <input v-model="userData.citizenship" type="text" class="edit__data-input">
          </div>
        </div>
        <div class="edit__data-block">
          <div class="edit__data-field">
            <p class="edit__data-field__name">Регион:</p>
            <input v-model="userData.region" type="text" class="edit__data-input">
          </div>
          <div class="edit__data-field">
            <p class="edit__data-field__name">Город проживания:</p>
            <input v-model="userData.city" type="text" class="edit__data-input">
          </div>
        </div>
        <div class="edit__data-block">
          <p class="edit__data-field__name">Контакты:</p>
          <div class="edit__data-field contact">
            <img
                src="../../assets/phone-icon.svg"
                alt="иконка телефона"
                class="edit__data-img">
            <input
                v-model="userData.phoneNumber"
                v-mask="'+7 (###) ### ##-##'"
                placeholder="Номер телефона"
                class="edit__data-input contact"/>
          </div>
          <div class="edit__data-field contact">
            <img
                src="../../assets/email-icon.svg"
                alt="иконка e-mail"
                class="edit__data-img">
            <input
                v-model="userData.email"
                type="text"
                placeholder="Адрес эл.почты"
                class="edit__data-input contact" >
          </div>
          <div class="edit__data-field contact">
            <img
                src="../../assets/telegram-icon.svg"
                alt="иконка телеграмма"
                class="edit__data-img">
            <input
                v-model="userData.telegram"
                type="text"
                placeholder="Telegram"
                class="edit__data-input contact">
          </div>
          <div class="edit__data-field contact">
            <img
                src="../../assets/link-icon.svg"
                alt="иконка ссылки"
                class="edit__data-img">
            <input
                v-model="userData.website"
                type="text"
                class="edit__data-input contact" placeholder="Личный сайт">
          </div>
        </div>
        <h2 class="edit__data-title">О вас</h2>
        <div class="edit__data-block about">
          <div class="edit__data-field about">
            <p class="edit__data-field__name">Название организации:</p>
            <textarea class="edit__data-input about" v-model="userData.about"></textarea>
          </div>
        </div>
        <div class="edit__data-block about">
          <div class="edit__data-field about">
            <p class="edit__data-field__name">Краткое описание вашей деятельности:</p>
            <textarea class="edit__data-input about" v-model="userData.aboutWork"></textarea>
          </div>
        </div>
      </form>
      <aside class="edit__side">
        <span class="edit__side-title">Вы в режиме редактирования</span>
        <button @click="submitUserData" class="button-green edit__side-button">Сохранить</button>
        <button @click="closeEditProfile" class="edit__side-link">Отменить изменения</button>
      </aside>
    </div>
  </section>
</template>

<script>

import Vue from "vue";
import VueTheMask from "vue-the-mask";
import axios from "axios";

Vue.use(VueTheMask);

export default {
  name: 'user-edit',
  data() {
    return {
      errorFields: {
        firstname: false,
        lastname: false,
        surname: false,
        dateOfBirth: false
      },
      userData: {},
    }
  },
  methods: {
    closeEditProfile() {
      this.$router.push(`/${this.userData.usertype}/${this.userData.id}`)
    },
    async submitUserData() {
      try {
        if(this.checkValidData()) {
          const response = await axios.get(`/${this.userData.usertype}/edit/${this.userData.id}/`, this.userData)
          console.log(response)
        } else {
          this.checkValidData()
        }
      } catch (error) {
        console.log(error)
      }
    },
    validateField(value) {
      return value === null;
    },
    checkValidData() {
      this.errorFields.firstname = this.validateField(this.userData.firstName)
      this.errorFields.lastname = this.validateField(this.userData.lastName)
      this.errorFields.surname = this.validateField(this.userData.surname)
      this.errorFields.dateOfBirth = this.validateField(this.userData.dateOfBirth)
      return Object.values(this.errorFields).every((error) => !error)
    },
    updateEditedUserData() {
      this.userData = { ...this.$store.state.userData };
    },
  },
  watch: {
    '$store.state.userData': {
      handler: 'updateEditedUserData',
      immediate: true,
    },
  },
}
</script>

<style src="@/style/userEdit.scss" lang="scss" scoped>

</style>