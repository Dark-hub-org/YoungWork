<template>
  <user-profile :userData="applicantData" :buttonText="buttonText" :placeholders="placeholders">
    <template v-slot:twoTub>
      <div class="profile__block data block__full-name">
        <div class="profile__field">
          <p class="profile__field__name">Фамилия:</p>
          <input v-model="applicantData.lastname" type="text" class="profile__input">
        </div>
        <div class="profile__field">
          <p class="profile__field__name">Имя:</p>
          <input v-model.trim="applicantData.firstname" type="text" class="profile__input">
        </div>
        <button type="button" class="profile__btn-edit field"></button>
      </div>
      <div class="profile__block">
        <div class="profile__field">
          <p class="profile__field__name">Дата рождения:</p>
          <input v-model="applicantData.birthday" type="text" class="profile__input" v-mask="'##/##/####'">
        </div>
      </div>
      <div class="profile__block">
        <div class="profile__field">
          <p class="profile__field__name">Пол:</p>
          <div class="profile__radio-wrapper">
            <input v-model="applicantData.sex" type="radio" name="exp" value="men" class="profile__radio"
                   id="men"
                   checked>
            <label for="men" class="profile-filter-label">Мужской</label>
          </div>
          <div class="profile__radio-wrapper">
            <input v-model="applicantData.sex" type="radio" name="exp" value="women" class="profile__radio"
                   id="women">
            <label for="women" class="profile-filter-label">Женщина</label>
          </div>
        </div>
      </div>
      <div class="profile__block data start">
        <div class="profile__field">
          <p class="profile__field__name">Регион:</p>
          <input v-model="applicantData.region" type="text" class="profile__input">
        </div>
        <div class="profile__field">
          <p class="profile__field__name">Город проживания:</p>
          <input v-model="applicantData.city" type="text" class="profile__input">
        </div>
        <button type="button" class="profile__btn-edit field"></button>
      </div>
      <div class="profile__block data">
        <div class="profile__field contact">
          <p class="profile__field__name">Контакты:</p>
          <img
              src="@/assets/phone-icon.svg"
              alt="иконка телефона"
              class="profile__connection__img">
          <input
              v-mask="'+7 (###) ### ##-##'"
              placeholder="Номер телефона"
              class="profile__input connect"
              v-model="applicantData.contact.telephone"/>
        </div>
        <div class="profile__field contact">
          <img
              src="@/assets/email-icon.svg"
              alt="иконка e-mail"
              class="profile__connection__img">
          <input type="text" class="profile__input connect" placeholder="Адрес эл.почты"
                 v-model.trim="applicantData.contact.email">
        </div>
        <div class="profile__field contact">
          <img
              src="@/assets/telegram-icon.svg"
              alt="иконка телеграмма"
              class="profile__connection__img">
          <input type="text" class="profile__input connect" placeholder="Telegram"
                 v-model="applicantData.contact.telegram">
        </div>
        <div class="profile__field contact">
          <img
              src="@/assets/link-icon.svg"
              alt="иконка ссылки"
              class="profile__connection__img">
          <input type="text" class="profile__input connect" placeholder="Личный сайт"
                 v-model.trim="applicantData.contact.website">
        </div>
        <button type="button" class="profile__btn-edit field "></button>
      </div>
    </template>
  </user-profile>
</template>

<script>
import Vue from "vue";
import VueTheMask from 'vue-the-mask';
import UserProfile from "@/components/ui/userProfile.vue";

Vue.use(VueTheMask);

export default {
  name: 'applicant-profile',
  components: {UserProfile},
  data() {
    return {
      buttonText: 'Личные данные',
      placeholders: {
        about: 'Расскажите, где работали, какие у вас качества, которые могли бы заинтересовать работодателя',
        aboutWork: 'Описание выполненных работ',
      },
      applicantData: {
        firstname: '',
        lastname: '',
        birthday: '',
        sex: '',
        region: '',
        city: '',
        photo: '',
        patronymic: '',
        about: '',
        aboutWork: '',
        portfolio: [
          {id: 1, image: '../../assets/applicant-profile/image-1.png'},
          {id: 2, image: '../../assets/applicant-profile/image-2.png'},
          {id: 3, image: '../../assets/applicant-profile/image-3.png'},
        ],
        contact: {
          telegram: 'as8691_1',
          email: 'sasha-andreeva-1998@list.ru',
          telephone: '+7 999 888 77 66',
          website: 'https://dprofile.ru/andreeva_design',
        }
      },
    }
  }
}
</script>

<style src="@/style/applicant.scss" lang="scss" scoped>

</style>