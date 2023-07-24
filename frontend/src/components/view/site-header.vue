<template>
  <header class="header">
    <div class="wrapper wrapper-header">
      <router-link
          to="/"
          tag="a"
          class="header-logo-link">
        <img src="@/assets/logo.svg" alt="логотип" class="header-logo">
      </router-link>
      <!-- <a href="#" class="header-logo-link">
        <img src="@/assets/logo.svg" alt="логотип" class="header-logo">
      </a> -->
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
          <template v-if="!isAutoRization">
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
          </template>
          <template v-else>
            <div class="header-supernova">
              <button @click="openSupernovaMenu" type="button" class="supernova__btn"></button>
              <div class="supernova-wrapper" v-if="isSupernovaMenuActive">
                <span class="supernova-wrapper__name" :src="user_data">{{ user_data }}</span>
                <ul class="supernova-wrapper-list">
                  <router-link to="#" tag="li" class="supernova-wrapper-item">
                    <a href="#" class="supernova-wrapper-link">Работа</a>
                  </router-link>
                  <li class="supernova-wrapper-item">
                    <ul @click="openSubMenu" class="supernova-wrapper-sublist" :class="{active: isSubMenu}">
                      <span class="supernova-wrapper-title" :class="{active: isSubMenu}">Услуги</span>
                      <router-link to="#" tag="li">
                        <a href="#" class="supernova-sublist-title">Найти задание</a>
                      </router-link>
                      <router-link to="#" tag="li">
                        <a href="#" class="supernova-sublist-title">Создать задание</a>
                      </router-link>
                    </ul>
                  </li>
                  <li class="supernova-wrapper-item">
                    <button @click="logOut" class="supernova-exits-btn">
                      Выход
                    </button>
                  </li>
                </ul>
              </div>
            </div>
          </template>
        </ul>
      </nav>
      <modal-window
          @close="onCloseModalReg"
          :isVisible="isModalWinReg">
        <div class="modal-reg-wrapper">
          <p class="modal-title">Регистрация</p>
          <form @submit.prevent="submitFormReg" class="modal-form">
            <div v-if="ModalWinRegCurrentStep === 0">
              <div class="modal-form-block">
                <label class="modal-form-name">Имя</label>
                <div class="modal-wrapper-input">
                  <input
                      v-model.trim="name"
                      @input="isEmptyName = false"
                      @focus="isEmptyName = false"
                      type="text"
                      class="modal-form__input"
                      :class="{error: isEmptyName}">
                  <template v-if="isEmptyName">
                    <div class="icon-error">
                    </div>
                    <label
                        class="modal-input-error">
                      Пожалуйста, заполните поле
                    </label>
                  </template>
                </div>
              </div>
              <div class="modal-form-block">
                <label class="modal-form-name">Электронная почта</label>
                <div class="modal-wrapper-input">
                  <input
                      v-model.trim="email"
                      @blur="checkEmail"
                      @input="isEmptyEmail = false"
                      @focus="isCheckEmail = true"
                      :class="{error: !isCheckEmail || isEmptyEmail}"
                      type="text"
                      class="modal-form__input">
                  <template v-if="!isCheckEmail && email !== '' || isEmptyEmail">
                    <div class="icon-error">
                    </div>
                    <label v-if="!isCheckEmail" class="modal-input-error">
                      Неверный E-mail
                    </label>
                    <label
                        v-if="isEmptyEmail"
                        class="modal-input-error">
                      Пожалуйста, заполните поле
                    </label>
                  </template>
                </div>
              </div>
              <div class="modal-form-block">
                <label class="modal-form-name">Придумайте пароль (минимум 8 символов)</label>
                <div class="modal-form__password-wrapper">
                  <input
                      v-model.trim="password"
                      ref="passwordInput"
                      @blur="checkPassword"
                      @input="isEmptyPassword = false"
                      @focus="isCheckPassword = true; isEmptyPassword = false"
                      :class="{error: !isCheckPassword || isEmptyPassword}"
                      :type="isHidePassword ? 'password' : 'text'"
                      class="modal-form__input">

                  <template v-if="(!isCheckPassword && password !== '') || isEmptyPassword">
                    <template v-if="!isCheckPassword && password !== ''">
                      <!-- <div class="icon-error">
                      </div> -->
                      <label class="modal-input-error">
                        Пароль должен быть минимум 8 символов
                      </label>
                    </template>
                    <template v-if="isEmptyPassword">
                      <label
                          v-if="isEmptyPassword"
                          class="modal-input-error">
                        Пожалуйста, заполните поле
                      </label>
                    </template>
                  </template>

                  <i v-if="isHidePassword" @click="isHidePassword = false;" class="bx bx-hide modal-form__hide"></i>
                  <i v-else @click="isHidePassword = true" class="bx bx-show modal-form__hide"></i>
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
            <!-- функция для переключения шага
            @click="openNextStep" -->
            <button
                type="submit"
                class="modal-form__submit button-orange-another"
                @click="checkRegFields">Зарегистрироваться
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
          <form class="modal-form modal-form-log">
            <div class="modal-form-block">
              <label class="modal-form-name">Электронная почта</label>
              <div class="modal-wrapper-input">
                <input
                    v-model.trim="username"
                    @input="isEmptyName = false"
                    @focus='isEmptyName = false'
                    type="text"
                    class="modal-form__input"
                    :class="{error: isEmptyName}">
                <template v-if="isEmptyName">
                  <div class="icon-error">
                  </div>
                  <label
                      v-if="isEmptyEmail"
                      class="modal-input-error">
                    Пожалуйста, заполните поле
                  </label>
                </template>
              </div>
            </div>
            <div class="modal-form-block">
              <label class="modal-form-name">Пароль</label>
              <div class="modal-form__password-wrapper">
                <input
                    v-model.trim="password"
                    @blur="checkPassword"
                    @focus="isCheckPassword = true"
                    @input="isEmptyPassword = false"
                    :class="{error: !isCheckPassword || isEmptyPassword}"
                    :type="isHidePassword ? 'password' : 'text'"
                    class="modal-form__input">
                <!-- <div
                class="icon-error"
                v-if="!isCheckPassword && password !== ''">
                </div> -->
                <template v-if="(!isCheckPassword && password !== '') || isEmptyPassword">
                  <template v-if="!isCheckPassword && password !== ''">
                    <!-- <div class="icon-error">
                    </div> -->
                    <label class="modal-input-error">
                      Пароль должен быть минимум 8 символов
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
                <i v-if="isHidePassword" @click="isHidePassword = false;" class="bx bx-hide modal-form__hide"></i>
                <i v-else @click="isHidePassword = true" class="bx bx-show modal-form__hide"></i>
              </div>
            </div>
            <button
                type="button"
                @click="openModalWinReset()"
                class="modal-form-password-reset">
              Забыли пароль?
            </button>
            <button
                type="button"
                @click="checkRegFields(); logIn()"
                class="modal-form__submit button-orange-another">
              Войти
            </button>
            <!--  onCloseModalWin();  -->
            <button
                @click="openModalWinReg"
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
              <label v-if="resetPasswordCurrentStep === 2" class="modal-form-name">Придумайте новый пароль (минимум 8
                символов)</label>

              <div v-if="resetPasswordCurrentStep === 0 || resetPasswordCurrentStep === 1" class="modal-wrapper-input">
                <input
                    v-model.trim="email"
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
import axios from "axios"

