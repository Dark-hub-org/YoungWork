<template>
  <section class="constructor">
    <div class="wrapper constructor-wrapper">
      <!--      <div ref="banner" class="dropzone constructor__banner">-->
      <!--        <div class="constructor__banner-wrapper">-->
      <!--          <p class="constructor__banner-title">Загрузите тизер</p>-->
      <!--          <div class="constructor__banner-cross"></div>-->
      <!--        </div>-->
      <!--      </div>-->
      <h2 class="constructor__title">Создание вакансии</h2>
      <form class="constructor__form">
        <div class="constructor__form-block">
          <p class="constructor__form-block__name">Напишите название вакансии:</p>
          <input
              v-model.trim="vacancyTitle"
              v-restrict-input-length="120"
              :class="{ error: errorFields.vacancyTitle }"
              @input="errorFields.vacancyTitle = false"
              type="text"
              class="constructor__form-block__input not-margin"
              placeholder="Дизайнер">
          <span
              class="constructor__form-block__error"
              :class="{ active: errorFields.vacancyTitle }">Заполните поле</span>
        </div>
        <div class="constructor__form-block">
          <p class="constructor__form-block__name">Уровень заработной платы:</p>
          <input
              v-model.number="salaryMin"
              type="number"
              class="constructor__form-block__input small"
              placeholder="От">
          <span
              class="constructor__form-block__error">Заполните поле</span>
          <input
              v-model.number="salaryMax"
              type="number"
              class="constructor__form-block__input small"
              placeholder="До">
          <span
              class="constructor__form-block__error">Заполните поле</span>
          <div class="constructor__form-parameter">
            <input
                v-model="isSalaryTask"
                type="radio"
                value="До вычета налогов"
                name="salary"
                class="constructor__form-parameter__input"
                id="beforeDed" checked>
            <label for="beforeDed" class="constructor__form-parameter__label radio">До вычета налогов</label>
          </div>
          <div class="constructor__form-parameter">
            <input
                v-model="isSalaryTask"
                type="radio"
                name="salary"
                value="На руки"
                class="constructor__form-parameter__input"
                id="afterDed">
            <label for="afterDed" class="constructor__form-parameter__label radio">На руки</label>
          </div>
        </div>
        <div class="constructor__form-block">
          <p class="constructor__form-block__name">Укажите тип занятости:</p>
          <div class="constructor__form-parameter">
            <input
                v-model="employ"
                type="checkbox"
                name="employ"
                value="Полная занятость"
                class="constructor__form-parameter__input"
                id="fullEmploy"
                checked>
            <label
                for="fullEmploy"
                class="constructor__form-parameter__label check"
                :class="{error: errorFields.employ }">Полная занятость</label>

          </div>
          <div class="constructor__form-parameter">
            <input
                v-model="employ"
                type="checkbox"
                name="employ"
                value="Частичная занятость"
                class="constructor__form-parameter__input"
                id="partialEmploy">
            <label
                for="partialEmploy"
                class="constructor__form-parameter__label check"
                :class="{error: errorFields.employ }">Частичная занятость</label>
          </div>
          <div class="constructor__form-parameter">
            <input
                v-model="employ"
                type="checkbox"
                name="employ"
                value="Стажировка"
                class="constructor__form-parameter__input"
                id="internship">
            <label
                for="internship"
                class="constructor__form-parameter__label check"
                :class="{error: errorFields.employ }">Стажировка</label>
          </div>
          <div class="constructor__form-parameter">
            <input
                v-model="employ"
                type="checkbox"
                name="employ"
                value="Проектная работа"
                class="constructor__form-parameter__input"
                id="projectWork">
            <label
                for="projectWork"
                class="constructor__form-parameter__label check"
                :class="{error: errorFields.employ }">Проектная работа</label>
          </div>
          <div class="constructor__form-parameter">
            <input
                v-model="employ"
                type="checkbox"
                name="employ"
                value="Волонтерство"
                class="constructor__form-parameter__input"
                id="volunteering">
            <label
                for="volunteering"
                class="constructor__form-parameter__label check"
                :class="{error: errorFields.employ }">Волонтерство</label>
          </div>
          <span
              class="constructor__form-block__error"
              :class="{ active: errorFields.employ }">Заполните поле</span>
        </div>
        <div class="constructor__form-block">
          <p class="constructor__form-block__name">Укажите требуемый опыт работы:</p>
          <div class="constructor__form-parameter">
            <input
                v-model="experience"
                type="radio"
                name="exp"
                value="Не имеет значения"
                class="constructor__form-parameter__input" id="exp-1"
                checked>
            <label for="exp-1" class="constructor__form-parameter__label radio">Не имеет значения</label>
          </div>
          <div class="constructor__form-parameter">
            <input
                v-model="experience"
                type="radio"
                name="exp"
                value="от 1 года до 3 лет"
                class="constructor__form-parameter__input" id="exp-2">
            <label for="exp-2" class="constructor__form-parameter__label radio">от 1 года до 3 лет</label>
          </div>
          <div class="constructor__form-parameter">
            <input
                v-model="experience"
                type="radio"
                name="exp"
                value="От 3 до 6 лет"
                class="constructor__form-parameter__input"
                id="exp-3">
            <label for="exp-3" class="constructor__form-parameter__label radio">От 3 до 6 лет</label>
          </div>
          <div class="constructor__form-parameter">
            <input
                v-model="experience"
                type="radio"
                name="exp"
                value="Нет опыта"
                class="constructor__form-parameter__input"
                id="exp-4">
            <label for="exp-4" class="constructor__form-parameter__label radio">Нет опыта</label>
          </div>
          <div class="constructor__form-parameter">
            <input
                v-model="experience"
                type="radio"
                name="exp"
                value="Более 6 лет"
                class="constructor__form-parameter__input"
                id="exp-5">
            <label for="exp-5" class="constructor__form-parameter__label radio">Более 6 лет</label>
          </div>
        </div>
        <div class="constructor__form-block">
          <p class="constructor__form-block__name">График работы</p>
          <div class="constructor__form-parameter employ">
            <input
                v-model="graph"
                @change="errorFields.graph = false"
                type="checkbox"
                class="constructor__form-parameter__input"
                id="graph-1"
                value="Полный день">
            <label
                for="graph-1"
                class="constructor__form-parameter__label check"
                :class="{error: errorFields.graph }">Полный день</label>
          </div>
          <div class="constructor__form-parameter employ">
            <input
                v-model="graph"
                @change="errorFields.graph = false"
                type="checkbox"
                class="constructor__form-parameter__input"
                id="graph-2"
                value="Удаленная работа">
            <label
                for="graph-2"
                class="constructor__form-parameter__label check"
                :class="{error: errorFields.graph }">Удаленная работа</label>
          </div>
          <div class="constructor__form-parameter employ">
            <input
                v-model="graph"
                @change="errorFields.graph = false"
                type="checkbox"
                class="constructor__form-parameter__input"
                id="graph-3"
                value="Сменный график">
            <label
                for="graph-3"
                class="constructor__form-parameter__label check"
                :class="{ error: errorFields.graph }">Сменный график</label>
          </div>
          <div class="constructor__form-parameter employ">
            <input
                v-model="graph"
                @change="errorFields.graph = false"
                type="checkbox"
                class="constructor__form-parameter__input"
                id="graph-4"
                value="Гибкий график">
            <label
                for="graph-4"
                class="constructor__form-parameter__label check"
                :class="{error: errorFields.graph }">Гибкий график</label>
          </div>
          <div class="constructor__form-parameter employ">
            <input
                v-model="graph"
                @change="errorFields.graph = false"
                type="checkbox"
                class="constructor__form-parameter__input"
                id="graph-5"
                value="Вахтовый метод">
            <label
                for="graph-5"
                class="constructor__form-parameter__label check"
                :class="{error: errorFields.graph }">Вахтовый метод</label>
          </div>
          <span
              class="constructor__form-block__error"
              :class="{ active: errorFields.graph }">Заполните поле</span>
        </div>
        <div
            class="constructor__form-ckeditor-wrapper">
          <ckeditor
              :config="editorConfig"
              v-model="description"
              @input="errorFields.description = false"
              :class="{error: errorFields.description}"
              class="constructor__form-ckeditor"></ckeditor>
          <span
              class="constructor__form-block__error"
              :class="{ active: errorFields.description }">Заполните поле</span>
        </div>
        <div class="constructor-contact">
        </div>
        <div class="constructor__form-btns">
          <button
              type="submit"
              @click.prevent="createVacancy"
              class="button-orange-another constructor__form-submit"
          >Опубликовать
          </button>
        </div>
      </form>
    </div>
  </section>
