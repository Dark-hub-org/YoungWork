<template>
  <header class="header">
    <div class="wrapper wrapper-header">
      <a href="#" class="header-logo-link">
        <img src="@/assets/logo.svg" alt="логотип" class="header-logo">
      </a>
      <nav
          :class="{active: isMenuActive}"
          class="header-nav">
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
              Вход
            </button>
          </li>
          <li class="header-nav__list-item">
            <button
                @click="isModalWinReg = true"
                type="button"
                class="header-btn button-green">
              Регистрация
            </button>
          </li>
        </ul>
      </nav>

      <!--      Делай на примере этой модалки-->
      <modal-window

          @close="onCloseModalReg"
          :isVisible="isModalWinReg">

        <div class="modal-reg-wrapper">
          <p class="modal-title">Регистрация</p>
          <form action="#" class="modal-form">
            <div v-if="ModalWinRegCurrentStep === 0">
              <div class="modal-form-block">
                <label class="modal-form-name">Имя</label>
                <input
                    v-model="name"
                    @input="isEmptyName = false"
                    type="text"
                    class="modal-form__input">
                  <label
                      v-if="isEmptyName"
                      class="modal-input-error">
                    Пожалуйста, заполните поле
                  </label>
              </div>
              <div class="modal-form-block">
                <label class="modal-form-name">Электронная почта</label>
                <div class="modal-wrapper-input">
                  <input
                      v-model="email"
                      @blur="checkEmail"
                      @input="isEmptyEmail = false"
                      @focus="isCheckEmail = true"
                      :class="{error: !isCheckEmail}"
                      type="text"
                      class="modal-form__input">
                  <template v-if="!isCheckEmail && email !== ''">
                    <div class="icon-error">
                    </div>
                    <label class="modal-input-error">
                      Неверный E-mail
                    </label>
                  </template>
                  <label
                      v-if="isEmptyEmail"
                      class="modal-input-error">
                    Пожалуйста, заполните поле
                  </label>
                </div>
              </div>
              <div class="modal-form-block">
                <label class="modal-form-name">Придумайте пароль (минимум 6 символов)</label>
                <div class="modal-form__password-wrapper">
                  <input
                      v-model="password"
                      ref="passwordInput"
                      @blur="checkPassword"
                      @input="isEmptyPassword = false"
                      @focus="isCheckPassword = true"
                      :class="{error: !isCheckPassword}"
                      :type="passwordType"
                      class="modal-form__input">

                  <template v-if="(!isCheckPassword && password !== '') || isEmptyPassword">
                    <template v-if="!isCheckPassword && password !== ''">
