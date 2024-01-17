<template>
  <user-profile :userData="applicantData" :profileText="profileText" :userAge="userAge">
    <template v-slot:twoTub>
      <div class="profile__main-block data block__full-name">
        <div class="profile__field">
          <p class="profile__field-name">Фамилия:</p>
          <div class="profile__value">
            <p class="profile__value-text">{{applicantData.lastname}}</p>
          </div>
        </div>
        <div class="profile__field">
          <p class="profile__field-name">Имя:</p>
          <div class="profile__value">
            <p class="profile__value-text">{{applicantData.firstname}}</p>
          </div>
        </div>
        <div class="profile__field">
          <p class="profile__field-name">Отчество:</p>
          <div class="profile__value">
            <p class="profile__value-text">{{applicantData.patronymic}}</p>
          </div>
        </div>
      </div>
      <div class="profile__main-block">
        <div class="profile__field">
          <p class="profile__field-name">Дата рождения:</p>
          <div class="profile__value">
            <p class="profile__value-text" v-mask="'##/##/####'">{{applicantData.birthday}}</p>
          </div>
        </div>
      </div>
      <div class="profile__main-block">
        <div class="profile__field">
          <p class="profile__field-name">Пол:</p>
          <div class="profile__value">
            <p class="profile__value-text">
              <template v-if="applicantData.sex === 'men'">
                Мужской
              </template>
              <template v-else-if="applicantData.sex === 'women'">
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
            <p class="profile__value-text">{{applicantData.citizenship}}</p>
          </div>
        </div>
      </div>
      <div class="profile__main-block data start">
        <div class="profile__field">
          <p class="profile__field-name">Регион:</p>
          <div class="profile__value">
            <p class="profile__value-text">{{applicantData.region}}</p>
          </div>
        </div>
        <div class="profile__field">
          <p class="profile__field-name">Город проживания:</p>
          <div class="profile__value">
            <p class="profile__value-text">{{applicantData.city}}</p>
          </div>
        </div>
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
  computed: {
    userAge() {
      const birthYear = new Date(this.applicantData.birthday).getFullYear()
      const nowYear = new Date().getFullYear()
      return nowYear - birthYear
    }
  }
}
</script>

<style src="@/style/applicant.scss" lang="scss" scoped>

</style>