<template>
  <user-profile
      :userData="employerData"
      :profileText="profileText"
      :userAge="userAge">
    <template v-slot:modal-window>
      <modal-window
          :isVisible="isModalVisible"
          @close="onCloseModalWin">
        <div class="profile__modal-verification">
          <form class="modal-verification__form" :class="{'stepTwo': isVerificationModal}">
            <template v-if="!isVerificationModal">
              <p class="modal-verification__title">Мы заботимся о безопасности наших пользователей.</p>
              <p class="modal-verification__text">Подтверждение ИНН повысит доверие к вашей организации со стороны
                соискателей.</p>
              <p class="modal-verification__text">Введите идентификационный номер налогоплательщика (ИНН):</p>
              <div class="modal-verification__input-wrapper">
                <input
                    v-model="userINN"
                    @input="handlerInput"
                    type="text"
                    placeholder="Например, 987654321098"
                    class="modal-verification__input"
                    :class="{error: isUserINNError}">
                <img v-if="isUserINNError" src="@/assets/error-icon.svg" alt="иконка ошибка" class="modal-verification__error-icon">
                <p v-if="isUserINNError" class="modal-verification__error">Неправильно заполнено поле</p>
                <p class="modal-verification__label">12 цифр</p>
              </div>
              <button @click="submitINN" type="button" class="modal-verification__btn">Отправить на проверку</button>
            </template>
            <template v-else>
              <p class="modal-verification__title">Отправлено на проверку</p>
              <p class="modal-verification__text">Заявление будет рассмотрено в течение 24 часов.</p>
            </template>
          </form>
        </div>
      </modal-window>
    </template>
    <template v-slot:twoTub>
      <div class="profile__vacancy">
        <p class="profile__subtitle">Активные:</p>
      </div>
      <div class="profile__vacancy">
        <p class="profile__subtitle">Завершенные:</p>
      </div>
    </template>
    <template v-slot:verification>
      <div class="profile-verification">
        <template v-if="!employerData.isVerification">
          <p class="profile-verification__title">Подтвердите профиль</p>
          <p class="profile-verification__text">Так вы обеспечиваете дополнительную безопасность и доверие пользователя
            к вашей организации</p>
          <button @click="isModalVisible = true" class="profile-verification__button">Подтвердить</button>
        </template>
        <template v-else>
          <p class="profile-verification__title verification">Профиль подтвержден</p>
          <p class="profile-verification__text">Это проверенный работодатель</p>
        </template>
      </div>
    </template>
  </user-profile>
</template>

<script>
import UserProfile from "@/components/ui/userProfile.vue";
import ModalWindow from "@/components/ui/modalWin.vue";

export default {
  name: 'employer-profile',
  components: {ModalWindow, UserProfile},
  data() {
    return {
      profileText: {
        buttonText: 'Вакансии',
        placeholders: {
          about: 'Расскажите, где работали, какие у вас качества, которые могли бы заинтересовать работодателя',
          aboutWork: 'Описание выполненных работ',
        },
        portfolioTitle: 'Награды и достижения:',
      },
      employerData: {
        firstname: '',
        lastname: '',
        patronymic: '',
        birthday: '10/02/2004',
        sex: '',
        region: '',
        city: '',
        photo: '',
        about: '',
        aboutWork: '',
        isVerification: false,
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
      isVerificationModal: false,
      userINN: '',
      isUserINNError: false,
      isModalVisible: false,
    }
  },
  methods: {
    onCloseModalWin() {
      this.isModalVisible = false;
      this.userINN = '';
      this.isUserINNError = false;
      this.isVerificationModal = false
    },
    handlerInput() {
      console.log(new Date())
      if (this.userINN.length > 12) {
        this.userINN = this.userINN.slice(0, 12)
      } else {
        if(this.isUserINNError) {
          this.isUserINNError = false
        }
        this.userINN = this.userINN.replace(/[^0-9]/g, '');
      }

    },
    submitINN() {
      if(this.userINN.length !== 12) {
        this.isUserINNError = true;
      } else {
        this.isVerificationModal = true
      }
    }
  },
  computed: {
    userAge() {
      const birthYear = new Date(this.employerData.birthday).getFullYear()
      const nowYear = new Date().getFullYear()
      return nowYear - birthYear
    }
  }
}
</script>

<style src="@/style/employer.scss" lang="scss" scoped>

</style>