<!--                      <div class="icon-error">-->
<!--                      </div>-->
                      <label class="modal-input-error">
                        Пароль должен быть минимум 6 символов
                      </label>
                    </template>
                    <template v-if="isEmptyPassword">
                      <label
                          v-if="isEmptyEmail"
                          class="modal-input-error">
                        Пожалуйста, заполните поле
                      </label>
                    </template>
                  </template>
                  <button
                      @click="hidePassword"
                      type="button"
                      class="modal-form__hide">
                  </button>
                </div>
              </div>
            </div>
            <div v-if="ModalWinRegCurrentStep === 1">
              <div class="modal-reg-step-two">
                <label class="modal-form-label">Введите код для подтверждения почты (письмо с кодом отправлено на
                  указанный вами E-mail)</label>
                <input type="text" class="modal-form__input">
                <label class="modal-form-label">Если письмо не пришло, проверьте спам</label>
              </div>
            </div>
            <!--функция для переключения шага-->
            <button
                @click="checkRegFields"
                class="modal-form__submit button-orange-another">Зарегистрироваться
            </button>
            <button
                @click="openModalWinLog"
                type="button"
                class="modal-form-login">
              Войти
            </button>
          </form>
        </div>
      </modal-window>
      <modal-window

          @close="onCloseModalWin"
          :isVisible="isModalWinLog">

        <div class="modal-reg-wrapper">
          <p class="modal-title modal-title-reg">Войти</p>
          <form action="#" class="modal-form modal-form-log">
            <div class="modal-form-block">
              <label class="modal-form-name">электронная почта</label>
              <div class="modal-wrapper-input">
                <input
                    v-model="email"
                    @blur="checkEmail"
                    @input="isEmptyEmail = false"
                    @focus="isCheckEmail = true"
                    :class="{error: !isCheckEmail}"
                    type="text"
                    class="modal-form__input">
                <div
                    class="icon-error"
                    v-if="!isCheckEmail && email !== ''">
                </div>
                <label
                    v-if="!isCheckEmail && email !== ''"
                    class="modal-input-error">
                  Неверный E-mail
                </label>
                <label
                    v-if="isEmptyEmail"
                    class="modal-input-error">
                  Пожалуйста, заполните поле
                </label>
              </div>
            </div>
            <div class="modal-form-block">
              <label class="modal-form-name">Пароль</label>
              <div class="modal-form__password-wrapper">
                <input
                    v-model="password"
                    @blur="checkPassword"
                    @focus="isCheckPassword = true"
                    :class="{error: !isCheckPassword}"
                    :type="passwordType"
                    class="modal-form__input">
                <div
                    class="icon-error"
                    v-if="!isCheckPassword && password !== ''">
                </div>
                <label
                    v-if="!isCheckPassword && password !== ''"
                    class="modal-input-error">
                  Пароль должен быть минимум 6 символов
                </label>
                <button
                    v-else
                    @click="hidePassword"
                    type="button"
                    class="modal-form__hide">
                </button>
              </div>
            </div>
            <button
                @click="isModalWinResetPass = true; isModalWinLog = false"
                class="modal-form-password-reset">
              Забыли пароль?
            </button>
            <button class="modal-form__submit button-orange-another">Войти</button>
            <!--            На этой кнопки выдает ошибку-->
            <button
                @click="isModalWinReg = true; isModalWinLog = false"
                type="button"
                class="modal-form-login">
              Зарегистрироваться
            </button>
          </form>
        </div>
      </modal-window>
      <modal-window
          @close="onCloseModalResetPass"
          :isVisible="isModalWinResetPass">
        <div class="modal-reg-wrapper">
          <p class="modal-title modal-title-reg">Восстановление пароля</p>
          <form action="#" class="modal-form modal-form-reset">
            <div class="modal-form-block">
              <label v-if="resetPasswordCurrentStep === 0" class="modal-form-name">Укажите E-mail, который вы
                использовали при регистрации</label>
              <label v-if="resetPasswordCurrentStep === 1" class="modal-form-name">Введите код восстановления пароля<br>
                (письмо с кодом отправлено на указанный E-mail)</label>
              <label v-if="resetPasswordCurrentStep === 2" class="modal-form-name">Придумайте новый пароль (минимум 6
                символов)</label>
              <div v-if="resetPasswordCurrentStep === 0 || resetPasswordCurrentStep === 1" class="modal-wrapper-input">
                <input
                    v-model="email"
                    @blur="checkEmail"
                    @focus="isCheckEmail = true"
                    :class="{error: !isCheckEmail}"
                    type="text"
                    class="modal-form__input">
                <div
                    class="icon-error"
                    v-if="!isCheckEmail && email !== ''">
                </div>
                <label
                    v-if="!isCheckEmail && email !== ''"
                    class="modal-input-error">
                  Неверный E-mail
                </label>
              </div>
              <div v-if="resetPasswordCurrentStep === 2" class="modal-wrapper-input">
                <input
                    type="text"
                    class="modal-form__input">
                <div
                    class="icon-error">
                </div>
                <label
                    class="modal-input-error">
                  Неверный E-mail
                </label>
              </div>
            </div>
            <button type="button" @click.stop="resetPasswordCurrentStep++"
                    class="modal-form__submit button-orange-another">Далее
            </button>
          </form>
        </div>
      </modal-window>
      <button
          @click="openItem"
          :class="{active: isMenuActive}"
          class="menu-btn">
        <span class="menu-btn__line"></span>
        <span class="menu-btn__line"></span>
        <span class="menu-btn__line"></span>
      </button>
    </div>
  </header>
</template>

<script>
import ModalWindow from "@/components/ui/modalWin.vue";
import _ from 'lodash';

export default {
  name: 'site-header',
  components: {
    ModalWindow
  },
  data() {
    return {
      name: '',
      password: '',
      email: '',

      isCheckEmail: true,
      isCheckPassword: true,
      isEmptyEmail: false,
      isEmptyPassword: false,
      isEmptyName: false,

      passwordType: 'password',
      resetPasswordCurrentStep: 0,
      ModalWinRegCurrentStep: 0,

      isModalWinReg: false,
      isModalWinLog: false,
      isModalWinResetPass: false,

      isMenuActive: false,
    }
  },

  methods: {
    checkRegFields() {
      this.isEmptyEmail = _.isEmpty(this.email);
      this.isEmptyName = _.isEmpty(this.name);
      this.isEmptyPassword = _.isEmpty(this.password);

      if (this.isEmptyName || this.isEmptyPassword || this.isEmptyPassword) {
        return;
      }
      this.ModalWinRegCurrentStep++
    },
    openModalWinLog() {
      this.sModalWinLog = true;
      this.isModalWinReg = false;
    },
    onCloseModalWin() {
      this.isModalWinLog = false
      this.clearModalData();
    },
    onCloseModalReg() {
      this.isModalWinReg = false
      this.clearModalData();
    },
    onCloseModalResetPass() {
      this.isModalWinResetPass = false
    },
    clearModalData() {
      this.email = '';
      this.password = '';
      this.name = '';
    },
    checkEmail() {
      if (this.email === '') {
        return;
      }
      let re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      this.isCheckEmail = re.test(this.email);
    },
    checkPassword() {
      if (this.password === '') {
        return;
      }
      this.password.length < 6 ? this.isCheckPassword = false : this.isCheckPassword = true;
    },

    openItem() {
      this.isMenuActive = !this.isMenuActive;
      document.documentElement.style.overflow = 'hidden';
    },
    hidePassword() {
      this.passwordType = this.passwordType === 'password' ? 'text' : 'password';
    }
  },
  watch: {
    isMenuActive: function () {
      if (this.isMenuActive) {
        document.documentElement.style.overflow = 'hidden'
        return
      }
      document.documentElement.style.overflow = 'auto'
    },
  },
  computed: {

  }
}
</script>

<style lang="scss">
@import "../../style/header";
@import "../../style/main";

</style>
