<template>
  <div>
    <section class="inner">
      <div class="wrapper inner__wrapper">
        <the-heading title="Сервис по поиску работы для подростков"></the-heading>
        <form class="inner__form">
          <input type="text" class="inner__form-search" placeholder="найти вакансию">
          <button type="button" class="inner__form-button"></button>
        </form>
        <div class="inner__info">
          <div class="inner__info-card">
            <img src="@/assets/inner/info-1.png" alt="девушка с папкой" class="inner__info-image">
            <div class="inner__info-block">
              <a href="/vacancy" class="button-orange-another inner__info-block__link">Перейти</a>
              <h4 class="inner__info-block__title">Отзывы об исполнителях и работодателях</h4>
            </div>
          </div>
          <div class="inner__info-card">
            <img src="@/assets/inner/info-2.png" alt="сужчина с табличкой" class="inner__info-image">
            <div class="inner__info-block">
              <a href="/vacancy" class="button-orange-another inner__info-block__link">Перейти</a>
              <h4 class="inner__info-block__title white">Топ вакансий на этом сервисе</h4>
            </div>
          </div>
          <div class="inner__info-card small">
            <picture>
              <source media="(max-width: 1024px)" srcset="@/assets/inner/info-3__1024.png">
              <img src="@/assets/inner/info-3.png" alt="рукопожатие" class="inner__info-image">
            </picture>
            <div class="inner__info-block">
              <a href="/vacancy" class="button-orange-another inner__info-block__link">Перейти</a>
              <h4 class="inner__info-block__title">Узнать подробнее о сервисе</h4>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section class="reviews">
      <div class="wrapper">
        <h2 class="section-title reviews__title">Отзывы</h2>
        <swiper
            :slides-per-view="1"
            :space-between="16"
            :breakpoints="breakpoints"
            :loop="false"
            :navigation="true"
            class="reviews__slider"
        >
          <swiper-slide
              v-for="review in reviewsList"
              :key="review.id"
              class="reviews__slider-item">
            <p class="reviews__slider-title">{{review.title}}</p>
            <p class="reviews__slider-text">{{review.text}}</p>
            <div class="reviews__slider-author">
              <img :src="require(`../../assets/reviews/${review.src}`)" alt="" class="reviews__slider-author__img">
              <div class="reviews__slider-author__info">
                <p class="reviews__slider-author__name">{{review.name}}</p>
                <p class="reviews__slider-author__post">{{review.post}}</p>
              </div>

            </div>
          </swiper-slide>
        </swiper>
        <a href="#" class="reviews__more">Смотреть все</a>
      </div>
    </section>
    <section class="recommendation">
      <div class="wrapper">
        <h2 class="section-title">Рекомендуем вам</h2>
        <div class="recommendation__list">
          <vacancy-item
              v-for="vacancy in ListLength"
              :vacancy="vacancy"
              :key="vacancy.id"
              class="recommendation__list-card"
          ></vacancy-item>
        </div>
        <a href="/vacancy" class="reviews__more">Смотреть все</a>
      </div>
    </section>
  </div>
</template>

<script>
import VacancyItem from "@/components/ui/vacancyItem.vue";

import { Navigation} from 'swiper'
import { SwiperCore, Swiper, SwiperSlide } from 'swiper-vue2'
SwiperCore.use([Navigation])

