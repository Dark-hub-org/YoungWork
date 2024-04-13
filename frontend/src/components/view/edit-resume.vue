<template>
  <section class="create-resume">
    <div class="wrapper">
      <h1 class="create-resume__title">Редактировать резюме</h1>
      <form class="create-resume__form">
        <div class="create-resume__section">
          <span class="create-resume__section-title">Напишите, кем хотите работать:</span>
          <input
              v-restrict-input-length="120"
              type="text"
              class="create-resume__section-input"
              :class="{error: errorFields.isErrorName}"
              placeholder="Разработчик java"
              v-model.trim="resumeData.resume_title"
              @focus="errorFields.isErrorName = false">
          <p v-if="errorFields.isErrorName" class="create-resume__error">
            Пожалуйста, заполните поле
          </p>
        </div>
        <div class="create-resume__section">
          <span class="create-resume__section-title">Напишите, желанный доход:</span>
          <input
              v-restrict-input-length="120"
              type="number"
              class="create-resume__section-input"
              v-model.number="resumeData.salary"
          >
        </div>
        <div class="create-resume__wrapper">
          <p class="create-resume__wrapper-title">Тип занятости</p>
          <div class="create-resume__block employ">
            <input
                type="checkbox"
                value="Полная занятость"
                class="create-resume__input"
                id="employ-1"
                v-model="resumeData.employ"
                @change="errorFields.isErrorEmploy = false"
                checked>
            <label
                for="employ-1"
                class="create-resume__block-label check"
                :class="{'error': errorFields.isErrorEmploy}">Полная занятость</label>
          </div>
          <div class="create-resume__block employ">
            <input
                type="checkbox"
                value="Частичная занятость"
                class="create-resume__input"
                id="employ-2"
                v-model="resumeData.employ"
                @change="errorFields.isErrorEmploy = false"
            >
            <label
                for="employ-2"
                class="create-resume__block-label check"
                :class="{'error': errorFields.isErrorEmploy}">Частичная занятость</label>
          </div>
          <div class="create-resume__block employ">
            <input
                type="checkbox"
                value="Стажировка"
                class="create-resume__input"
                id="employ-3"
                v-model="resumeData.employ"
                @change="errorFields.isErrorEmploy = false">
            <label
                for="employ-3"
                class="create-resume__block-label check"
                :class="{'error': errorFields.isErrorEmploy}">Стажировка</label>
          </div>
          <div class="create-resume__block employ">
            <input
                type="checkbox"
                value="Проектная работа"
                class="create-resume__input"
                id="employ-4"
                v-model="resumeData.employ"
                @change="errorFields.isErrorEmploy = false">
            <label
                for="employ-4"
                class="create-resume__block-label check"
                :class="{'error': errorFields.isErrorEmploy}">Проектная работа</label>
          </div>
          <div class="create-resume__block employ">
            <input
                type="checkbox"
                value="Волонтерство"
                class="create-resume__input"
                id="employ-5"
                v-model="resumeData.employ"
                @change="errorFields.isErrorEmploy = false">
            <label
                for="employ-5"
                class="create-resume__block-label check"
                :class="{'error': errorFields.isErrorEmploy}">Волонтерство</label>
          </div>
          <p v-if="errorFields.isErrorEmploy" class="create-resume__error">
            Пожалуйста, заполните поле
          </p>
        </div>
        <div class="create-resume__wrapper">
          <p class="create-resume__wrapper-title">Укажите опыт работы:</p>
          <div class="create-resume__block">
            <input v-model="resumeData.experience" type="radio" name="exp" value="Нет опыта" class="create-resume__input"
                   id="exp-4" checked>
            <label for="exp-4" class="create-resume__block-label radio">Нет опыта</label>
          </div>
          <div class="create-resume__block">
            <input v-model="resumeData.experience" type="radio" name="exp" value="От 1 года до 3 лет"
                   class="create-resume__input"
                   id="exp-2">
            <label for="exp-2" class="create-resume__block-label radio">От 1 года до 3 лет</label>
          </div>
          <div class="create-resume__block">
            <input v-model="resumeData.experience" type="radio" name="exp" value="От 3 до 6 лет" class="create-resume__input"
                   id="exp-3">
            <label for="exp-3" class="create-resume__block-label radio">От 3 до 6 лет</label>
          </div>
          <div class="create-resume__block">
            <input v-model="resumeData.experience" type="radio" name="exp" value="Более 6 лет"
                   class="create-resume__input"
                   id="exp-4">
            <label for="exp-4" class="create-resume__block-label radio">Более 6 лет</label>
          </div>
        </div>
        <div class="create-resume__section">
          <h3 class="create-resume__section-title">Ключевые навыки:</h3>
          <input
              v-restrict-input-length="120"
              type="text"
              class="create-resume__section-input"
              placeholder="Перечислите ваши навыки"
              v-model.trim="resumeSkill"
              @keyup.enter="addTagsSkills">
          <div class="create-resume__tags">
            <div class="create-resume__tag" v-for="item in resumeData.skills" :key="item">
              <span class="create-resume__tag-text">{{ item }}</span>
              <button
                  type="button"
                  class="create-resume__tag-btn"
                  @click="deleteSkill(item)"></button>
            </div>
          </div>
        </div>
        <div class="create-resume__section">
          <h3 class="create-resume__section-title">Ваши качества:</h3>
          <input
              v-restrict-input-length="120"
              type="text"
              class="create-resume__section-input"
              placeholder="Перечислите ваши навыки"
              v-model.trim="resumeQuality"
              @keyup.enter="addTagsQuality">
          <div class="create-resume__tags">
            <div class="create-resume__tag" v-for="item in resumeData.quality" :key="item">
              <span class="create-resume__tag-text">{{ item }}</span>
              <button type="button" class="create-resume__tag-btn" @click="deleteQuality(item)"></button>
            </div>
          </div>
        </div>
        <div class="create-resume__section">
          <h3 class="create-resume__section-title">О вас:</h3>
          <ckeditor
              :config="editorConfig"
              v-model="resumeData.about_us"
              class="ckeditor-text">
          </ckeditor>
