<template>
  <section class="profile">
    <div class="profile__wrapper wrapper">
      <div class="profile__left">
        <template v-if="!isProfileEdit">
          <div class="profile__top">
            <div class="profile__photo-wrapper">
              <div
                  class="profile__photo" style="background: #DFDFDF">
              </div>
              <div class="profile__btn-edit-wrapper">
                <input type="file" class="profile__photo__btn">
              </div>
            </div>
            <div class="profile__data">
              <p class="profile__data__name text-margin">{{userData.firstname}} {{userData.lastname}} {{userData.patronymic}}</p>
              <p class="profile__data__age text-margin">{{userAge}} лет</p>
              <p class="profile__data__geo text-margin">Гражданство:
                <template v-if="userData.citizenship">{{userData.citizenship}}</template><template v-else>Не заполнено</template></p>
              <p class="profile__data__geo">
                <template v-if="userData.region">{{userData.region}}</template>
                <template v-else>Регион не заполнен</template>,
                <template v-if="userData.city">{{userData.city}}</template>
                <template v-else>город не заполнен</template>
              </p>
              <button @click="isProfileEdit = true" class="profile__data-edit">Редактировать профиль</button>
            </div>
          </div>
          <div class="profile__line"></div>
          <div class="profile__main">
            <slot name="modal-window"></slot>
            <div class="profile__btns">
              <button @click="switchingTabs" class="profile__btn" :class="{active: applicantStab === 1}">Обо мне</button>
              <button @click="switchingTabs" class="profile__btn" :class="{active: applicantStab === 2}">{{ profileText.buttonText }}</button>
            </div>
            <template v-if="applicantStab === 1">
              <div class="profile__block">
                <div class="profile__contact-mobile">
                  <user-contacts :userContact="userData.contact" class="contact-mobile">
                  </user-contacts>
                  <slot name="verification"></slot>
                </div>
                <h3 class="profile__subtitle">О вас:</h3>
                <div class="profile__about-wrapper">
                <textarea
                    v-model="localUserData.about"
                    class="profile__about__text"
                    :placeholder="profileText.placeholders.about"
                ></textarea>
                </div>
              </div>
              <div class="profile__block">
                <h3 class="profile__subtitle">{{profileText.portfolioTitle}}</h3>
                <div class="profile__portfolio">
                  <div class="profile__portfolio__block portfolio__block--add">
                    <button class="profile__btn-edit btn--work btn--add"></button>
                  </div>
                  <div
                      v-for="item of localUserData.portfolio"
                      :key="item.id"
                      class="profile__portfolio__block">
                    <button class="profile__btn-edit btn--work btn--"></button>
                  </div>
                </div>
                <textarea v-model="localUserData.aboutWork" class="profile__about" :placeholder="profileText.placeholders.aboutWork"></textarea>
              </div>
            </template>
            <template v-else>
              <slot name="twoTub">
              </slot>
            </template>
          </div>
        </template>
        <template v-else>
          <user-edit>

          </user-edit>
        </template>
      </div>
      <aside class="profile-side">
        <template v-if="!isProfileEdit">
          <user-contacts :userContact="userData.contact" class="contact-desktop"></user-contacts>
          <slot name="verification"></slot>
        </template>
        <template v-else>
          <div class="profile-changes">
            <p class="profile-changes__title">Вы в режиме редактирования</p>
            <button class="profile-changes__save">Сохранить </button>
            <button class="profile-changes__cancel">Отменить изменения</button>
          </div>
        </template>
      </aside>
    </div>
  </section>
</template>

<script>
import UserContacts from "@/components/ui/userContacts.vue";
import axios from "axios";
import UserEdit from "@/components/ui/userEdit.vue";

export default {
  name: 'user-profile',
  components: {UserEdit, UserContacts},
  props: {
    profileText: {
      type: Object,
      required: true,
    },
    userData: {
      type: Object,
      required: true,
    },
    userAge: {
      type: Number,
      required: true,
    }
  },
  data() {
    return {
      applicantStab: 1,
      localUserData: this.userData,
      isProfileEdit: false,
    }
  },
  methods: {

    switchingTabs() {
      if (this.applicantStab === 1) {
        this.applicantStab = 2;
        localStorage.setItem('applicantTab', JSON.stringify(2));
        console.log('1')
      } else {
        this.applicantStab = 1;
        localStorage.setItem('applicantTab', JSON.stringify(1));
        console.log('2')
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
    },
    onCloseModalWin() {
      this.modalVisible = false
    },
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

<style src="@/style/ui/userProfile.scss" lang="scss" scoped>

</style>