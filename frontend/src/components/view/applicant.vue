<template>
  <user-profile :userData="userData" :profileText="profileText" :userAge="userAge">
    <template v-slot:twoTub>
      <div class="profile__vacancy">
        <p class="profile__subtitle">Активные:</p>
        <swiper
            :slides-per-view="2"
            :space-between="16"
            :loop="false"
            :navigation="true"
            class="profile__slider">
          <swiper-slide
              v-for="resume in activeResume"
              :key="resume.id"
              class="profile__slider-item">
            <p class="profile__slider-title">{{resume.resume_title}}</p>
            <div class="profile__slider-btns">
              <router-link :to="{name: 'edit-resume', params: {id: resume.id}}" tag="a" class="profile__slider-link button-orange-another">Редактировать</router-link>
              <button @click="changeStatusResume(resume, 'active')" type="button" class="button-orange">В архив</button>
            </div>
          </swiper-slide>
        </swiper>
      </div>
      <div class="profile__vacancy">
        <p class="profile__subtitle">Завершенные:</p>
        <swiper
            :slides-per-view="2"
            :space-between="16"
            :loop="false"
            :navigation="true"
            class="profile__slider">
          <swiper-slide
              v-for="resume in inactiveResume"
              :key="resume.id"
              class="profile__slider-item profile__slider-item--inactive">
            <p class="profile__slider-title">{{resume.resume_title}}</p>
            <div class="profile__slider-btns">
              <router-link :to="{name: 'edit-resume', params: {id: resume.id}}" tag="a" class="profile__slider-link button-orange-another">Редактировать</router-link>
              <button @click="changeStatusResume(resume, 'inactive')" type="button" class="button-orange">В актив</button>
            </div>
          </swiper-slide>
        </swiper>
      </div>
    </template>
  </user-profile>
</template>

<script>
import UserProfile from "@/components/ui/userProfile.vue";

import { Navigation} from 'swiper'
import { SwiperCore, Swiper, SwiperSlide } from 'swiper-vue2'
import axios from "axios";
SwiperCore.use([Navigation])

export default {
  name: 'applicant-profile',
  components: {UserProfile, Swiper, SwiperSlide},
  data() {
    return {
      profileText: {
        buttonText: 'Резюме',
        placeholders: {
          about: 'Расскажите, где работали, какие у вас качества, которые могли бы заинтересовать работодателя',
          aboutWork: 'Описание выполненных работ',
        },
        portfolioTitle: 'Примеры выполненных работ:',
      },
      activeResume: [],
      inactiveResume: [],
    }
  },
  methods: {
    async getResumeUser() {
      try {
        const activeResume = await axios.get('/api/active/res/')
        const inactiveResume = await axios.get('/api/inactive/res/')
        this.activeResume = activeResume.data
        this.inactiveResume = inactiveResume.data
      } catch(error) {
        console.log(error)
      }
    },
    async changeStatusResume(resume, status) {
      try {
        if(status === 'active') {
          await axios.post('/api/inactive/res/', {pk: resume.id})
          this.activeResume = this.activeResume.filter(item => item.id !== resume.id)
          this.inactiveResume.push(resume)
        } else {
          await axios.post('/api/active/res/', {pk: resume.id})
          this.inactiveResume = this.inactiveResume.filter(item => item.id !== resume.id)
          this.activeResume.push(resume)
        }
      } catch(error) {
        console.log(error)
      }
    },
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
  mounted() {
    this.getResumeUser()
  }
}
</script>

<style src="@/style/applicant.scss" lang="scss" scoped>

</style>