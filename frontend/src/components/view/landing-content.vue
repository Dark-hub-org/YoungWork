<template>
<main class="main">
  <section class="inner">
    <div class="wrapper inner-wrapper">
      <h1 class="inner-title">Сервис по поиску работы для подростков </h1>
      <form class="inner-form">
        <input type="text" class="inner-form__search" placeholder="найти вакансию">
        <button type="button" class="inner-form__button"></button>
      </form>
      <div class="inner-info">
        <div class="inner-info__card">
          <img src="@/assets/inner/info-1.png" alt="девушка с папкой" class="inner-info-image">
          <div class="info__card-block">
              <a href="#" class="button-orange-another info__card-block__link">Перейти</a>
              <h4 class="info__card-block__title">Отзывы об исполнителях и работодателях</h4>
          </div>
        </div>
        <div class="inner-info__card">
          <img src="@/assets/inner/info-2.png" alt="сужчина с табличкой" class="inner-info-image">
          <div class="info__card-block">
              <a href="#" class="button-orange-another info__card-block__link">Перейти</a>
              <h4 class="info__card-block__title white">Топ вакансий на этом сервисе</h4>
          </div>
        </div>
        <div class="inner-info__card">
          <picture>
            <source media="(max-width: 1024px)" srcset="@/assets/inner/info-3__1024.png">
            <img src="@/assets/inner/info-3.png" alt="рукопожатие" class="inner-info-image">
          </picture>
          <div class="info__card-block">
              <a href="#" class="button-orange-another info__card-block__link">Перейти</a>
              <h4 class="info__card-block__title">Узнать подробнее о сервисе</h4>
          </div>
        </div>
      </div>
    </div>
  </section>
  <section class="reviews">
    <div class="wrapper">
      <h2 class="section-title reviews-title">Отзывы</h2>
      <div class="reviews-slider">
        <slider-item
          v-for="review in reviews"
          :review="review"
          :key="review.id"
        ></slider-item>
      </div>
      <a href="#" class="reviews-more">Смотреть все</a>
    </div>
  </section>
  <section class="recommendation">
    <div class="wrapper">
      <h2 class="section-title">Рекомендуем вам</h2>
      <div class="recommendation-block">
          <vacancy-item
            v-for="vacancy in ListLength"
            :vacancy="vacancy"
            :key="vacancy.id"
          ></vacancy-item>
      </div>
      <a href="#" class="reviews-more">Смотреть все</a>
    </div>
  </section>
</main>
</template>

<script>
import SliderItem from "@/components/ui/sliderItem.vue";
import VacancyItem from "@/components/ui/vacancyItem.vue";

export default {
  name: "landing-content",
  components: {
    VacancyItem,
    SliderItem,
  },
  data() {
    return {
      reviews: [
        {title: 'Нужно оформить презентацию перед запуском продукта', text: 'Нашла исполнителя за 1 час, который проявил исключительные навыки и профессионализм при оформлении презентации. Было произведено глубокое понимание нашего бизнеса. Был внимателен к деталям и учел все наши требования и пожелания.', src: 'person-1.png', name: 'Алена Игнатова', post: 'HR, Компания Юла'},
        {title: 'Нужно сделать лендинг салона красоты', text: 'Нашла исполнителя за 1 час, который проявил исключительные навыки и профессионализм при создании лендинга. Было произведено глубокое понимание нашего бизнеса. Был внимателен к деталям и учел все наши требования и пожелания.', src: 'person-2.png', name: 'Мария Погорелова', post: 'Владелец салона красоты'},
        {title: 'Нужно сделать креативы и баннеры для рекламы', text: 'Быстро откликнулся молодой человек. Уже через два дня у меня были отличные баннеры и креативы для рекламы Был внимателен к деталям и учел все требования и пожелания.', src: 'person-3.png', name: 'Артём Васильев', post: 'Владелец студии тату'},
        {title: 'Нужно сверстать сайт для компании', text: 'Загрузил объявление, через день откликнулась девушка. Всё было выполнено на высшем уровне - обсудили все детали и подписали договор. Через месяц у меня уже был готовый сайт из 40 страниц. Огромное спасибо!', src: 'person-4.png', name: 'Сергей Андреев', post: 'ИП, Строительная компания'},
      ],
      vacancys: [
        {title: 'Дизайнер интерфейсов', requirements: 'Хорошее понимание UI/UX базы; понимание всех нюансов разработки современных сайтов.', tasks: 'Разработка макетов и адаптивов, упаковка готовых решений в презентации.', salary: '35 000 рублей'},
        {title: 'Дизайнер интерфейсов', requirements: 'Хорошее понимание UI/UX базы; понимание всех нюансов разработки современных сайтов.', tasks: 'Разработка макетов и адаптивов, упаковка готовых решений в презентации.', salary: '35 000 рублей'},
        {title: 'Дизайнер интерфейсов', requirements: 'Хорошее понимание UI/UX базы; понимание всех нюансов разработки современных сайтов.', tasks: 'Разработка макетов и адаптивов, упаковка готовых решений в презентации.', salary: '35 000 рублей'},
        {title: 'Дизайнер интерфейсов', requirements: 'Хорошее понимание UI/UX базы; понимание всех нюансов разработки современных сайтов.', tasks: 'Разработка макетов и адаптивов, упаковка готовых решений в презентации.', salary: '35 000 рублей'},
        {title: 'Дизайнер интерфейсов', requirements: 'Хорошее понимание UI/UX базы; понимание всех нюансов разработки современных сайтов.', tasks: 'Разработка макетов и адаптивов, упаковка готовых решений в презентации.', salary: '35 000 рублей'},
        {title: 'Дизайнер интерфейсов', requirements: 'Хорошее понимание UI/UX базы; понимание всех нюансов разработки современных сайтов.', tasks: 'Разработка макетов и адаптивов, упаковка готовых решений в презентации.', salary: '35 000 рублей'},
        {title: 'Дизайнер интерфейсов', requirements: 'Хорошее понимание UI/UX базы; понимание всех нюансов разработки современных сайтов.', tasks: 'Разработка макетов и адаптивов, упаковка готовых решений в презентации.', salary: '35 000 рублей'},
        {title: 'Дизайнер интерфейсов', requirements: 'Хорошее понимание UI/UX базы; понимание всех нюансов разработки современных сайтов.', tasks: 'Разработка макетов и адаптивов, упаковка готовых решений в презентации.', salary: '35 000 рублей'},
      ]
    }
  },
  computed: {
    ListLength() {
      if(window.innerWidth > 1024) {
        return this.vacancys.slice(0, 8)
      }
        return this.vacancys.slice(0, 6)
    }
  }
}
</script>

<style lang="scss">
@import "@/style/landing";
.main {
  margin-top: 158px;
}

</style>
