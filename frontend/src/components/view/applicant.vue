<template>
  <section class="applicant-profile">
    <div class="applicant-profile__wrapper">
      <div class="applicant-profile__left">
        <div class="applicant-profile__top">
          <div class="applicant-profile__photo-wrapper">
            <img
                src="@/assets/applicant-profile/applicant-photo.png"
                alt="фото соискателя"
                class="applicant-profile__photo">
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
            <button class="applicant-profile__btn">Обо мне</button>
            <button class="applicant-profile__btn another">Личные данные</button>
          </div>
          <div class="applicant-profile__block">
            <h3 class="applicant-profile__subtitle">О вас:</h3>
            <textarea
                class="applicant-profile__about__text"
                placeholder="Расскажите, где работали, какие у вас качества, которые могли бы заинтересовать работодателя "
            ></textarea>
          </div>
          <div class="applicant-profile__block">

          </div>
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

export default {
name: 'applicant-profile',
  data() {
    return {
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
      name: '1212'
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