<!--          <p v-if="isErrorAbout" class="create-resume__error">-->
<!--            Пожалуйста, заполните поле-->
<!--          </p>-->
        </div>
        <div class="create-resume__bottom">
          <button @click="submitForm(resumeData.id)" type="button" class="button-orange-another">Сохранить</button>
          <button @click="deleteResume(resumeData.id)" type="button" class="button-orange">Удалить</button>
        </div>
      </form>
    </div>
  </section>
</template>

<script>
import Vue from "vue";
import VueTheMask from 'vue-the-mask';
import axios from "axios";

Vue.use(VueTheMask);

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
  name: 'create-resume',
  data() {
    return {
      resumeData: {},
      errorFields: {
        isErrorName: false,
        isErrorEmploy: false,
      },
      resumeSkill: '',
      resumeQuality: '',
      editorConfig: {
        toolbar: [['Bold'], ['Italic'], ['Underline'], ['Strike'], ['NumberedList'], ['BulletedList'], ['Styles'], ['Format']],
      },
    }
  },
  methods: {
    async getResumeData(id) {
      try {
        const response = await axios.get(`/api/res/${id}`)
        this.resumeData = response.data
      } catch (error) {
        console.log(error)
      }
    },
    async submitForm(id) {
      try {
        if(this.validationDataResume()) {
          await axios.patch(`/api/edit-resume/${id}/`, this.resumeData)
          location.reload()
        } else {
          this.validationDataResume()
        }
      } catch(error) {
        console.log(error)
      }
    },
    async deleteResume(id) {
      try {
        await axios.delete(`/api/resume/delete/${id}/`)
        this.$router.push({name: 'applicant', params: {id: this.userId}})
      } catch (error) {
        console.log(error)
      }
    },
    validationDataResume() {
      this.errorFields.isErrorName = this.validateField(this.resumeData.resume_title)
      this.errorFields.isErrorEmploy = this.validateField(this.resumeData.employ)
      return Object.values(this.errorFields).every((error) => !error)
    },
    validateField(value) {
      return value.length === 0;
    },
    addTagsSkills() {
      if(this.resumeSkill.length && !this.resumeData.skills.includes(this.resumeSkill.toLowerCase())) {
        this.resumeData.skills.push(this.resumeSkill.toLowerCase())
        this.resumeSkill = '';
      }
    },
    deleteSkill(skill) {
      this.resumeData.skills = this.resumeData.skills.filter((item) => item !== skill)
    },
    addTagsQuality() {
      if(this.resumeQuality.length && !this.resumeData.quality.includes(this.resumeQuality.toLowerCase())) {
        this.resumeData.quality.push(this.resumeQuality.toLowerCase())
        this.resumeQuality = '';
      }
    },
    deleteQuality(skill) {
      this.resumeData.quality = this.resumeData.quality.filter((item) => item !== skill)
    },
  },
  computed: {
    userId() {
      return this.$store.state.userData.id
    }
  },
  mounted() {
    this.getResumeData(this.$route.params.id)
  }
}
</script>

<style src="@/style/create-resume.scss" lang="scss" scoped>

</style>