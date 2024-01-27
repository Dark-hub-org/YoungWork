<template>
  <section class="profile">
    <div class="profile__wrapper wrapper">
      <div class="profile__left">
        <template v-if="!this.$store.state.isProfileEdit">
          <div class="profile__top">
            <div class="profile__top-photo-wrapper">
              <div
                  class="profile__top-photo" style="background: #DFDFDF">
              </div>
              <div class="profile__top-photo__edit">
                <input type="file" class=" profile__top-photo__input">
              </div>
            </div>
            <div class="profile__data">
              <p class="profile__data-name text-margin">{{userData.first_name}} {{userData.last_name}} {{userData.surname}}</p>
              <p class="profile__data-age text-margin">{{userAge}} лет</p>
              <p class="profile__data-geo text-margin">Гражданство:
                <template v-if="userData.citizenship">{{userData.citizenship}}</template><template v-else>Не заполнено</template></p>
              <p class="profile__data-geo">
                <template v-if="userData.region">{{userData.region}}</template>
                <template v-else>Регион не заполнен</template>,
                <template v-if="userData.city">{{userData.city}}</template>
                <template v-else>город не заполнен</template>
              </p>
              <button @click="openEditProfile" class="profile__data-edit">Редактировать профиль</button>
            </div>
          </div>
          <div class="profile__line"></div>
          <div class="profile__main">
            <slot name="modal-window"></slot>
            <div class="profile__main-btns">
              <button
                  @click="switchingTabs(1)"
                  :class="{active: applicantStab === 1}"
                  class="profile__main-btn"
                  ref="tabOne"
                  >Обо мне</button>
              <button
                  @click="switchingTabs(2)"
                  :class="{active: applicantStab === 2}"
                  class="profile__main-btn"
                  ref="tabTwo"
                  >
                {{ profileText.buttonText }}</button>
            </div>
            <template v-if="applicantStab === 1">
              <div class="profile__main-block">
                <div class="profile__contact-mobile">
                  <user-contacts :userContact="userData.contact" class="contact-mobile">
                  </user-contacts>
                  <slot name="verification"></slot>
                </div>
                <h3 class="profile__subtitle">О вас:</h3>
                <div class="profile__main-block__about">
                <textarea
                    v-model="localUserData.about"
                    class="profile__main-block__about-text"
                    :placeholder="profileText.placeholders.about"
                ></textarea>
                </div>
              </div>
              <div class="profile__main-block">
                <h3 class="profile__subtitle">{{profileText.portfolioTitle}}</h3>
                <div class="profile__portfolio">
                  <div class="profile__portfolio-block profile__portfolio-block--add">
                    <button class="profile__btn-edit btn--work btn--add"></button>
                  </div>
                  <div
                      v-for="item of localUserData.portfolio"
                      :key="item.id"
                      class="profile__portfolio-block">
                    <button class="profile__btn-edit btn--work btn--"></button>
                  </div>
                </div>
                <textarea v-model="localUserData.aboutWork" class="profile__portfolio-about" :placeholder="profileText.placeholders.aboutWork"></textarea>
              </div>
            </template>
            <template v-else>
              <slot name="twoTub">
              </slot>
            </template>
          </div>
        </template>
        <template v-else>
          <user-edit :userData="userData">
          </user-edit>
        </template>
      </div>
      <aside class="profile__side">
        <template v-if="!this.$store.state.isProfileEdit">
          <user-contacts :userContact="userData.contact" class="contact-desktop"></user-contacts>
          <slot name="verification"></slot>
        </template>
        <template v-else>
          <div class="profile__changes">
            <p class="profile__changes-title">Вы в режиме редактирования</p>
            <button class="profile__changes-save">Сохранить </button>
            <button @click="closeEditProfile" class="profile__changes-cancel">Отменить изменения</button>
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
    }
  },
  methods: {
    switchingTabs(tab) {
      this.applicantStab = tab
      localStorage.setItem('applicantTab', JSON.stringify(tab));
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
    openEditProfile() {
      this.$store.commit('editISProfileEdit', true)
    },
    closeEditProfile() {
      this.$store.commit('editISProfileEdit', false)
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

<style src="@/style/ui/userProfile.scss" lang="scss" scoped>

</style>