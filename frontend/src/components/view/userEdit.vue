<template>
  <section class="edit">
    <div class="wrapper edit__wrapper">
      <form class="edit__data">
        <h2 class="edit__data-title">Личные данные</h2>
        <div class="edit__data-block">
          <div ref="dropzone" class="dropzone edit__data-photo">
            <button v-if="userData.avatar" type="button" @click="deletePhotoAvatar(userData.avatar)" class="edit__data-photo__delete"></button>
            <img v-if="!userData.avatar" src="@/assets/create/cross-icon.svg" alt="иконка загрузки" class="edit__data-photo__icon">
            <img v-else :src='"/img" + userData.avatar' alt="" class="edit__data-photo__upload">
          </div>
        </div>
        <div class="edit__data-block">
          <div class="edit__data-field">
            <p class="edit__data-field__name">Фамилия:</p>
            <input
                v-model.trim="userData.lastName"
                @input="errorFields.lastname = false"
                :class="{'error': errorFields.lastname}"
                v-restrict-input-length="120"
                type="text"
                class="edit__data-input">
            <!--            <div class="edit__data-input">{{userData.lastName}}</div>-->
            <span
                class="edit__data-field__error"
                :class="{ active: errorFields.lastname }">Заполните обязательно поле</span>
          </div>
          <div class="edit__data-field">
            <p class="edit__data-field__name">Имя:</p>
            <input
                v-model.trim="userData.firstName"
                @input="errorFields.firstname = false"
                :class="{'error': errorFields.firstname}"
                v-restrict-input-length="120"
                type="text"
                class="edit__data-input">
            <span
                class="edit__data-field__error"
                :class="{ active: errorFields.firstname }">Заполните обязательно поле</span>
          </div>
          <div class="edit__data-field">
            <p class="edit__data-field__name">Отчество:</p>
            <input
                v-model.trim="userData.surname"
                @input="errorFields.surname = false"
                :class="{'error': errorFields.surname}"
                v-restrict-input-length="120"
                type="text"
                class="edit__data-input">
            <span
                class="edit__data-field__error"
                :class="{ active: errorFields.surname }">Заполните обязательно поле</span>
          </div>
        </div>
        <div class="edit__data-block">
          <div class="edit__data-field">
            <p class="edit__data-field__name">Дата рождения:</p>
            <date-pick
                v-model="userData.dateOfBirth"
                @input="errorFields.dateOfBirth = false, errorFields.isValidBirth = false"
                :class="{'error': errorFields.dateOfBirth || errorFields.isValidBirth}"
                :format="'YYYY-MM-DD'"
                class="edit__data-input--date">
            </date-pick>
            <span
                class="edit__data-field__error"
                :class="{ active: errorFields.dateOfBirth || errorFields.isValidBirth}">
              <template v-if="errorFields.dateOfBirth">Заполните обязательно поле</template>
              <template v-else>Заполните поле правильно ГГГГ-ММ-ДД</template>
            </span>
          </div>
        </div>
        <div class="edit__data-block">
          <div class="edit__data-field">
            <p class="edit__data-field__name">Гражданство:</p>
            <input v-model.trim="userData.citizenship" type="text" class="edit__data-input">
          </div>
        </div>
        <div class="edit__data-block">
          <div class="edit__data-field">
            <p class="edit__data-field__name">Регион:</p>
            <input v-model.trim="userData.region" type="text" class="edit__data-input">
          </div>
          <div class="edit__data-field">
            <p class="edit__data-field__name">
              <template v-if="userData.usertype === 'applicant'">Город проживания:</template>
              <template v-else>Адрес офиса компании:</template>
            </p>
            <input v-model.trim="userData.city" type="text" class="edit__data-input">
          </div>
        </div>
        <p class="edit__data-field__name">Контакты:</p>
        <div class="edit__data-block">

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
                v-model.trim="userData.email"
                type="text"
                placeholder="Адрес эл.почты"
                class="edit__data-input contact"
                readonly>
          </div>
          <div class="edit__data-field contact">
            <img
                src="../../assets/telegram-icon.svg"
                alt="иконка телеграмма"
                class="edit__data-img">
            <input
                v-model.trim="userData.telegram"
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
                v-model.trim="userData.website"
                type="text"
                class="edit__data-input contact" placeholder="Личный сайт">
          </div>
        </div>

        <div class="edit__data-field about">
          <form class="edit__data-portfolio">
            <div v-for="image in userDataPortfolio" :key="image" class="edit__data-portfolio__item">
              <img :src="image" alt="" class="edit__data-portfolio__image">
              <button @click="deleteImage(image)" type="button" class="edit__data-portfolio__delete"></button>
            </div>
            <div ref="dropzonePortfolio" class="dropzone edit__data-portfolio__item">
              <img class="edit__data-portfolio__button" src="@/assets/btn-add.svg" alt="кнопка добавления">
            </div>
          </form>
        </div>
        <h2 class="edit__data-title">О вас</h2>
        <div v-if="userData.usertype === 'employer'" class="edit__data-block">
          <div ref="dropzoneSmall" class="dropzone edit__data-photo edit__data-photo--organization">
            <button v-if="userData.photo_org" @click="deletePhotoOrg()" class="edit__data-photo__delete"></button>
            <img v-if="!userData.photo_org" src="@/assets/create/cross-icon.svg" alt="иконка загрузки" class="edit__data-photo__icon">
            <img v-else :src='"/img" + userData.photo_org' alt="" class="edit__data-photo__upload">
          </div>
        </div>
        <div v-if="userData.usertype === 'employer'" class="edit__data-block about">
          <div class="edit__data-field about">
            <p class="edit__data-field__name">Название организации</p>
            <input
                v-model.trim="userData.title_org"
                @input="errorFields.titleOrg = false"
                :class="{'error': errorFields.titleOrg}"
                class="edit__data-input"/>
            <span
                class="edit__data-field__error"
                :class="{ active: errorFields.titleOrg }">Заполните обязательно поле</span>
          </div>
        </div>
        <div class="edit__data-block about">
          <div class="edit__data-field about">
            <p class="edit__data-field__name">
              <template v-if="userData.usertype === 'employer'">Описание организации:</template>
              <template v-else>Описание:</template>
            </p>
            <textarea v-model.trim="userData.about" class="edit__data-input about"></textarea>
          </div>
        </div>
        <div class="edit__data-block about">
          <div class="edit__data-field about">
            <p class="edit__data-field__name">
              <template v-if="userData.usertype === 'employer'">Краткое описание ваших достижений:</template>
              <template v-else>Краткое описание ваших работ</template>
            </p>
            <textarea v-model.trim="userData.aboutWork" class="edit__data-input about"></textarea>
          </div>
        </div>
      </form>
      <aside class="edit__side">
        <span class="edit__side-title">Вы в режиме редактирования</span>
        <button @click="submitUserData" type="button" class="button-green edit__side-button">Сохранить</button>
        <button @click="closeEditProfile" type="button" class="edit__side-link">Вернуться в профиль</button>
      </aside>
    </div>
  </section>
