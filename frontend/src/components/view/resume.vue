<template>
  <section class="resume">
    <div class="wrapper">
      <the-heading title="Сервис по поиску работы для подростков"/>
      <div class="resume__main">
        <div class="resume__top">
          <p class="resume__top-title">UI/UX дизайнер</p>
          <p class="resume__top-summery">50 000 рублей</p>
          <div class="resume__top-block">
            <p class="resume__top-text">Опыт работы: нет опыта</p>
            <p class="resume__top-text">Частичная занятость, полная занятость</p>
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
            <p class="resume__content-text">Работаю поэтапно, начинаю с поиска и анализа информации. Выделяю ключевые проблемы и особенности, формирую гипотезы. На основании аналитической части создаю функциональный прототип и поэтапно детализирую, доводя до готовой визуальной концепции.

            Люблю искать решения задач в дизайне и других сферах. Расширяю и углубляю свои знания через книги, лекции и курсы (на данный момент прохожу курсы UPROCK).</p>
          </div>
          <div class="resume__content-block">
            <p class="resume__content-title">Мои качества:</p>
            <div class="resume__content-list">
              <p v-for="item in characteristics" :key="item" class="resume__content-item">{{item}}</p>
            </div>
          </div>
          <div class="resume__content-block">
            <p class="resume__content-title">Ключевые навыки:</p>
            <div class="resume__content-list">
              <p v-for="item in skills" :key="item" class="resume__content-item">{{item}}</p>
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

export default {
  components: {TheHeading},
  name: 'resume-page',
  data() {
    return {
      characteristics: ['Дружелюбность', 'Отзывчивость', 'Эмпатичность', 'Вежливость', 'Ответственность'],
      skills: ['Прототипирование', 'Анализ ЦА', 'Английский язык', 'Веб-дизайн', 'Figma', 'Adobe Photoshop', 'UI/UX']
    }
  }
}
</script>

<style lang="scss" src="@/style/resume.scss">

</style>