<template>
  <user-profile :userData="employerData" :buttonText="buttonText" :placeholders="placeholders">
    <template v-slot:twoTub>
        <div class="profile__vacancy">
          <p class="profile__subtitle">Активные:</p>
        </div>
      <div class="profile__vacancy">
        <p class="profile__subtitle">Завершенные:</p>
      </div>
    </template>
  </user-profile>
</template>

<script>
import UserProfile from "@/components/ui/userProfile.vue";

export default {
  name: 'employer-profile',
  components: {UserProfile},
  data() {
    return {
      buttonText: 'Вакансии',
      placeholders: {
        about: 'Расскажите, где работали, какие у вас качества, которые могли бы заинтересовать работодателя',
        aboutWork: 'Описание выполненных работ',
      },
      employerData: {
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

<style lang="scss" scoped>

</style>