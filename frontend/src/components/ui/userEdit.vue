<template>
  <div class="profile-edit">
    <h2 class="profile-edit__title">Личные данные</h2>
    <div class="profile-edit__block">
      <div class="profile-edit__field">
        <p class="profile-edit__field__name">Фамилия:</p>
        <input type="text" class="profile-edit__data">
      </div>
      <div class="profile-edit__field">
        <p class="profile-edit__field__name">Имя:</p>
        <input type="text" class="profile-edit__data">
      </div>
      <div class="profile-edit__field">
        <p class="profile-edit__field__name">Отчество:</p>
        <input type="text" class="profile-edit__data">
      </div>
    </div>
    <div class="profile-edit__block">
      <div class="profile-edit__field">
        <p class="profile-edit__field__name">Дата рождения:</p>
        <input placeholder="00/00/0000" type="text" class="profile-edit__data" v-mask="'##/##/####'">
      </div>
    </div>
    <div class="profile-edit__block">
      <div class="profile-edit__field">
        <p class="profile-edit__field__name">Гражданство:</p>
        <input type="text" class="profile-edit__data">
      </div>
    </div>
    <div class="profile-edit__block">
      <div class="profile-edit__field">
        <p class="profile-edit__field__name">Регион:</p>
        <input type="text" class="profile-edit__data">
      </div>
      <div class="profile-edit__field">
        <p class="profile-edit__field__name">Город проживания:</p>
        <input type="text" class="profile-edit__data">
      </div>
    </div>
    <div class="profile-edit__block">
      <div class="profile-edit__field contact">
        <p class="profile-edit__field__name">Контакты:</p>
        <img
            src="@/assets/phone-icon.svg"
            alt="иконка телефона"
            class="profile-edit__connection__img">
        <input
            v-mask="'+7 (###) ### ##-##'"
            placeholder="Номер телефона"
            class="profile-edit__data contact"/>
      </div>
      <div class="profile-edit__field contact">
        <img
            src="@/assets/email-icon.svg"
            alt="иконка e-mail"
            class="profile-edit__connection__img">
        <input
            type="text"
            placeholder="Адрес эл.почты"
            class="profile-edit__data contact" >
      </div>
      <div class="profile-edit__field contact">
        <img
            src="@/assets/telegram-icon.svg"
            alt="иконка телеграмма"
            class="profile-edit__connection__img">
        <input
            type="text"
            placeholder="Telegram"
            class="profile-edit__data contact">
      </div>
      <div class="profile-edit__field contact">
        <img
            src="@/assets/link-icon.svg"
            alt="иконка ссылки"
            class="profile-edit__connection__img">
        <input
            type="text"
            class="profile-edit__data contact" placeholder="Личный сайт">
      </div>
    </div>
    <h2 class="profile-edit__title">О вас</h2>
    <div class="profile-edit__block about">
      <div class="profile-edit__field about">
        <p class="profile-edit__field__name">Название организации:</p>
        <textarea class="profile-edit__data about"></textarea>
      </div>
    </div>
    <div class="profile-edit__block about">
      <div class="profile-edit__field about">
        <p class="profile-edit__field__name">Краткое описание вашей деятельности:</p>
        <textarea class="profile-edit__data about" style="min-height: 170px"></textarea>
      </div>
    </div>
    <div class="profile-edit__block">
      <button class="profile-edit__save">Сохранить</button>
      <button class="profile-edit__cancel">Отменить разрешения</button>
    </div>
  </div>
</template>

<script>

import Vue from "vue";
import VueTheMask from "vue-the-mask";

Vue.use(VueTheMask);

export default {
  name: 'user-edit',
  props: {
    userData: {
      type: Object,
      required: true,
    }
  },
  data() {
    return {

    }
  },
  methods: {

  }
}
</script>

<style src="@/style/ui/userEdit.scss" lang="scss" scoped>

</style>