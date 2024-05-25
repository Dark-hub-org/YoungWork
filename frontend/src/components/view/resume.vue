<template>
  <section class="resume">
    <div class="wrapper">
      <the-heading title="Сервис по поиску работы для подростков"/>
      <div class="resume__main">
        <div class="resume__top">
          <p class="resume__top-title">{{resumeData.resume_title}}</p>
          <p class="resume__top-summery">{{resumeData.salary}} рублей</p>
          <div class="resume__top-block">
            <p class="resume__top-text">Опыт работы: {{resumeData.experience}}</p>
            <div class="resume__top-list">
              <p v-for="item in resumeEmploy" :key="item" class="resume__top-text">{{item}}</p>
            </div>

          </div>
          <div class="resume__top-btns">
<!--            <button class="button-orange-another">Связаться</button>-->
            <button class="button-orange">В избранное</button>
          </div>
        </div>
        <div class="resume__contacts">
          <img v-if="resumeData.avatar" :src='"/img" + resumeData.avatar' alt="фото соискателя" class="resume__contacts-img">
          <img v-else src="@/assets/header/anonim-logo.svg" class="resume__contacts-img resume__contacts-img--anonymous" alt="фото соискателя">
          <p class="resume__contacts-name">{{resumeData.last_name}} {{resumeData.first_name}} {{resumeData?.surname}}</p>
          <div class="resume__contacts-block">
            <p v-if="resumeData.region || resumeData.citizenship" class="resume__contacts-text">
              {{resumeData.region}} {{resumeData.citizenship}}</p>
            <a href="tel:+89998887766" class="resume__contacts-text">{{resumeData.phone_number}}</a>
          </div>
        </div>
        <div class="resume__content">
          <div class="resume__content-block">
            <p class="resume__content-title">Обо мне:</p>
            <div class="resume__content-text" v-html="resumeData.about_us"></div>
          </div>
          <div class="resume__content-block">
            <p class="resume__content-title">Мои качества:</p>
            <div class="resume__content-list">
              <p v-for="item in resumeData.quality" :key="item" class="resume__content-item">{{item}}</p>
            </div>
          </div>
          <div class="resume__content-block">
            <p class="resume__content-title">Ключевые навыки:</p>
            <div class="resume__content-list">
              <p v-for="item in resumeData.skills" :key="item" class="resume__content-item">{{item}}</p>
            </div>
          </div>
          <div class="resume__bottom">
            <p class="resume__bottom-date">Резюме было опубликовано {{resumeData.timestamp}}</p>
<!--            Y -->
          </div>
        </div>
      </div>
    </div>
  </section>

</template>

<script>
import TheHeading from "@/components/ui/heading.vue";
import axios from "axios";
export default {
  components: {TheHeading},
  name: 'resume-page',
  data() {
    return {
      resumeData: {},
    }
  },
  methods: {
    async getResumeData(id) {
      try {
        const response = await axios.get(`/api/res/${id}`)
        this.resumeData = response.data
      } catch (error) {
        console.log(error)
      }
    },

  },
  computed: {
    resumeEmploy() {
      return this.resumeData?.employ.map((item, index, arr) => index !== arr.length - 1 ? item + ',' : item)
    }
  },
  mounted() {
    this.getResumeData(this.$route.params.id)
  }
}
</script>

<!--<style lang="scss" src="@/style/page/resume.scss" scoped>-->

<!--</style>-->