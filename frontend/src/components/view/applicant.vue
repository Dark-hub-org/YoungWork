<template>
  <div>
    <form action="">
      <div class="block-wrapper">
        <span>Фото</span>
        <input type="file">
      </div>
      <div class="block-wrapper">
        <span>Имя</span>
        <input v-model="applicantFirstName" type="text" class="input">
      </div>
      <div class="block-wrapper">
        <span>Фамилия</span>
        <input v-model="applicantLastName" type="text" class="input">
      </div>
      <div class="block-wrapper">
        <span>Отчество</span>
        <input v-model="applicantPatronymic" type="text" class="input">
      </div>
      <div class="block-wrapper">
        <span>Дата рождения</span>
        <input v-model="applicantBirthday" type="date" class="input">
      </div>
      <div class="block-wrapper">
        <span>Регион</span>
        <input v-model="applicantRegion" type="text" class="input">
      </div>
      <div class="block-wrapper">
        <span>город</span>
        <input v-model="applicantCity" type="text" class="input">
      </div>
      <div class="block-wrapper">
        <span>номер телефона</span>
        <input v-model="applicantPhoneNumber" type="text" class="input">
      </div>
      <div class="block-wrapper">
        <span>Телеграм</span>
        <input v-model="applicantTelegram" type="text" class="input">
      </div>
      <div class="block-wrapper">
        <span>Сайт</span>
        <input v-model="applicantWebsite" type="text" class="input">
      </div>
      <div class="block-wrapper">
        <span>Email</span>
        <input v-model="applicantEmail" type="text" class="input">
      </div>
      <button type="submit" @click="submitForm" style="font-size: 30px">Отправить</button>
    </form>
  </div>
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