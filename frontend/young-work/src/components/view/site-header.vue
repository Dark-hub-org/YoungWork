<template>
  <header class="header">
    <div class="wrapper wrapper-header">
      <a href="#" class="header-logo-link">
        <img src="@/assets/logo.svg" alt="логотип" class="header-logo">
      </a>
      <nav :class="{active: isMenuActive}" class="header-nav">
        <ul class="header-nav__list">
          <li class="header-nav__list-item">
            <button type="button" class="header-btn button-orange">Услуги</button>
          </li>
          <li class="header-nav__list-item">
            <button type="button" class="header-btn button-orange">Работа</button>
          </li>
          <li class="header-nav__list-item">
            <button
                @click="isModalWinLog = true"
                type="button"
                class="header-btn button-green">
              Вход</button>
          </li>
          <li class="header-nav__list-item">
            <button
                @click="isModalWinReg = true"
                type="button"
                class="header-btn button-green">
              Регистрация</button>
          </li>
        </ul>
      </nav>
      <modal-window
        :show="isModalWinReg">
        <div class="modal-reg-wrapper">
          <p class="modal-title">Регистрация</p>
          <form action="#" class="modal-form">
            <div class="modal-form-block">
              <label class="modal-form-name">Имя</label>
              <input type="text" class="modal-form__input">
            </div>
            <div class="modal-form-block">
              <label class="modal-form-name">Электронная почта</label>
              <input type="text" class="modal-form__input">
            </div>
            <div class="modal-form-block">
              <label class="modal-form-name">Придумайте пароль (минимум 6 символов)</label>
              <input type="text" class="modal-form__input">
            </div>
            <button class="modal-form__submit button-orange-another">Зарегистрироваться</button>
            <button
                @click="isModalWinLog = true"
                class="modal-form-login">
              Войти</button>
          </form>
        </div>
      </modal-window>
      <modal-window
        :show="isModalWinLog">
        <div class="modal-reg-wrapper">
          <p class="modal-title modal-title-reg">Войти</p>
          <form action="#" class="modal-form modal-form-log">
            <div class="modal-form-block">
              <label class="modal-form-name">электронная почта</label>
              <input type="text" class="modal-form__input">
            </div>
            <div class="modal-form-block">
              <label class="modal-form-name">Пароль</label>
              <input type="text" class="modal-form__input">
            </div>
            <button
                @click="isModalWinResetPass = true"
                class="modal-form-password">
              Забыли пароль?</button>
            <button class="modal-form__submit button-orange-another">Войти</button>
            <button class="modal-form-login">Зарегистрироваться</button>
          </form>
        </div>
      </modal-window>
       <modal-window
       :show="isModalWinResetPass">
        <div class="modal-reg-wrapper">
          <p class="modal-title modal-title-reg">Восстановление пароля</p>
          <form action="#" class="modal-form modal-form-reset">
            <div class="modal-form-block">
              <label class="modal-form-name">Укажите E-mail, который вы использовали при регистрации</label>
              <input type="text" class="modal-form__input">
            </div>
            <button class="modal-form__submit button-orange-another">Далее</button>
          </form>
        </div>
       </modal-window>
      <button @click="openItem" class="menu-btn">
        <span class="menu-btn__line"></span>
        <span class="menu-btn__line"></span>
        <span class="menu-btn__line"></span>
      </button>
    </div>
  </header>
</template>

<script>
import ModalWindow from "@/components/ui/modalWin.vue";

export default {
  name: 'site-header',
  components: {
    ModalWindow
  },
  data() {
    return {
      isModalWinReg: false,
      isModalWinLog: false,
      isModalWinResetPass: false,
      isMenuActive: false,
    }
  },
  methods: {
    openItem() {
      this.isMenuActive = !this.isMenuActive;
        document.documentElement.style.overflow = 'hidden';
    },
  },
  watch: {
    isMenuActive: function() {
      if(this.isMenuActive){
        document.documentElement.style.overflow = 'hidden'
        return
      }
      document.documentElement.style.overflow = 'auto'
    }
  }
}
</script>

<style lang="scss">
@import "../../style/header";
@import "../../style/main";
</style>
