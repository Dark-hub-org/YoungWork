<template>
  <section class="applicant-profile">
    <div class="applicant-profile__wrapper wrapper">
      <div class="applicant-profile__left">
        <div class="applicant-profile__top">
          <div class="applicant-profile__photo-wrapper">
            <div
                class="applicant-profile__photo" style="background: #DFDFDF">
            </div>
            <div class="applicant-profile__btn-edit-wrapper">
              <input type="file" class="applicant-profile__photo__btn">
            </div>
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
            <button @click="switchingTabs" class="applicant-profile__btn" :class="{active: applicantStab === 1}">Обо
              мне
            </button>
            <button @click="switchingTabs" class="applicant-profile__btn" :class="{active: applicantStab === 2}">Личные
              данные
            </button>
          </div>
          <template v-if="applicantStab === 1">
            <div class="applicant-profile__block">
              <user-contacts :userContact="userContact"  class="contact-mobile">

              </user-contacts>
              <h3 class="applicant-profile__subtitle">О вас:</h3>
              <div class="applicant-profile__about-wrapper">
                <textarea
                    class="applicant-profile__about__text"
                    placeholder="Расскажите, где работали, какие у вас качества, которые могли бы заинтересовать работодателя "
                ></textarea>
                <button type="button" class="applicant-profile__btn-edit field about"></button>
              </div>
            </div>
            <div class="applicant-profile__block">
              <h3 class="applicant-profile__subtitle">Примеры выполненных работ:</h3>
              <div class="applicant-profile__portfolio">
                <div class="applicant-profile__portfolio__block portfolio__block--add">
                  <button class="applicant-profile__btn-edit btn--work btn--add"></button>
                </div>
                <div
                    v-for="item of applicantPortfolio"
                    :key="item.id"
                    class="applicant-profile__portfolio__block">
                  <button class="applicant-profile__btn-edit btn--work btn--"></button>
                </div>
              </div>
              <textarea class="applicant-profile__about" placeholder="Описание выполненных работ"></textarea>
            </div>
          </template>
          <template v-else>
            <div class="applicant-profile__block data block__full-name">
              <div class="applicant-profile__field">
                <p class="applicant-profile__field__name">Фамилия:</p>
                <input v-model="applicantLastName" type="text" class="applicant-profile__input">
              </div>
              <div class="applicant-profile__field">
                <p class="applicant-profile__field__name">Имя:</p>
                <input v-model.trim="applicantFirstName" type="text" class="applicant-profile__input">
              </div>
              <!--              <div class="applicant-profile__field">-->
              <!--                <p class="applicant-profile__field__name">Отчество:</p>-->
              <!--                <input v-model="applicantPatronymic" type="text" class="applicant-profile__input">-->
              <!--              </div>-->
              <button type="button" class="applicant-profile__btn-edit field"></button>
            </div>
            <div class="applicant-profile__block">
              <div class="applicant-profile__field">
                <p class="applicant-profile__field__name">Дата рождения:</p>
                <input v-model="applicantBirthday" type="text" class="applicant-profile__input" v-mask="'##/##/####'">
              </div>
            </div>
            <div class="applicant-profile__block">
              <div class="applicant-profile__field">
                <p class="applicant-profile__field__name">Пол:</p>
                <div class="applicant-profile__radio-wrapper">
                  <input v-model="applicationSex" type="radio" name="exp" value="men" class="applicant-profile__radio"
                         id="men"
                         checked>
                  <label for="men" class="applicant-profile-filter-label">Мужской</label>
                </div>
                <div class="applicant-profile__radio-wrapper">
                  <input v-model="applicationSex" type="radio" name="exp" value="women" class="applicant-profile__radio"
                         id="women">
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
              <button type="button" class="applicant-profile__btn-edit field"></button>
            </div>
            <div class="applicant-profile__block data">
              <div class="applicant-profile__field contact">
                <p class="applicant-profile__field__name">Контакты:</p>
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
                <input type="text" class="applicant-profile__input connect" placeholder="Адрес эл.почты"
                       v-model.trim="applicantEmail">
              </div>
              <div class="applicant-profile__field contact">
                <img
                    src="@/assets/telegram-icon.svg"
                    alt="иконка телеграмма"
                    class="applicant-profile__connection__img">
                <input type="text" class="applicant-profile__input connect" placeholder="Telegram"
                       v-model="applicantTelegram">
              </div>
              <div class="applicant-profile__field contact">
                <img
                    src="@/assets/link-icon.svg"
                    alt="иконка ссылки"
                    class="applicant-profile__connection__img">
                <input type="text" class="applicant-profile__input connect" placeholder="Личный сайт"
                       v-model.trim="applicantWebsite">
              </div>
              <button type="button" class="applicant-profile__btn-edit field "></button>
            </div>
          </template>
        </div>
      </div>
      <user-contacts :userContact="userContact" class="contact-desktop"></user-contacts>
    </div>
  </section>
</template>

<script>
import axios from "axios";
import Vue from "vue";
import VueTheMask from 'vue-the-mask';
import UserContacts from "@/components/ui/userContacts.vue";

Vue.use(VueTheMask);

export default {
  name: 'applicant-profile',
  components: {UserContacts},
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
      applicantPortfolio: [
        {id: 1, image: '../../assets/applicant-profile/image-1.png'},
        {id: 2, image: '../../assets/applicant-profile/image-2.png'},
        {id: 3, image: '../../assets/applicant-profile/image-3.png'}
      ],
      userContact: {
        telegram: 'as8691_1',
        email: 'sasha-andreeva-1998@list.ru',
        telephone: '+7 999 888 77 66',
        website: 'https://dprofile.ru/andreeva_design',
      }
    }
  },
  methods: {
    switchingTabs() {
      if (this.applicantStab === 1) {
        this.applicantStab = 2;
        localStorage.setItem('applicantTab', JSON.stringify(2));
      } else {
        this.applicantStab = 1;
        localStorage.setItem('applicantTab', JSON.stringify(1));
      }
    },
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
  },
  mounted() {
    for (let key in localStorage) {
      if (key === 'applicantTab') {
        this.applicantStab = JSON.parse(localStorage.getItem('applicantTab'))
      }
    }
  },
  beforeDestroy() {
    for (let key in localStorage) {
      if (key === 'applicantTab') {
        localStorage.removeItem('applicantTab')
      }
    }
  }
}
</script>

<style src="@/style/applicant.scss" lang="scss" scoped>

</style>