</template>
<script>

import axios from "axios";
import Vue from 'vue';

Vue.directive('restrict-input-length', {
  bind(el, binding) {
    el.addEventListener('input', (event) => {
      const maxLength = binding.value;
      if (event.target.value.length > maxLength) {
        event.target.value = event.target.value.slice(0, maxLength);
      }
    });
  }
});

export default {
  data() {
    return {
      editorConfig: {
        toolbar: [['Bold'], ['Italic'], ['Underline'], ['Strike'], ['NumberedList'], ['BulletedList'], ['Styles'], ['Format']],
      },
      description:
          "<p><strong>О компании / заказчике:</strong></p" +
          "<ul><li></li></ul>" +
          "<p><strong>Обязанности:</strong></p>" +
          "<ul><li></li></ul>" +
          "<p><strong>Требования:</strong></p>" +
          "<ul><li></li></ul>" +
          "<p><strong>Условия:</strong></p>" +
          "<ul><li></li></ul>",
      tasks: '',
      requirements: this.description,
      isSalaryTask: "До вычета налогов",
      employ: ['Полная занятость',],
      experience: 'Не имеет значения',
      graph: ["Полный день",],

      vacancyTitle: '',
      salaryMin: null,
      salaryMax: null,
      type: '',
      logo: '',
      errorFields: {
        vacancyTitle: false,
        salary: false,
        employ: false,
        graph: false,
        description: false,
      }
    }
  },
  methods: {
    async createVacancy() {
      try {
        this.parseResponsibilities(this.description, 'Обязанности')
        this.parseResponsibilities(this.description, 'Требования')
        const vacancyData = {
          job_title: this.vacancyTitle,
          company_name: this.userData.title_org,
          salary_min: this.salaryMin,
          salary_max: this.salaryMax,
          description: this.description,
          tasks: this.tasks,
          requirements: this.requirements,
          tax: this.isSalaryTask,
          employ: this.employ,
          required_experience: this.experience,
          created_by: this.userData.id,
          graph: this.graph,
          title_org: this.userData.title_org,
          citizenship: this.userData.city,
          phone_number: this.userData.phoneNumber,
          first_name: this.userData.firstName,
          last_name: this.userData.lastName,
          com_logo: this.userData.photo_org,
          region: this.userData.region,
        };
        if (this.validateFormVacancy()) {
          await axios.post('/create-vacancy/', vacancyData)
          this.$router.push('/employer')
          localStorage.setItem('applicantTab', JSON.stringify(2));
        }
      } catch (error) {
        console.log(error)
      }
    },
    parseResponsibilities(description, codeWord) {
      const parser = new DOMParser();
      const doc = parser.parseFromString(description, 'text/html');
      const strongParagraphs = doc.querySelectorAll('p');
      let responsibilitiesList = null;
      for (const strongParagraph of strongParagraphs) {

        if (strongParagraph.textContent.includes(codeWord)) {
          responsibilitiesList = strongParagraph.nextElementSibling;
          break;
        }
      }

      if (responsibilitiesList && responsibilitiesList.tagName.toLowerCase() === 'ul') {
        const responsibilitiesArray = Array.from(responsibilitiesList.querySelectorAll('li')).map(li => li.textContent.trim());

        if (responsibilitiesArray.length > 0) {
          if (codeWord === 'Обязанности') {
            this.tasks = `${responsibilitiesArray.join(', ')}`;
          } else if (codeWord === 'Требования') {
            this.requirements = `${responsibilitiesArray.join(', ')}`;
          }

        }
      }
    },
    validateField(value) {
      return value.length === 0;
    },
    validateFormVacancy() {
      this.errorFields.vacancyTitle = this.validateField(this.vacancyTitle)
      this.errorFields.graph = this.validateField(this.graph)
      this.errorFields.employ = this.validateField(this.employ)
      this.errorFields.description = this.validateField(this.description)
      return Object.values(this.errorFields).every((error) => !error)
    },
  },
  computed: {
    userData() {
      return this.$store.state.userData
    },
  },
  mounted() {
  }
}
</script>
<style src="@/style/create.scss" lang="scss" scoped>

</style>
