<template>
  <section class="profile">
    <div class="profile__wrapper wrapper">
      <div class="profile__left">
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
            <p class="profile__data__name text-margin">Александра Андреева</p>
            <p class="profile__data__age text-margin">19 лет</p>
            <p class="profile__data__geo">Алтайский край, Барнаул</p>
          </div>
        </div>
        <div class="profile__line"></div>
        <div class="profile__main">
          <div class="profile__btns">
            <button @click="switchingTabs" class="profile__btn" :class="{active: applicantStab === 1}">Обо мне
            </button>
            <button @click="switchingTabs" class="profile__btn" :class="{active: applicantStab === 2}">{{ buttonText }}
            </button>
          </div>

          <template v-if="applicantStab === 1">
            <div class="profile__block">
              <user-contacts :userContact="userData.contact" class="contact-mobile">
              </user-contacts>
              <h3 class="profile__subtitle">О вас:</h3>
              <div class="profile__about-wrapper">
                <textarea
                    v-model="localUserData.about"
                    class="profile__about__text"
                    :placeholder="placeholders.about"
                ></textarea>
                <button type="button" class="profile__btn-edit field about"></button>
              </div>
            </div>
            <div class="profile__block">
              <h3 class="profile__subtitle">Примеры выполненных работ:</h3>
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
              <textarea v-model="localUserData.aboutWork" class="profile__about" :placeholder="placeholders.aboutWork"></textarea>
            </div>
          </template>
          <template v-else>
            <slot name="twoTub">
            </slot>
          </template>
        </div>
      </div>
      <user-contacts :userContact="userData.contact" class="contact-desktop"></user-contacts>
    </div>
  </section>
</template>

<script>
import UserContacts from "@/components/ui/userContacts.vue";
import axios from "axios";


export default {
  name: 'user-profile',
  components: {UserContacts},
  props: {
    buttonText: {
      type: String,
      required: true,
    },
    userData: {
      type: Object,
      required: true,
    },
    placeholders: {
      type: Object,
      required: true,
    }
  },
  data() {
    return {
      applicantStab: 1,
      localUserData: this.userData,
      placeholder: '121212',
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