<template>
  <section class="create-resume">
    <div class="wrapper create-resume-wrapper">
      <h1 class="create-resume__title">Создание резюме</h1>
      <form class="create-resume__form">
        <div class="create-resume-block__wrapper">
          <span class="create-resume-block__title">Напишите, кем хотите работать:</span>
          <input
              v-restrict-input-length="120"
              type="text"
              class="create-resume__input-text"
              :class="{error: isErrorName}"
              placeholder="Разработчик java"
              v-model.trim="resumeName"
              @focus="isErrorName = false">
          <p v-if="isErrorName" class="create-resume__error">
            Пожалуйста, заполните поле
          </p>
        </div>
        <div class="create-resume__wrapper">
          <p class="create-resume__name-filter">Тип занятости</p>
          <div class="create-resume__block employ">
            <input
                type="checkbox"
                value="Полная занятость"
                class="create-resume__input"
                id="employ-1"
                v-model="resumeEmploy"
                @change="isErrorEmploy = false"
                checked>
            <label
                for="employ-1"
                class="create-resume-filter-label check"
                :class="{'error': isErrorEmploy}">Полная занятость</label>
          </div>
          <div class="create-resume__block employ">
            <input
                type="checkbox"
                value="Частичная занятость"
                class="create-resume__input"
                id="employ-2"
                v-model="resumeEmploy"
                @change="isErrorEmploy = false"
            >
            <label
                for="employ-2"
                class="create-resume-filter-label check"
                :class="{'error': isErrorEmploy}">Частичная занятость</label>
          </div>
          <div class="create-resume__block employ">
            <input
                type="checkbox"
                value="Стажировка"
                class="create-resume__input"
                id="employ-3"
                v-model="resumeEmploy"
                @change="isErrorEmploy = false">
            <label
                for="employ-3"
                class="create-resume-filter-label check"
                :class="{'error': isErrorEmploy}">Стажировка</label>
          </div>
          <div class="create-resume__block employ">
            <input
                type="checkbox"
                value="Проектная работа"
                class="create-resume__input"
                id="employ-4"
                v-model="resumeEmploy"
                @change="isErrorEmploy = false">
            <label
                for="employ-4"
                class="create-resume-filter-label check"
                :class="{'error': isErrorEmploy}">Проектная работа</label>
          </div>
          <div class="create-resume__block employ">
            <input
                type="checkbox"
                value="Волонтерство"
                class="create-resume__input"
                id="employ-5"
                v-model="resumeEmploy"
                @change="isErrorEmploy = false">
            <label
                for="employ-5"
                class="create-resume-filter-label check"
                :class="{'error': isErrorEmploy}">Волонтерство</label>
          </div>
          <p v-if="isErrorEmploy" class="create-resume__error">
            Пожалуйста, заполните поле
          </p>
        </div>
        <div class="create-resume__wrapper">
          <p class="create-resume__name-filter">Укажите опыт работы:</p>
          <div class="create-resume__block">
            <input v-model="resumeExperience" type="radio" name="exp" value="Нет опыта" class="create-resume__input"
                   id="exp-4" checked>
            <label for="exp-4" class="create-resume-filter-label radio">Нет опыта</label>
          </div>
          <div class="create-resume__block">
            <input v-model="resumeExperience" type="radio" name="exp" value="От 1 года до 3 лет" class="create-resume__input"
                   id="exp-2">
            <label for="exp-2" class="create-resume-filter-label radio">От 1 года до 3 лет</label>
          </div>
          <div class="create-resume__block">
            <input v-model="resumeExperience" type="radio" name="exp" value="От 3 до 6 лет" class="create-resume__input"
                   id="exp-3">
            <label for="exp-3" class="create-resume-filter-label radio">От 3 до 6 лет</label>
          </div>
        </div>
        <div class="create-resume-block__wrapper">
          <h3 class="create-resume-block__title">Ключевые навыки:</h3>
          <input
              v-restrict-input-length="120"
              type="text"
              class="create-resume__input-text"
              placeholder="Перечислите ваши навыки"
              v-model.trim="resumeSkill"
              @keyup.enter="addTagsSkills">
          <div class="create-resume__tags-wrapper">
            <div class="create-resume__tag" v-for="item in skillsTags" :key="item">
              <span class="create-resume__tag-text">{{ item }}</span>
              <button
                  type="button"
                  class="create-resume__tag-btn"
                  @click="deleteSkill(item)"></button>
            </div>
          </div>
        </div>
        <div class="create-resume-block__wrapper">
          <h3 class="create-resume-block__title">Ваши качества:</h3>
          <input
              v-restrict-input-length="120"
              type="text"
              class="create-resume__input-text"
              placeholder="Перечислите ваши навыки"
              v-model.trim="resumeQuality"
              @keyup.enter="addTagsQuality">
          <div class="create-resume__tags-wrapper">
            <div class="create-resume__tag" v-for="item in qualityTags" :key="item">
              <span class="create-resume__tag-text">{{ item }}</span>
              <button type="button" class="create-resume__tag-btn" @click="deleteQuality(item)"></button>
            </div>
          </div>
        </div>
        <div class="create-resume-block__wrapper">
          <h3 class="create-resume-block__title">О вас:</h3>
          <ckeditor
              :config="editorConfig"
              v-model="resumeAbout"
              class="ckeditor-text">
          </ckeditor>
          <p v-if="isErrorAbout" class="create-resume__error">
            Пожалуйста, заполните поле
          </p>
        </div>
        <div class="create-resume-block__wrapper">
          <h3 class="create-resume-block__title">Как с вами можно связаться:</h3>
          <div class="create-resume-block__wrapper connection">
            <img
                src="@/assets/phone-icon.svg"
                alt="иконка телефона"
                class="create-resume__connection__img">
            <input
                v-mask="'+7 (###) ### ##-##'"
                v-model="resumePhoneNumber"
                placeholder="Номер телефона"
                class="create-resume__input-text connect"
                :class="{'error': isErrorContact}"
                @focus="isErrorContact = false"/>
          </div>
          <div class="create-resume-block__wrapper connection">
            <img
                src="@/assets/email-icon.svg"
                alt="иконка e-mail"
                class="create-resume__connection__img">
            <input
                v-model.trim="resumeEmail"
                type="text"
                class="create-resume__input-text connect"
                :class="{'error': isErrorContact}"
                placeholder="Адрес эл.почты"
                @focus="isErrorContact = false">
          </div>
          <div class="create-resume-block__wrapper connection">
            <img
                src="@/assets/telegram-icon.svg"
                alt="иконка телеграмма"
                class="create-resume__connection__img">
            <input
                v-model.trim="resumeTelegram"
                type="text"
                class="create-resume__input-text connect"
                :class="{'error': isErrorContact}"
                placeholder="Telegram"
                @focus="isErrorContact = false">
          </div>
          <div class="create-resume-block__wrapper connection">
            <img
                src="@/assets/link-icon.svg"
                alt="иконка ссылки"
                class="create-resume__connection__img">
            <input
                v-model.trim="resumeSite"
                type="text"
                class="create-resume__input-text connect"
                :class="{'error': isErrorContact}"
                placeholder="Личный сайт"
                @focus="isErrorContact = false">
          </div>
          <p v-if="isErrorContact" class="create-resume__error">Пожалуйста, заполните поле</p>
        </div>
        <button @click.prevent="submitForm" type="button" class="create-resume__submit">Опубликовать</button>
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
      resumeName: '',
      isErrorName: false,

      resumeEmploy: ['fullEmploy'],
      isErrorEmploy: false,

      resumeGraph: [],

      resumeSkill: '',
      skillsTags: [],
      isErrorSkills: false,

      resumeQuality: '',
      qualityTags: [],
      isErrorQuality: false,

      editorConfig: {
        toolbar: [['Bold'], ['Italic'], ['Underline'], ['Strike'], ['NumberedList'], ['BulletedList'], ['Styles'], ['Format']],
      },
      resumeAbout: '',
      isErrorAbout: false,

      resumeExperience: 'noExp',
      resumePhoneNumber: '',
      resumeEmail: '',
      resumeTelegram: '',
      resumeSite: '',
      isErrorContact: false,
      type: '',
    }
  },
  methods: {
    submitForm() {
      if (this.resumeName === '') {
        this.isErrorName = true;
      }
      if (this.resumeEmploy.length === 0) {
        this.isErrorEmploy = true
      }
      if (this.resumePhoneNumber.length === 0 && this.resumeEmail.length === 0 && this.resumeTelegram.length === 0 && this.resumeSite.length === 0) {
        this.isErrorContact = true
      }
      const resume = {
        summary_title: this.resumeName,
        type: this.type,
        skill: this.resumeSkill,
        quality: this.resumeQuality,
        experience: this.resumeExperience,
        about_us: this.resumeAbout,
        phone_number: this.resumePhoneNumber,
        email: this.resumeEmail,
        tm: this.resumeTelegram,
        website: this.resumeSite,
      };
      axios.post('', resume)
          .then(response => {
            console.log(response)
            window.location.reload();
          })
          .catch(error => {
            console.log(error)
          });
    },
    addTagsSkills() {
      if (this.resumeSkill === '') {
        return
      } else if (this.skillsTags.includes(this.resumeSkill.toLowerCase())) {
        return
      } else {
        this.skillsTags.push(this.resumeSkill.toLowerCase())
        this.resumeSkill = '';
      }
    },
    deleteSkill(skill) {
      this.skillsTags = this.skillsTags.filter((item) => item !== skill)
    },
    addTagsQuality() {
      if (this.resumeQuality === '') {
        return
      } else if (this.qualityTags.includes(this.resumeQuality.toLowerCase())) {
        return
      } else {
        this.qualityTags.push(this.resumeQuality.toLowerCase())
        this.resumeQuality = '';
      }
    },
    deleteQuality(skill) {
      this.qualityTags = this.skillsTags.filter((item) => item !== skill)
    },
  },
  computed: {},
  watch: {}
}
</script>

<style src="@/style/create-resume.scss" lang="scss" scoped>

</style>