import 'swiper/swiper-bundle.css'
import TheHeading from "@/components/ui/heading.vue";
export default {
  name: "landing-content",
  components: {
    TheHeading,
    VacancyItem,
    Swiper,
    SwiperSlide
  },
  data() {
    return {
      breakpoints: {
        1440: {
          slidesPerView: 4
        },
        1100: {
          slidesPerView: 3
        },
        850: {
          slidesPerView: 2
        }
      },
      currentSliderStep: 0,
      reviews: [
        {
          title: 'Нужно оформить презентацию перед запуском продукта',
          text: 'Нашла исполнителя за 1 час, который проявил исключительные навыки и профессионализм при оформлении презентации. Было произведено глубокое понимание нашего бизнеса. Был внимателен к деталям и учел все наши требования и пожелания.',
          src: 'person-1.png',
          name: 'Алена Игнатова',
          post: 'HR, Компания Юла'
        },
        {
          title: 'Нужно сделать лендинг салона красоты',
          text: 'Нашла исполнителя за 1 час, который проявил исключительные навыки и профессионализм при создании лендинга. Было произведено глубокое понимание нашего бизнеса. Был внимателен к деталям и учел все наши требования и пожелания.',
          src: 'person-2.png',
          name: 'Мария Погорелова',
          post: 'Владелец салона красоты'
        },
        {
          title: 'Нужно сделать креативы и баннеры для рекламы',
          text: 'Быстро откликнулся молодой человек. Уже через два дня у меня были отличные баннеры и креативы для рекламы Был внимателен к деталям и учел все требования и пожелания.',
          src: 'person-3.png',
          name: 'Артём Васильев',
          post: 'Владелец студии тату'
        },
        {
          title: 'Нужно сверстать сайт для компании',
          text: 'Загрузил объявление, через день откликнулась девушка. Всё было выполнено на высшем уровне - обсудили все детали и подписали договор. Через месяц у меня уже был готовый сайт из 40 страниц. Огромное спасибо!',
          src: 'person-4.png',
          name: 'Сергей Андреев',
          post: 'ИП, Строительная компания'
        },
        {
          title: 'Нужно оформить презентацию перед запуском продукта',
          text: 'Нашла исполнителя за 1 час, который проявил исключительные навыки и профессионализм при оформлении презентации. Было произведено глубокое понимание нашего бизнеса. Был внимателен к деталям и учел все наши требования и пожелания.',
          src: 'person-1.png',
          name: 'Алена Игнатова',
          post: 'HR, Компания Юла'
        },
      ],
      vacancys: [
        {
          title: 'Дизайнер интерфейсов',
          requirements: 'Хорошее понимание UI/UX базы; понимание всех нюансов разработки современных сайтов.',
          tasks: 'Разработка макетов и адаптивов, упаковка готовых решений в презентации.',
          salary: '35 000 рублей'
        },
        {
          title: 'Дизайнер интерфейсов',
          requirements: 'Хорошее понимание UI/UX базы; понимание всех нюансов разработки современных сайтов.',
          tasks: 'Разработка макетов и адаптивов, упаковка готовых решений в презентации.',
          salary: '35 000 рублей'
        },
        {
          title: 'Дизайнер интерфейсов',
          requirements: 'Хорошее понимание UI/UX базы; понимание всех нюансов разработки современных сайтов.',
          tasks: 'Разработка макетов и адаптивов, упаковка готовых решений в презентации.',
          salary: '35 000 рублей'
        },
        {
          title: 'Дизайнер интерфейсов',
          requirements: 'Хорошее понимание UI/UX базы; понимание всех нюансов разработки современных сайтов.',
          tasks: 'Разработка макетов и адаптивов, упаковка готовых решений в презентации.',
          salary: '35 000 рублей'
        },
        {
          title: 'Дизайнер интерфейсов',
          requirements: 'Хорошее понимание UI/UX базы; понимание всех нюансов разработки современных сайтов.',
          tasks: 'Разработка макетов и адаптивов, упаковка готовых решений в презентации.',
          salary: '35 000 рублей'
        },
        {
          title: 'Дизайнер интерфейсов',
          requirements: 'Хорошее понимание UI/UX базы; понимание всех нюансов разработки современных сайтов.',
          tasks: 'Разработка макетов и адаптивов, упаковка готовых решений в презентации.',
          salary: '35 000 рублей'
        },
      ],
    }
  },
  methods: {
  },
  computed: {
    ListLength() {
      if (window.innerWidth > 1440) {
        return this.vacancys.slice(0, 6)
      }
      return this.vacancys.slice(0, 4)
    },
    reviewsList() {
      return this.reviews.map(review => {
        if (review.text.length > 250) {
          return {
            ...review,
            text: review.text.slice(0, 247) + '...'
          };
        }
        return review;
      });
    },
  },
  mounted() {

  }
}
</script>

<style lang="scss">
@import "@/style/landing";

</style>
