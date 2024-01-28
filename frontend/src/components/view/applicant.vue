<template>
  <user-profile :userData="userData" :profileText="profileText" :userAge="userAge">
    <template v-slot:twoTub>
      <div class="profile__main-block data block__full-name">
        <div class="profile__field">
          <p class="profile__field-name">Фамилия:</p>
          <div class="profile__value">
            <p class="profile__value-text">{{userData.lastName}}</p>
          </div>
        </div>
        <div class="profile__field">
          <p class="profile__field-name">Имя:</p>
          <div class="profile__value">
            <p class="profile__value-text">{{userData.firstName}}</p>
          </div>
        </div>
        <div class="profile__field">
          <p class="profile__field-name">Отчество:</p>
          <div class="profile__value">
            <p class="profile__value-text">{{userData.surname}}</p>
          </div>
        </div>
      </div>
      <div class="profile__main-block">
        <div class="profile__field">
          <p class="profile__field-name">Дата рождения:</p>
          <div class="profile__value">
            <p class="profile__value-text">{{userData.dateOfBirth}}</p>
          </div>
        </div>
      </div>
      <div class="profile__main-block">
        <div class="profile__field">
          <p class="profile__field-name">Пол:</p>
          <div class="profile__value">
            <p class="profile__value-text">
              <template v-if="userData.gender === 'men'">
                Мужской
              </template>
              <template v-else-if="userData.gender === 'women'">
                Женский
              </template>
              <template v-else>
                Не заданно
              </template>
            </p>
          </div>
        </div>
      </div>
<!--      <div class="profile__main-block">-->
<!--        <div class="profile__field">-->
<!--          <p class="profile__field-name">Пол:</p>-->
<!--          <div class="profile__radio-wrapper">-->
<!--            <input v-model="applicantData.sex" type="radio" name="exp" value="men" class="profile__radio"-->
<!--                   id="men"-->
<!--                   checked>-->
<!--            <label for="men" class="profile-filter-label">Мужской</label>-->
<!--          </div>-->
<!--          <div class="profile__radio-wrapper">-->
<!--            <input v-model="applicantData.sex" type="radio" name="exp" value="women" class="profile__radio"-->
<!--                   id="women">-->
<!--            <label for="women" class="profile-filter-label">Женщина</label>-->
<!--          </div>-->
<!--        </div>-->
<!--      </div>-->
      <div class="profile__main-block data start">
        <div class="profile__field">
          <p class="profile__field-name">Гражданство:</p>
          <div class="profile__value">
            <p class="profile__value-text">{{userData.citizenship}}</p>
          </div>
        </div>
      </div>
      <div class="profile__main-block data start">
        <div class="profile__field">
          <p class="profile__field-name">Регион:</p>
          <div class="profile__value">
            <p class="profile__value-text">{{userData.region}}</p>
          </div>
        </div>
        <div class="profile__field">
          <p class="profile__field-name">Город проживания:</p>
          <div class="profile__value">
            <p class="profile__value-text">{{userData.city}}</p>
          </div>
        </div>
      </div>
    </template>
  </user-profile>
</template>

<script>
// import Vue from "vue";
// import VueTheMask from 'vue-the-mask';
import UserProfile from "@/components/ui/userProfile.vue";

// Vue.use(VueTheMask);

export default {
  name: 'applicant-profile',
  components: {UserProfile},
  data() {
    return {
      profileText: {
        buttonText: 'Личные данные',
        placeholders: {
          about: 'Расскажите, где работали, какие у вас качества, которые могли бы заинтересовать работодателя',
          aboutWork: 'Описание выполненных работ',
        },
        portfolioTitle: 'Примеры выполненных работ:',
      },
      applicantData: {
        firstname: 'Максим',
        lastname: 'Кирюшин',
        patronymic: 'Евгеньвич',
        birthday: '10/04/2004',
        sex: '',
        citizenship: '',
        region: '',
        city: '',
        photo: '',
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
  },
  methods: {

  },
  computed: {
    userAge() {
      const birthYear = new Date(this.userData.date_of_birth).getFullYear()
      console.log(birthYear)
      const nowYear = new Date().getFullYear()
      return nowYear - birthYear
    },
    userData() {
      return this.$store.state.userData
    },
  },
}
</script>

<style src="@/style/applicant.scss" lang="scss" scoped>

</style>