export default {
  name: 'SiteHeader',
  components: {
    ModalWindow
  },
  data() {
    return {
      email: '',
      username: '',
      password: '',
      user_data: '',
      name: '',

      isCheckEmail: true,
      isCheckPassword: true,
      isEmptyEmail: false,
      isEmptyPassword: false,
      isEmptyName: false,

      isHidePassword: true,
      resetPasswordCurrentStep: 0,
      ModalWinRegCurrentStep: 0,

      isModalWinReg: false,
      isModalWinLog: false,
      isModalWinResetPass: false,

      isMenuActive: false,

      isAutoRization: false,
      isSupernovaMenuActive: false,
      isSubMenu: false,
    }
  },
  mounted() {
    this.getMe();
    this.isAutoRization = localStorage.getItem('isAutoRization');
  },
  methods: {
    submitFormReg() {
      if (this.isEmptyEmail || this.isEmptyName || this.isEmptyPassword || !this.isCheckPassword || !this.isCheckEmail) {
        return
      }
      const presentUser = {
        email: this.email,
        username: this.email,
        password: this.password,
      };
      axios.post('/api/v1/users/', presentUser)
          .then(response => {
            console.log(response)
            this.authentication(presentUser)
          })
          .catch(error => {
            console.log(error)
          });
      this.onCloseModalReg();
    },
    authentication(presentUser) {
      axios.defaults.headers.common['Authorization'] = ''
      localStorage.removeItem('access')


      axios.post('/api/v1/jwt/create/', presentUser)
          .then(response => {
            console.log(response)
            const access = response.data.access
            const refresh = response.data.refresh
            this.$store.commit('setAccess', access)
            this.$store.commit('setRefresh', refresh)
            this.isAutoRization = true;
            this.isModalWinLog = false;
            axios.defaults.headers.common['Authorization'] = 'JWT ' + access
            localStorage.setItem('access', access)
            localStorage.setItem('refresh', refresh)
            localStorage.setItem('isAutoRization', this.isAutoRization);
            location.reload()
          })
          .catch(error => {
            console.log(error)
          })
    },
    logIn() {
      if (!this.isCheckPassword || this.isEmptyName || this.isEmptyPassword) {
        return;
      }
      axios.defaults.headers.common['Authorization'] = ''
      localStorage.removeItem('access')

      const presentUser = {
        username: this.username,
        password: this.password,
      }

      axios.post('/api/v1/jwt/create/', presentUser)
          .then(response => {
            console.log(response)
            const access = response.data.access
            const refresh = response.data.refresh
            this.$store.commit('setAccess', access)
            this.$store.commit('setRefresh', refresh)
            this.isAutoRization = true;
            this.isModalWinLog = false;
            axios.defaults.headers.common['Authorization'] = 'JWT ' + access
            localStorage.setItem('access', access)
            localStorage.setItem('refresh', refresh)
            localStorage.setItem('isAutoRization', this.isAutoRization);
            location.reload()
          })
          .catch(error => {
            console.log(error)
          })
    },
    getMe() {
      axios.get('/api/v1/users/me')
          .then(response => {
            console.log(response)
            this.user_data = response.data.username
          })
          .catch(error => {
            console.log(error)
          })
    },
    logOut() {
      localStorage.removeItem('access')
      localStorage.removeItem('refresh')
      localStorage.removeItem('isAutoRization')
      location.reload()
    },
    refreshPassword() {
      const presentUser = {
        email: this.email
      }
      axios.post('/api/v1/users/reset_password/', presentUser)
          .then(response => {
            console.log(response)
          })
          .catch(error => {
            console.log(error)
          });
    },
    checkRegFields() {
      this.isEmptyEmail = _.isEmpty(this.email);
      this.isEmptyName = _.isEmpty(this.username);
      this.isEmptyPassword = _.isEmpty(this.password);
      if (this.isEmptyEmail || this.isEmptyName || this.isEmptyPassword) {
        return;
      }
    },
    openNextStep() {
      this.checkRegFields();

      if (this.isEmptyName || this.isEmptyPassword || this.isEmptyName || !this.isCheckPassword || !this.isCheckEmail) {
        return;
      }
      this.ModalWinRegCurrentStep++
    },
    openModalWinLog() {
      this.clearModalData();
      // 
      this.isModalWinLog = true;
      this.isModalWinReg = false;
    },
    openModalWinReg() {
      this.clearModalData();
      // 
      this.isModalWinReg = true;
      this.isModalWinLog = false
    },
    openModalWinReset() {
      this.clearModalData();
      this.isModalWinResetPass = true;
      this.isModalWinLog = false
    },
    onCloseModalWin() {
      this.isModalWinLog = false
      this.clearModalData();
    },
    onCloseModalReg() {
      this.isModalWinReg = false;
      this.clearModalData();
    },
    onCloseModalResetPass() {
      this.isModalWinResetPass = false
    },
    clearModalData() {
      this.email = '';
      this.password = '';
      this.username = '';
      this.isHidePassword = true;
      this.isCheckEmail = true;
      this.isCheckPassword = true;
      this.isEmptyEmail = false;
      this.isEmptyPassword = false;
      this.isEmptyName = false;
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
      this.password.length < 8 ? this.isCheckPassword = false : this.isCheckPassword = true;
    },

    openItem() {
      this.isMenuActive = !this.isMenuActive;
      document.documentElement.style.overflow = 'hidden';
    },
    openSupernovaMenu() {
      this.isSupernovaMenuActive = !this.isSupernovaMenuActive;
    },
    openSubMenu() {
      this.isSubMenu = !this.isSubMenu;
    },
    // validName() {
    //   this.username = this.username.charAt(0).toUpperCase() + this.username.slice(1).toLowerCase().replace(/\s/g, '');
    // }
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
    formaterName: {
      get: function () {
        return this.username
      },
      set: function (value) {
        this.username = value.charAt(0).toUpperCase() + value.slice(1).toLowerCase().replace(/\s/g, '');
      }

    }
  }
}
</script>

<style lang="scss">
@import "@/style/header";

</style>
