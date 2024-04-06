<template>
  <section class="response">
    <div class="wrapper">
      <the-heading title="Отклики на вакансию"></the-heading>
      <p class="response__quantity">Количество откликов: 32</p>
      <div class="response__list">
        <div class="response__item">
          <div class="response__item-left">
            <img src="" alt="фото соискатель" class="response__item-img">
            <p class="response__item-name">Александра Андреева</p>
            <p class="response__item-age">19 лет</p>
            <div class="response__item-social">
              <div class="response__item-social__block">
                <img src="@/assets/telegram-icon.svg" alt="" class="response__item-social__img">
                <a href="https://t.me/" class="response__item-social__link">@as8691_1</a>
              </div>
              <div class="response__item-social__block">
                <img src="@/assets/email-icon.svg" alt="" class="response__item-social__img">
                <a href="mailto:" class="response__item-social__link">sasha-andreeva-1998@list.ru</a>
              </div>
              <div class="response__item-social__block">
                <img src="@/assets/phone-icon.svg" alt="" class="response__item-social__img">
                <a href="tel:" class="response__item-social__link">+7 999 888 77 66</a>
              </div>
              <div class="response__item-social__block">
                <img src="@/assets/link-icon.svg" alt="" class="response__item-social__img">
                <a href="" target="_blank" class="response__item-social__link response__item-social__site">https://dprofile.ru/andreeva_design</a>
              </div>
            </div>
          </div>
          <div class="response__item-right">
            <div class="response__item-top">
              <p class="response__item-title">Дизайнер UI/UX</p>
              <p class="response__item-exp">Опыт: 2 года</p>
            </div>
            <div class="response__item-block">
              <p class="response__item-subtitle">Навыки:</p>
              <div class="response__item-about">

              </div>
            </div>
            <div class="response__item-block">
              <p class="response__item-subtitle">Об исполнителе:</p>
              <div class="response__item-about">
                <p>Дипломированный специалист. Работаю в большой компании в отделе дизайна. Своя команда веб-студии.</p>
                <p>В работе люблю делать так, чтобы было просто и удобно, но стилёво.  С моим портфолио  можете ознакомиться по прикрепленной ссылке.</p>
              </div>
            </div>
            <div class="response__item-bottom">
              <button type="button" class="button-orange-another response__item-response">Откликнуться</button>
              <button type="button" class="button-orange-another response__item-response">В избранное</button>
              <router-link to="/" tag="a" class="response__item-profile">Перейти в профиль</router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "axios";
import TheHeading from "@/components/ui/heading.vue";

export default {
  name: 'response-vacancy',
  components: {TheHeading},
  data() {
    return {

    }
  },
  methods: {
    async getResponse(id) {
      try {
        const response = await axios.get('/api/all-response/', {pk: id})
        console.log(response)
      } catch (error) {
        console.log(error)
      }
    }
  },
  mounted() {
    this.getResponse(this.$route.params.id)
  }
}
</script>

<style src="@/style/response.scss" lang="scss">

</style>