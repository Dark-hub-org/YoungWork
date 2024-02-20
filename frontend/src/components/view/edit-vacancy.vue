<template>
  <section class="constructor">
    <div class="wrapper constructor-wrapper">
      <div class="constructor__banner">
        <div class="constructor__banner-wrapper">
          <p class="constructor__banner-title">Загрузите тизер</p>
          <input type="file" name="image" class="constructor__banner-input">
          <div class="constructor__banner-cross"></div>
        </div>
      </div>
      <h2 class="constructor__title">Создание вакансии</h2>
      <form class="constructor__form">
        <div class="constructor__form-block">
          <p class="constructor__form-block__name">Напишите название вакансии:</p>
          <input
              v-model.trim="vacancyData.job_title"
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
              v-model.number="vacancyData.salary_min"
              type="number"
              class="constructor__form-block__input small"
              placeholder="От">
          <span
              class="constructor__form-block__error">Заполните поле</span>
          <input
              v-model.number="vacancyData.salary_max"
              type="number"
              class="constructor__form-block__input small"
              placeholder="До">
          <span
              class="constructor__form-block__error">Заполните поле</span>
          <div class="constructor__form-parameter">
            <input
                v-model="vacancyData.tax"
                type="radio"
                value="До вычета налогов"
                name="salary"
                class="constructor__form-parameter__input"
                id="beforeDed" checked>
            <label for="beforeDed" class="constructor__form-parameter__label radio">До вычета налогов</label>
          </div>
          <div class="constructor__form-parameter">
            <input
                v-model="vacancyData.tax"
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
                v-model="vacancyData.employ"
                type="radio"
                name="employ"
                value="Полная занятость"
                class="constructor__form-parameter__input"
                id="fullEmploy"
                checked>
            <label for="fullEmploy" class="constructor__form-parameter__label radio">Полная занятость</label>
          </div>
          <div class="constructor__form-parameter">
            <input
                v-model="vacancyData.employ"
                type="radio"
                name="employ"
                value="Частичная занятость"
                class="constructor__form-parameter__input"
                id="partialEmploy">
            <label for="partialEmploy" class="constructor__form-parameter__label radio">Частичная занятость</label>
          </div>
          <div class="constructor__form-parameter">
            <input
                v-model="vacancyData.employ"
                type="radio"
                name="employ"
                value="Стажировка"
                class="constructor__form-parameter__input"
                id="internship">
            <label for="internship" class="constructor__form-parameter__label radio">Стажировка</label>
          </div>
          <div class="constructor__form-parameter">
            <input
                v-model="vacancyData.employ"
                type="radio"
                name="employ"
                value="Проектная работа"
                class="constructor__form-parameter__input"
                id="projectWork">
            <label for="projectWork" class="constructor__form-parameter__label radio">Проектная работа</label>
          </div>
          <div class="constructor__form-parameter">
            <input
                v-model="vacancyData.employ"
                type="radio"
                name="employ"
                value="Волонтерство"
                class="constructor__form-parameter__input"
                id="volunteering">
            <label for="volunteering" class="constructor__form-parameter__label radio">Волонтерство</label>
          </div>
        </div>
        <div class="constructor__form-block">
          <p class="constructor__form-block__name">Укажите требуемый опыт работы:</p>
          <div class="constructor__form-parameter">
            <input
                v-model="vacancyData.required_experience"
                type="radio"
                name="exp"
                value="Не имеет значения"
                class="constructor__form-parameter__input" id="exp-1"
                checked>
            <label for="exp-1" class="constructor__form-parameter__label radio">Не имеет значения</label>
          </div>
          <div class="constructor__form-parameter">
            <input
                v-model="vacancyData.required_experience"
                type="radio"
                name="exp"
                value="от 1 года до 3 лет"
                class="constructor__form-parameter__input" id="exp-2">
            <label for="exp-2" class="constructor__form-parameter__label radio">от 1 года до 3 лет</label>
          </div>
          <div class="constructor__form-parameter">
            <input
                v-model="vacancyData.required_experience"
                type="radio"
                name="exp"
                value="От 3 до 6 лет"
                class="constructor__form-parameter__input"
                id="exp-3">
            <label for="exp-3" class="constructor__form-parameter__label radio">От 3 до 6 лет</label>
          </div>
          <div class="constructor__form-parameter">
            <input
                v-model="vacancyData.required_experience"
                type="radio"
                name="exp"
                value="Нет опыта"
                class="constructor__form-parameter__input"
                id="exp-4">
            <label for="exp-4" class="constructor__form-parameter__label radio">Нет опыта</label>
          </div>
          <div class="constructor__form-parameter">
            <input
                v-model="vacancyData.required_experience"
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
                v-model="vacancyData.graph"
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
                v-model="vacancyData.graph"
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
                v-model="vacancyData.graph"
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
                v-model="vacancyData.graph"
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
                v-model="vacancyData.graph"
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
              v-model="vacancyData.description"
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
              @click.prevent="editVacancyData"
              class="button-orange-another constructor__form-submit"
          >Сохранить
          </button>
          <button
              @click="switchVacancyActive(vacancyData.active = !vacancyData.active)"
              type="button"
              class="button-orange constructor__form-submit"
          >
            <template v-if="vacancyData.active">Добавить в архив</template>
            <template v-else>Сделать активной</template>
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
      vacancyId: '',
      vacancyData: {},
      errorFields: {
        vacancyTitle: false,
        salary: false,
        graph: false,
        description: false,
      },
    }
  },
  methods: {
    async getVacancyData() {
      try {
        const vacancyData  = await axios(`/api/vac/${this.vacancyId}`)
        this.vacancyData = vacancyData.data
      } catch (error) {
        console.log(error)
      }
    },
    async editVacancyData() {
      this.parseResponsibilities(this.vacancyData.description, 'Обязанности')
      this.parseResponsibilities(this.vacancyData.description, 'Требования')
      try {
        if(this.validateFormVacancy) {
          await axios.patch(`/api/edit-vacancy/${this.vacancyData.id}/`, this.vacancyData)
          window.location.reload()
        }
      } catch(error) {
        console.log(error)
        console.log(this.vacancyData)
      }
    },
    async switchVacancyActive(isActive) {
      try {
        if(!isActive) {
          await axios.post('/api/inactive/vac/', {pk: this.vacancyData.id})
        } else {
          await axios.post('/api/active/vac/', {pk: this.vacancyData.id})
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
            this.vacancyData.tasks = `${responsibilitiesArray.join(', ')}`;
          } else if (codeWord === 'Требования') {
            this.vacancyData.requirements = `${responsibilitiesArray.join(', ')}`;
          }

        }
      }
    },
    validateField(value) {
      return value.length === 0;
    },
    validateFormVacancy() {
      this.errorFields.vacancyTitle = this.validateField(this.vacancyData.job_title)
      this.errorFields.graph = this.validateField(this.vacancyData.graph)
      this.errorFields.description = this.validateField(this.vacancyData.description)
      return Object.values(this.errorFields).every((error) => !error)
    },
  },
  computed: {
    userId() {
      return this.$store.state.userData.id
    },
    companyName() {
      return this.$store.state.userData.title_org
    }
  },
  mounted() {
    this.vacancyId = this.$route.params.id
    this.getVacancyData()
  }
}
</script>
<style src="@/style/create.scss" lang="scss" scoped>

</style>