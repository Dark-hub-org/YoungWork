<template>
  <section class="constructor">
    <div class="wrapper constructor-wrapper">
      <div class="upload-image">
        <div class="upload-image__wrapper">
          <p class="upload-image-title">Загрузите тизер</p>
          <input type="file" name="image" class="upload-image-input">
          <div class="upload-image__cross"></div>
        </div>
      </div>
      <form class="parameters-form">
        <h2 class="constructor-title">Создание вакансии</h2>
        <div class="parameters-form__wrapper">
          <span class="parameters-form__wrapper__name">Напишите название вакансии:</span>
          <input
              v-model.trim="nameVacancy"
              v-restrict-input-length="120"
              type="text"
              class="parameters-form__wrapper__text"
              placeholder="ООО “Маршмеллоу”">
        </div>
        <div class="parameters-form__wrapper">
          <span class="parameters-form__wrapper__name">Уровень заработной платы:</span>
          <input v-model.number="levelSalMin" type="number" class="parameters-form__wrapper__text small margin-bottom"
                 placeholder="От">
          <input v-model.number="levelSalMax" type="number" class="parameters-form__wrapper__text small margin-bottom"
                 placeholder="До">
          <div class="parameters-filter__block">
            <input v-model="isSalaryTask" type="radio" value="beforeTax" name="salary" class="parameters-filter__input"
                   id="beforeDed" checked>
            <label for="beforeDed" class="parameters-filter-label radio">До вычета налогов</label>
          </div>
          <div class="parameters-filter__block">
            <input v-model="isSalaryTask" type="radio" name="salary" value="afterTax" class="parameters-filter__input"
                   id="afterDed">
            <label for="afterDed" class="parameters-filter-label radio">На руки</label>
          </div>
        </div>
        <div class="parameters-form__wrapper">
          <span class="parameters-form__wrapper__name">Укажите тип занятости:</span>
          <div class="parameters-filter__block">
            <input v-model="employ" type="radio" name="employ" value="fullEmploy" class="parameters-filter__input"
                   id="fullEmploy" checked>
            <label for="fullEmploy" class="parameters-filter-label radio">Полная занятость</label>
          </div>
          <div class="parameters-filter__block">
            <input v-model="employ" type="radio" name="employ" value="partialEmploy" class="parameters-filter__input"
                   id="partialEmploy">
            <label for="partialEmploy" class="parameters-filter-label radio">Частичная занятость</label>
          </div>
          <div class="parameters-filter__block">
            <input v-model="employ" type="radio" name="employ" value="internship" class="parameters-filter__input"
                   id="internship">
            <label for="internship" class="parameters-filter-label radio">Стажировка</label>
          </div>
          <div class="parameters-filter__block">
            <input v-model="employ" type="radio" name="employ" value="projectWork" class="parameters-filter__input"
                   id="projectWork">
            <label for="projectWork" class="parameters-filter-label radio">Проектная работа</label>
          </div>
          <div class="parameters-filter__block">
            <input v-model="employ" type="radio" name="employ" value="volunteering" class="parameters-filter__input"
                   id="volunteering">
            <label for="volunteering" class="parameters-filter-label radio">Волонтерство</label>
          </div>
        </div>
        <div class="parameters-form__wrapper">
          <span class="parameters-form__wrapper__name">Укажите требуемый опыт работы:</span>
          <div class="parameters-filter__block">
            <input v-model="experience" type="radio" name="exp" value="0" class="parameters-filter__input" id="exp-1"
                   checked>
            <label for="exp-1" class="parameters-filter-label radio">Не имеет значения</label>
          </div>
          <div class="parameters-filter__block">
            <input v-model="experience" type="radio" name="exp" value="1-3" class="parameters-filter__input" id="exp-2">
            <label for="exp-2" class="parameters-filter-label radio">от 1 года до 3 лет</label>
          </div>
          <div class="parameters-filter__block">
            <input v-model="experience" type="radio" name="exp" value="3-6" class="parameters-filter__input" id="exp-3">
            <label for="exp-3" class="parameters-filter-label radio">От 3 до 6 лет</label>
          </div>
          <div class="parameters-filter__block">
            <input v-model="experience" type="radio" name="exp" value="noExp" class="parameters-filter__input"
                   id="exp-4">
            <label for="exp-4" class="parameters-filter-label radio">Нет опыта</label>
          </div>
          <div class="parameters-filter__block">
            <input v-model="experience" type="radio" name="exp" value="<6" class="parameters-filter__input" id="exp-5">
            <label for="exp-5" class="parameters-filter-label radio">Более 6 лет</label>
          </div>
        </div>
        <div class="parameters-form__wrapper">
          <p class="parameters-form__wrapper__name">График работы</p>
          <div class="parameters-filter__block employ">
            <input v-model="graph" type="checkbox" class="parameters-filter__input" id="graph-1" value="FullDay">
            <label for="graph-1" class="parameters-filter-label check">Полный день</label>
          </div>
          <div class="parameters-filter__block employ">
            <input v-model="graph" type="checkbox" class="parameters-filter__input" id="graph-2" value="distantWork">
            <label for="graph-2" class="parameters-filter-label check">Удаленная работа</label>
          </div>
          <div class="parameters-filter__block employ">
            <input v-model="graph" type="checkbox" class="parameters-filter__input" id="graph-3" value="ShiftSchedule">
            <label for="graph-3" class="parameters-filter-label check">Сменный график</label>
          </div>
          <div class="parameters-filter__block employ">
            <input v-model="graph" type="checkbox" class="parameters-filter__input" id="graph-4" value="FlexibleSchedule">
            <label for="graph-4" class="parameters-filter-label check">Гибкий график</label>
          </div>
          <div class="parameters-filter__block employ">
            <input v-model="graph" type="checkbox" class="parameters-filter__input" id="graph-5" value="ShiftMethod">
            <label for="graph-5" class="parameters-filter-label check">Вахтовый метод</label>
          </div>
        </div>
        <ckeditor :config="editorConfig" v-model="editorData" class="ckeditor-text"></ckeditor>
        <div class="constructor-contact">
        </div>
        <button
            @click="create_vacancy"
            class="button-orange-another parameters-submit"
        >Опубликовать
        </button>
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
      editorData: '',
      nameVacancy: '',
      levelSalMin: null,
      levelSalMax: null,
      isSalaryTask: "beforeTax",
      employ: 'fullEmploy',
      experience: '0',
      graph: [],

      companyName: '',
      companyTel: '',
      companyEmail: '',
      companyPost: '',
      companyPerson: '',

    }
  },
  methods: {
    create_vacancy() {
      const vacancy = {
        vacancy_title: this.nameVacancy,
        salary_min: this.levelSalMin,
        salary_max: this.levelSalMax,
        employ: this.employ,
        experience: this.experience,
        vacancyDescription: this.editorData,
        companyName: this.companyName,
        companyTel: this.companyTel,
        companyEmail: this.companyEmail,
        companyPost: this.companyPost,
        companyPerson: this.companyPerson,
      };
      axios.post('api/v1/create/', vacancy)
          .then(response => {
            console.log(response)
          })
          .catch(error => {
            console.log(error)
          });
    },
    handlerGraph() {

    }
  },
}
</script>
<style src="@/style/create.scss" lang="scss" scoped>

</style>