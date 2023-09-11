<template>
  <section class="constructor">
    <div class="wrapper">
      <form class="upload-image">
        <!--                <p class="upload-image-title">Загрузите тизер</p>-->
        <div class="upload-image__wrapper">
          <p class="upload-image-title">Загрузите тизер</p>
          <input type="file" name="image" class="upload-image-input">
          <div class="upload-image__cross"></div>
        </div>
        <!--                <input type="file" name="image" class="upload-image-input">-->
        <!--                <div class="upload-image__cross"></div>-->
      </form>
      <form class="parameters-form">
        <h2 class="constructor-title">Создание вакансии</h2>
        <div class="parameters-form__wrapper">
          <span class="parameters-form__wrapper__name">Напишите название вакансии:</span>
          <input v-model="nameVacancy" type="text" class="parameters-form__wrapper__text"
                 placeholder="ООО “Маршмеллоу”">
        </div>
        <div class="parameters-form__wrapper">
          <span class="parameters-form__wrapper__name">Уровень заработной платы:</span>
          <input v-model="levelSal" type="text" class="parameters-form__wrapper__text price margin-bottom"
                 placeholder="От">
          <input v-model="levelSalMar" type="text" class="parameters-form__wrapper__text price margin-bottom"
                 placeholder="До">
          <div class="radio-wrapper">
            <input v-model="salaryTax" type="radio" name="salary" value="beforeTax" class="parameters-filter__input"
                   id="beforeDed" checked>
            <label for="beforeDed" class="parameters-filter-label radio">До вычета налогов</label>
          </div>
          <div class="radio-wrapper">
            <input v-model="salaryTax_0" type="radio" name="salary" value="afterTax" class="parameters-filter__input"
                   id="afterDed">
            <label for="afterDed" class="parameters-filter-label radio">На руки</label>
          </div>
        </div>
        <div class="parameters-form__wrapper">
          <span class="parameters-form__wrapper__name">Укажите тип занятости:</span>
          <div class="radio-wrapper">
            <input v-model="employ" type="radio" name="employ" value="fullEmploy" class="parameters-filter__input"
                   id="fullEmploy" checked>
            <label for="fullEmploy" class="parameters-filter-label radio">Полная занятость</label>
          </div>
          <div class="radio-wrapper">
            <input v-model="employ" type="radio" name="employ" value="partialEmploy" class="parameters-filter__input"
                   id="partialEmploy">
            <label for="partialEmploy" class="parameters-filter-label radio">Частичная занятость</label>
          </div>
          <div class="radio-wrapper">
            <input v-model="employ" type="radio" name="employ" value="internship" class="parameters-filter__input"
                   id="internship">
            <label for="internship" class="parameters-filter-label radio">Стажировка</label>
          </div>
          <div class="radio-wrapper">
            <input v-model="employ" type="radio" name="employ" value="projectWork" class="parameters-filter__input"
                   id="projectWork">
            <label for="projectWork" class="parameters-filter-label radio">Проектная работа</label>
          </div>
          <div class="radio-wrapper">
            <input v-model="employ" type="radio" name="employ" value="volunteering" class="parameters-filter__input"
                   id="volunteering">
            <label for="volunteering" class="parameters-filter-label radio">Волонтерство</label>
          </div>
        </div>
        <div class="parameters-form__wrapper">
          <span class="parameters-form__wrapper__name">Укажите требуемый опыт работы:</span>
          <div class="radio-wrapper">
            <input v-model="experience" type="radio" name="exp" value="0" class="parameters-filter__input" id="exp-1"
                   checked>
            <label for="exp-1" class="parameters-filter-label radio">Не имеет значения</label>
          </div>
          <div class="radio-wrapper">
            <input v-model="experience" type="radio" name="exp" value="1-3" class="parameters-filter__input" id="exp-2">
            <label for="exp-2" class="parameters-filter-label radio">от 1 года до 3 лет</label>
          </div>
          <div class="radio-wrapper">
            <input v-model="experience" type="radio" name="exp" value="3-6" class="parameters-filter__input" id="exp-3">
            <label for="exp-3" class="parameters-filter-label radio">От 3 до 6 лет</label>
          </div>
          <div class="radio-wrapper">
            <input v-model="experience" type="radio" name="exp" value="noExp" class="parameters-filter__input"
                   id="exp-4">
            <label for="exp-4" class="parameters-filter-label radio">Нет опыта</label>
          </div>
          <div class="radio-wrapper">
            <input v-model="experience" type="radio" name="exp" value="<6" class="parameters-filter__input" id="exp-5">
            <label for="exp-5" class="parameters-filter-label radio">Более 6 лет</label>
          </div>
        </div>
        <!--            <div class="parameters-form__wrapper">-->
        <!--                <span class="parameters-form__wrapper__name">Расскажите про вакансию:</span>-->
        <!--                <span>Заголовок для раздела:</span>-->
        <!--              <input type="text" class="parameters-form__wrapper__text margin-bottom" placeholder="Заголовок">-->
        <!--              <textarea class=""></textarea>-->
        <!--            </div>-->
        <ckeditor :config="editorConfig" v-model="editorData" class="ckeditor-text"></ckeditor>
        <button class="button-orange-another parameters-submit">Опубликовать</button>
        <!--        <span class="supernova-wrapper__name" :src="vacancys">{{ vacancys }}</span>-->
      </form>
    </div>
  </section>
</template>
<script>

import axios from "axios";

export default {
  data() {
    return {
      editorConfig: {
        toolbar: [['Bold'], ['Italic'], ['Underline'], ['Strike'], ['NumberedList'], ['BulletedList'], ['Styles'], ['Format']],
      },
      editorData: '',
      tiser: null,
      nameVacancy: '',
      levelSal: null,
      levelSalMar: null,
      salaryTax: 'beforeTax',
      salaryTax_0: 'afterTax',
      employ: 'fullEmploy',
      experience: '0',
      vacancys: '',
    }
  },
  mounted() {
    this.getVacancys();
  },
  methods: {
    create_vacancy() {
      const vacancy = {
        vacancy_title: this.nameVacancy,
        poster: this.tiser,
        salary_min: this.salaryTax,
        salary_max: this.salaryTax_0,
      };
      axios.post('', vacancy)
          .then(response => {
            console.log(response)
          })
          .catch(error => {
            console.log(error)
          });
    },
  },
}
</script>
<style src="@/style/create.scss" lang="scss" scoped>

</style>