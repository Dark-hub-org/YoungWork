<template>
  <section class="create-resume">
    <div class="create-resume-wrapper">
      <h1 class="create-resume__title">Создание резюме</h1>
      <form class="create-resume__form">
        <div class="create-resume-block__wrapper">
          <span class="create-resume-block__title">Напишите, кем хотите работать:</span>
          <input
              v-restrict-input-length="120"
              type="text"
              class="create-resume__input-text"
              placeholder="Разработчик java"
              v-model.trim="resumeName">
        </div>
        <div class="create-resume__wrapper">
          <p class="create-resume__name-filter">Тип занятости</p>
          <div class="create-resume__block employ">
            <input type="checkbox" value="fullEmploy" class="create-resume__input" id="employ-1" v-model="resumeEmploy">
            <label for="employ-1" class="create-resume-filter-label check">Полная занятость</label>
          </div>
          <div class="create-resume__block employ">
            <input type="checkbox" value="partialEmploy" class="create-resume__input" id="employ-2" v-model="resumeEmploy">
            <label for="employ-2" class="create-resume-filter-label check">Частичная занятость</label>
          </div>
          <div class="create-resume__block employ">
            <input type="checkbox" value="internship" class="create-resume__input" id="employ-3" v-model="resumeEmploy">
            <label for="employ-3" class="create-resume-filter-label check">Стажировка</label>
          </div>
          <div class="create-resume__block employ">
            <input type="checkbox" value="projectWork" class="create-resume__input" id="employ-4" v-model="resumeEmploy">
            <label for="employ-4" class="create-resume-filter-label check">Проектная работа</label>
          </div>
          <div class="create-resume__block employ">
            <input type="checkbox" value="volunteering" class="create-resume__input" id="employ-5" v-model="resumeEmploy">
            <label for="employ-5" class="create-resume-filter-label check">Волонтерство</label>
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
              <span class="create-resume__tag-text">{{item}}</span>
              <button type="button" class="create-resume__tag-btn" @click="deleteSkill(item)"></button>
            </div>
          </div>
        </div>
        <div class="create-resume-block__wrapper">
          <h3 class="create-resume-block__title">Ваши  качества:</h3>
          <input
              v-restrict-input-length="120"
              type="text"
              class="create-resume__input-text"
              placeholder="Перечислите ваши навыки"
              v-model.trim="resumeQuality"
              @keyup.enter="addTagsQuality">
          <div class="create-resume__tags-wrapper">
            <div class="create-resume__tag" v-for="item in qualityTags" :key="item">
              <span class="create-resume__tag-text">{{item}}</span>
              <button type="button" class="create-resume__tag-btn" @click="deleteQulity(item)"></button>
            </div>
          </div>
        </div>
        <div class="create-resume-block__wrapper">
          <h3 class="create-resume-block__title">О вас:</h3>
          <textarea
              class="create-resume-about"
              placeholder="Расскажите, где работали, какие у вас качества, которые могли бы заинтересовать работодателя "
              v-model="resumeAbout"></textarea>
        </div>
        <div class="create-resume__wrapper">
          <p class="create-resume__name-filter">Укажите опыт работы:</p>
          <div class="create-resume__block">
            <input v-model="resumeExperience" type="radio" name="exp" value="0" class="create-resume__input" id="exp-1"
                   checked>
            <label for="exp-1" class="create-resume-filter-label radio">Не имеет значения</label>
          </div>
          <div class="create-resume__block">
            <input v-model="resumeExperience" type="radio" name="exp" value="1-3" class="create-resume__input" id="exp-2">
            <label for="exp-2" class="create-resume-filter-label radio">от 1 года до 3 лет</label>
          </div>
          <div class="create-resume__block">
            <input v-model="resumeExperience" type="radio" name="exp" value="3-6" class="create-resume__input" id="exp-3">
            <label for="exp-3" class="create-resume-filter-label radio">От 3 до 6 лет</label>
          </div>
          <div class="create-resume__block">
            <input v-model="resumeExperience" type="radio" name="exp" value="noExp" class="create-resume__input"
                   id="exp-4">
            <label for="exp-4" class="create-resume-filter-label radio">Нет опыта</label>
          </div>
          <div class="create-resume__block">
            <input v-model="resumeExperience" type="radio" name="exp" value="<6" class="create-resume__input" id="exp-5">
            <label for="exp-5" class="create-resume-filter-label radio">Более 6 лет</label>
          </div>
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
                class="create-resume__input-text connect"/>
          </div>
          <div class="create-resume-block__wrapper connection">
            <img
                src="@/assets/email-icon.svg"
                alt="иконка e-mail"
                class="create-resume__connection__img">
            <input v-model.trim="resumeEmail" type="text" class="create-resume__input-text connect" placeholder="Адрес эл.почты">
          </div>
          <div class="create-resume-block__wrapper connection">
            <img
                src="@/assets/telegram-icon.svg"
                alt="иконка телеграмма"
                class="create-resume__connection__img">
            <input v-model.trim="resumeTelegram" type="text" class="create-resume__input-text connect" placeholder="Telegram">
          </div>
          <div class="create-resume-block__wrapper connection">
            <img
                src="@/assets/link-icon.svg"
                alt="иконка ссылки"
                class="create-resume__connection__img">
            <input v-model.trim="resumeSite" type="text" class="create-resume__input-text connect" placeholder="Личный сайт">
          </div>
        </div>
<!--        <div class="create-resume-block__wrapper">-->
<!--          <p class="create-resume-block__title">Добавьте фото:</p>-->
<!--          <div class="upload-image">-->
<!--            <div class="upload-image__wrapper">-->
<!--              <input type="file" name="image" class="upload-image-input">-->
<!--              <div class="upload-image__cross"></div>-->
<!--            </div>-->
<!--          </div>-->
<!--          <p class="upload-image__description">Рекомендуемый размер 80х80</p>-->
<!--        </div>-->
        <button type="button" class="create-resume__submit">Опубликовать</button>
      </form>
    </div>
  </section>
</template>

<script>
import Vue from "vue";
import VueTheMask from 'vue-the-mask';
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
      resumeEmploy: [],
      resumeSkill: '',
      skillsTags: [],
      resumeQuality: '',
      qualityTags: [],
      resumeAbout: '',
      resumeExperience: '0',
      resumePhoneNumber: '',
      resumeEmail: '',
      resumeTelegram: '',
      resumeSite: '',
    }
  },
  methods: {
    addTagsSkills() {
      if(this.resumeSkill === '') {
        return
      }
      else if(this.skillsTags.includes(this.resumeSkill.toLowerCase())){
        return
      }
      else {
        this.skillsTags.push(this.resumeSkill.toLowerCase())
        this.resumeSkill = '';
      }
    },
    deleteSkill(skill) {
      this.skillsTags = this.skillsTags.filter((item) => item !== skill)
    },
    addTagsQuality() {
      if(this.resumeQuality === '') {
        return
      }
      else if(this.qualityTags.includes(this.resumeQuality.toLowerCase())){
        return
      }
      else {
        this.qualityTags.push(this.resumeQuality.toLowerCase())
        this.resumeQuality = '';
      }
    },
    deleteQulity(skill) {
      this.qualityTags = this.skillsTags.filter((item) => item !== skill)
    },
  },
  computed: {
  }
}
</script>

<style src="@/style/create-resume.scss" lang="scss" scoped>

</style>