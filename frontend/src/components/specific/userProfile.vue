<template>
  <section class="profile">
    <div class="wrapper profile__wrapper">
      <div class="profile__left">
        <template v-if="!this.$store.state.isProfileEdit">
          <div class="profile__top">
            <div ref="dropzone" class="profile__top-photo-wrapper">
              <img v-if="userData.avatar" :src='"/img/" + userData.avatar' alt="" class="profile__top-photo">
            </div>
            <div class="profile__data">
              <p class="profile__data-name text-margin">{{ userData.firstName }} {{ userData.lastName }}
                {{ userData.surname }}</p>
              <p class="profile__data-age text-margin">{{ userAge }} лет</p>
              <p class="profile__data-geo text-margin">Гражданство:
                <template v-if="userData.citizenship">{{ userData.citizenship }}</template>
                <template v-else>Не заполнено</template>
              </p>
              <p class="profile__data-geo">
                <template v-if="userData.region">{{ userData.region }}</template>
                <template v-else>Регион не заполнен</template>
                ,
                <template v-if="userData.city">{{ userData.city }}</template>
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
              >Обо мне
              </button>
              <button
                  @click="switchingTabs(2)"
                  :class="{active: applicantStab === 2}"
                  class="profile__main-btn"
                  ref="tabTwo"
              >
                {{ profileText.buttonText }}
              </button>
            </div>
            <template v-if="applicantStab === 1">
              <div class="profile__main-block">
                <div class="profile__contact-mobile">
                  <user-contacts :userContact="this.userContacts" class="contact-mobile">
                  </user-contacts>
                  <slot name="verification"></slot>
                </div>
                <h3 class="profile__subtitle">О вас:</h3>
                <div class="profile__main-block__about">
                  <div
                      class="profile__main-block__about-text"
                      v-html="userData.about"
                  ></div>
                </div>
              </div>
              <div class="profile__main-block">
                <h3 class="profile__subtitle">{{ profileText.portfolioTitle }}</h3>
                <ul class="profile__portfolio">
                  <template v-if="userData.usertype === 'employer'">
                    <li
                        v-for="image in userData.achievements"
                        :key="image.id"
                        class="profile__portfolio-block">
                      <img
                          :src='"/img" + image.employer_image'
                          class="profile__portfolio-img">
                    </li>
                  </template>
                  <template v-if="userData.usertype === 'applicant'">
                    <li
                        v-for="image in userData.portfolio"
                        :key="image.id"
                        class="profile__portfolio-block">
                      <img
                          :src='"/img" + image.applicant_image'
                          class="profile__portfolio-img">
                    </li>
                  </template>
                </ul>
                <div class="profile__portfolio-about" v-html="userData.aboutWork"></div>
              </div>
            </template>
            <template v-else>
              <slot name="twoTub">
              </slot>
            </template>
          </div>
        </template>
      </div>
      <aside class="profile__side">
        <user-contacts :user-contact="this.userContacts" class="contact-desktop"></user-contacts>
        <slot name="verification"></slot>
      </aside>
    </div>
  </section>
</template>

<script>
import UserContacts from "@/components/specific/userContacts.vue";
import axios from "axios";

export default {
  name: 'user-profile',
  components: {UserContacts},
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
      dropzone: null,
    };
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
    openEditProfile() {
      this.$router.push(`/${this.userData.usertype}/edit/`)
    },
  },
  computed: {
    userContacts() {
      return {
        avatar: this.$store.state.userData.telegram,
        telegram: this.$store.state.userData.telegram,
        email: this.$store.state.userData.email,
        phoneNumber: this.$store.state.userData.phoneNumber,
        website: this.$store.state.userData.website,
      }
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
