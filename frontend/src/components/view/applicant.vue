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
    }
  },
  methods: {

  },
  computed: {
    userAge() {
      const now = new Date();
      const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
      const userBirth = new Date(this.userData.dateOfBirth);
      const dateBirth = new Date(today.getFullYear(), userBirth.getMonth(), userBirth.getDate());
      const age = today.getFullYear() - userBirth.getFullYear();

      return today < dateBirth ? age - 1 : age
    },
    userData() {
      return this.$store.state.userData
    },
  },
}
</script>

<style src="@/style/applicant.scss" lang="scss" scoped>

</style>