</template>

<script>

import Vue from "vue";
import VueTheMask from "vue-the-mask";
import axios from "axios";

import DatePick from 'vue-date-pick';
import 'vue-date-pick/dist/vueDatePick.css';
import {Dropzone} from "dropzone";

Vue.use(VueTheMask);

export default {
  name: 'user-edit',
  components: {DatePick},
  data() {
    return {
      errorFields: {
        firstname: false,
        lastname: false,
        surname: false,
        dateOfBirth: false,
        isValidBirth: false,
        titleOrg: false,
      },
      userDataPortfolio: ['1212121', '121212aaa'],
      userData: {},
    }
  },
  methods: {
    closeEditProfile() {
      return this.checkValidData() ? this.$router.push(`/${this.userData.usertype}`) : this.checkValidData()
    },
    async deletePhotoAvatar(path) {
      path = `/img${path}`
      try {
        await axios.post(`/api/delete_photo/`, {file_path: path})
        await axios.post('/api/upload-avatar/',
            {
              avatar: 1,
              email: this.userData.email,
              usertype: this.userData.usertype,
            }
        )
        this.userData.avatar = ''
      } catch (error) {
        console.log({file_path: path})
        console.log(error)
      }
    },
    deletePhotoOrg() {
      this.userData.photo_org = ''
    },
    async submitUserData() {
      try {
        if (this.checkValidData()) {
          await axios.patch(`/${this.userData.usertype}/edit-data/${this.userData.id}/`, this.userData)
          location.reload()
        } else {
          this.checkValidData()
        }
      } catch (error) {
        console.log(error)
      }
    },
    validateField(value) {
      return !value;
    },
    checkValidData() {
      this.errorFields.firstname = this.validateField(this.userData.firstName)
      this.errorFields.lastname = this.validateField(this.userData.lastName)
      this.errorFields.surname = this.validateField(this.userData.surname)
      this.errorFields.dateOfBirth = this.validateField(this.userData.dateOfBirth)
      this.errorFields.titleOrg = this.validateField(this.userData.title_org) && this.userData.usertype === 'employer'
      this.errorFields.isValidBirth = this.checkValidDateOfBirth(this.userData.dateOfBirth)
      return Object.values(this.errorFields).every((error) => !error)
    },
    updateEditedUserData() {
      this.userData = {...this.$store.state.userData};

      if(this.$refs.dropzoneSmall) {
        this.dropzone = new Dropzone(this.$refs.dropzoneSmall, {
          url: "/api/employer/upload-photorg/",
          methods: "post",
          maxFiles: 1,
          maxFilesize: 2,
          thumbnailWidth: 250,
          thumbnailHeight: 250,
          addRemoveLinks: true,
          acceptedFiles: "image/jpeg,image/png,image/webp",
          paramName: "photo_org",
          sending: (file, xhr, formData) => {
            formData.append("pk", this.userData.id);
            formData.append("usertype", this.userData.usertype);
          },
        })
      }
    },
    checkValidDateOfBirth(date) {
      return !/[a-za-яё]/i.test(date) && !/^\d{4}-\d{2}-\d{2}$/.test(date)
    },
    deleteImage(image) {
      this.userDataPortfolio = this.userDataPortfolio.filter(item => item !== image)
    }
  },
  watch: {
    '$store.state.userData': {
      handler: 'updateEditedUserData',
      immediate: true,
    },
  },
  mounted() {
    this.dropzone = new Dropzone(this.$refs.dropzone, {
      url: "/api/upload-avatar/",
      method: 'post',
      maxFiles: 1,
      maxFilesize: 2,
      thumbnailWidth: 250,
      thumbnailHeight: 250,
      addRemoveLinks: true,
      acceptedFiles: "image/jpeg,image/png,image/webp",
      paramName: "avatar",
      sending: (file, xhr, formData) => {
        formData.append("email", this.userData.email);
        formData.append("usertype", this.userData.usertype);
      },
    })

    this.dropzone = new Dropzone(this.$refs.dropzonePortfolio, {
      url: "/api/applicant/upload-portfolio/",
      method: 'post',
      maxFiles: 1,
      maxFilesize: 2,
      thumbnailWidth: 373,
      thumbnailHeight: 280,
      addRemoveLinks: true,
      acceptedFiles: "image/jpeg,image/png,image/webp",
      paramName: "portfolio",
      sending: (file, xhr, formData) => {
        formData.append("pk", this.userData.id);
        formData.append("usertype", this.userData.usertype);
      },
    })
  },
}
</script>

<style src="@/style/userEdit.scss" lang="scss" scoped>

</style>

<!--</style>-->