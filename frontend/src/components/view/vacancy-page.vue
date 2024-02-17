<template>
  <section class="vacancy">
    <div class="wrapper vacancy__wrapper">
      <the-heading title="Сервис по поиску работы для молодежи"></the-heading>
      <div class="vacancy__main">
        <div class="vacancy__info">
          <p class="vacancy__info-title">{{vacancyData.job_title}}</p>
          <p class="vacancy__info-salary">
            <template
                v-if="vacancyData.salary_min && vacancyData.salary_max">
              от {{ vacancyData.salary_min }} до {{ vacancyData.salary_max }}
            </template>
            <template v-else-if="vacancyData.salary_min">от {{ vacancyData.salary_min }}</template>
            <template v-else>до {{ vacancyData.salary_max }}</template>
            рублей
          </p>
          <div class="vacancy__info-block">
            <p class="vacancy__info-text">Опыт работы: {{vacancyData.required_experience}}</p>
            <p class="vacancy__info-text">{{vacancyData.type}}</p>
            <p class="vacancy__info-text text--green">Сейчас эту вакансию смотрят 3 человека</p>
          </div>
          <div class="vacancy__info-btns">
            <button @click="sendResponse" class="button-orange-another">Откликнуться</button>
            <button class="button-orange">В избранное</button>
          </div>
        </div>
        <div class="vacancy__employer">
          <img src="@/assets/vacancy/company-logo.svg" alt="логотип компании" class="vacancy__employer-img">
          <p class="vacancy__employer-company">{{vacancyData.job_title}}</p>
          <p class="vacancy__info-text">Владивосток, ул. Ленина, 25</p>
          <p class="vacancy__info-text">8(999)888-77-66</p>
          <p class="vacancy__info-text text--green">HR, Самохина Людмила</p>
        </div>
        <div class="vacancy__description" v-html="vacancyData.description"></div>
        <div class="vacancy__bottom">
          <p class="vacancy__bottom-date">Вакансия была опубликована сегодня, 16:25</p>
          <button class="button-orange-another">Откликнуться</button>
        </div>
      </div>
      <h3 class="section-title">Рекомендуем вам</h3>
      <div class="vacancy__recommendation">
        <vacancy-item
            v-for="vacancy in vacancys"
            :vacancy="vacancy"
            :key="vacancy.id"
            class="recommendation__list-card"
        ></vacancy-item>
      </div>
    </div>
  </section>
</template>
<script>
import axios from "axios";
import VacancyItem from "@/components/ui/vacancyItem.vue";
import TheHeading from "@/components/ui/heading.vue";

export default {
  name: 'vacancy-page',
  components: {TheHeading, VacancyItem},
  props: ['id'],
  data() {
    return {
      vacancyData: {},
      employerData: {},
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
    };
  },
  methods: {
    async getVacancyData(id) {
      try {
        const response = await axios.get(`/api/vac/${id}`);
        // const employerData = await axios.get(`api/data/${response.data.id}`)
        // this.employerData = employerData

        this.vacancyData = response.data
      } catch (error) {
        console.log(error)
      }
    },
    async sendResponse() {
      const data = {
        vacancy: this.vacancyData.id,
        org: this.vacancyData.created_by,
        created_by: this.userId
      }
      try {
        await axios.post('/api/response/', JSON.stringify(data))
        console.log(data)
      } catch(error) {
        console.log(data)
        console.log(error)
      }
    }
  },
  computed: {
    userId() {
      return this.$store.state.userData.id
    }
  },
  mounted() {
    this.getVacancyData(this.id)

  },
}
</script>
<style src="@/style/vacancy-page.scss" lang="scss" scoped>

</style>
<style>
.vacancy__description {
  h2 {
    font-size: 32px;
    font-weight: 600;
    line-height: 98.023%;
    letter-spacing: -1.6px;
    &:not(:first-of-type) {
      margin-top: 64px;
    }
  }
  p {
    margin-top: 32px;
    font-size: 24px;
    line-height: 120%;
    letter-spacing: -1.2px;
  }
  @media(max-width: 1024px) {
    h2 {
      font-size: 32px;
      font-weight: 600;
      line-height: 98.023%;
      letter-spacing: -1.6px;
      &:not(:first-of-type) {
        margin-top: 48px;
      }
    }
  }
  @media(max-width: 450px) {
    h2 {
      font-size: 18px;
      letter-spacing: -0.9px;
      &:not(:first-of-type) {
        margin-top: 24px;
      }
    }
    p {
      margin-top: 16px;
      font-size: 14px;
      letter-spacing: -0.7px;
    }
  }
}
</style>