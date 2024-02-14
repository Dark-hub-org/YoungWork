<template>
  <section class="resume">
    <div class="wrapper">
      <the-heading title="Сервис по поиску работы для подростков"/>
      <div class="resume__main">
        <div class="resume__top">
          <p class="resume__top-title">{{resumeData?.resume_title}}</p>
          <p class="resume__top-summery">{{resumeData?.salary}}</p>
          <div class="resume__top-block">
            <p class="resume__top-text">Опыт работы: {{resumeData?.experience}}</p>
            <div class="resume__top-list">
              <p v-for="item in resumeData?.employ" :key="item" class="resume__top-text">{{item}}, </p>
            </div>

          </div>
          <div class="resume__top-btns">
            <button class="button-orange-another">Связаться</button>
            <button class="button-orange">В избранное</button>
          </div>
        </div>
        <div class="resume__contacts">
          <div class="resume__contacts-img"></div>
          <p class="resume__contacts-name">Андреева Александра Сергеевна</p>
          <div class="resume__contacts-block">
            <p class="resume__contacts-text">Алтайский край, Барнаул</p>
            <a href="tel:+89998887766" class="resume__contacts-text">8(999)888-77-66</a>
          </div>
        </div>
        <div class="resume__content">
          <div class="resume__content-block">
            <p class="resume__content-title">Обо мне:</p>
            <div class="resume__content-text" v-html="resumeData?.about_us"></div>
          </div>
          <div class="resume__content-block">
            <p class="resume__content-title">Мои качества:</p>
            <div class="resume__content-list">
              <p v-for="item in resumeData?.quality" :key="item" class="resume__content-item">{{item}}</p>
            </div>
          </div>
          <div class="resume__content-block">
            <p class="resume__content-title">Ключевые навыки:</p>
            <div class="resume__content-list">
              <p v-for="item in resume?.skills" :key="item" class="resume__content-item">{{item}}</p>
            </div>
          </div>
          <div class="resume__bottom">
            <p class="resume__bottom-date">Резюме было опубликовано сегодня, 16:25</p>
            <button class="button-orange-another">Связаться</button>
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
      characteristics: ['Дружелюбность', 'Отзывчивость', 'Эмпатичность', 'Вежливость', 'Ответственность'],
      skills: ['Прототипирование', 'Анализ ЦА', 'Английский язык', 'Веб-дизайн', 'Figma', 'Adobe Photoshop', 'UI/UX']
    }
  },
  methods: {
    async getResumeData() {
      try {
        const response = await axios.get('/api/res/c5762f8a-5037-4af5-a52a-f1c839613805/')
        // const applicantData = await axios.get('/api/me', { params: { createdBy: response.data.created_by } });

        console.log(response.data)
        this.resumeData = response.data
      } catch (error) {
        console.log(error)
      }
    }
  },
  mounted() {
    this.getResumeData()
  }
}
</script>

<style lang="scss" src="@/style/resume.scss">

</style>