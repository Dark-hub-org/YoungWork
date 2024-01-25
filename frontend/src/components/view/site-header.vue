<template>
  <header class="header">
    <div class="wrapper header__wrapper">
      <router-link
          to="/"
          tag="a"
          class="header-logo-link">
        <img src="@/assets/logo.svg" alt="логотип" class="header__logo">
      </router-link>
      <nav
          :class="{active: isMenuActive}"
          class="header__nav">
        <ul class="header__nav-list">
          <li class="header__nav-item">
            <button type="button" class="button-orange header__nav-button">Услуги</button>
          </li>
          <li class="header__nav-item">
            <button type="button" class="button-orange header__nav-button">Работа</button>
          </li>
          <template v-if="!isAutoRization">
            <li class="header__nav-item">
              <button
                  @click="isModalWinLog = true"
                  type="button"
                  class="button-green header__nav-button">
                Вход
              </button>
            </li>
            <li class="header__nav-item">
              <button
                  @click="isModalVisSwitch = true"
                  type="button"
                  class="button-green header__nav-button">
                Регистрация
              </button>
            </li>
          </template>
          <template v-else>
            <div class="header-supernova">
              <button @click="openSupernovaMenu" type="button" class="supernova__btn"></button>
              <div class="supernova-wrapper" v-if="isSupernovaMenuActive">
                <router-link to="/profile/applicant" tag="li" class="supernova-wrapper-item">
                  <span class="supernova-wrapper__name">{{ userName }}</span>
                </router-link>
                <ul class="supernova-wrapper-list">
                  <router-link to="/vacancies" tag="li" class="supernova-wrapper-item">
                    <a href="/vacancy" class="supernova-wrapper-link">Работа</a>
                  </router-link>
                  <li class="supernova-wrapper-item">
                    <ul @click="openSubMenu" class="supernova-wrapper-sublist" :class="{active: isSubMenu}">
                      <span class="supernova-wrapper-title" :class="{active: isSubMenu}">Услуги</span>
                      <router-link to="/vacancies" tag="li">
                        <a href="/vacancy" class="supernova-sublist-title">Найти задание</a>
                      </router-link>
                      <router-link to="/create-vacancy" tag="li">
                        <a href="/create-vacancy" class="supernova-sublist-title">Создать задание</a>
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
      <Transition name="modal">
        <modal-window
            @close="onCloseModalSwitch"
            :isVisible="isModalVisSwitch">
          <div class="modal-switch-wrapper">
            <p class="modal-title">Что вы тут делаете?</p>
            <div class="modal-switch__block">
              <button class="modal-switch__btn" @click="openModalWinReg('applicant')">Ищу работу</button>
              <button class="modal-switch__btn btn--green" @click="openModalWinReg('employer')">Ищу сотрудника</button>
            </div>
          </div>
        </modal-window>
      </Transition>
      <Transition name="modal">
        <modal-window
            @close="onCloseModalReg"
            :isVisible="isModalWinReg">
          <div class="modal-reg-wrapper">
            <p class="modal-title">Регистрация</p>
            <form @submit.prevent="submitFormReg" class="modal-form">
              <div v-if="ModalWinRegCurrentStep === 0">
                <!--                <div class="modal-form-block">-->
                <!--                  <label class="modal-form-name">Имя</label>-->
                <!--                  <div class="modal-wrapper-input">-->
                <!--                    <input-->
                <!--                        v-model.trim="userName"-->
                <!--                        @input="isEmptyName = false"-->
                <!--                        type="text"-->
                <!--                        class="modal-form__input"-->
                <!--                        :class="{error: isEmptyName}">-->
                <!--                    <template v-if="isEmptyName">-->
                <!--                      <div class="icon-error">-->
                <!--                      </div>-->
                <!--                      <label-->
                <!--                          class="modal-input-error">-->
                <!--                        Пожалуйста, заполните поле-->
                <!--                      </label>-->
                <!--                    </template>-->
                <!--                  </div>-->
                <!--                </div>-->
                <div class="modal-form-block">
                  <label class="modal-form-name">Электронная почта</label>
                  <div class="modal-wrapper-input">
                    <input
                        v-model.trim="email"
                        @blur="checkEmail"
                        @input="isEmptyEmail = false"
                        @focus="isCheckEmail = undefined"
                        type="text"
                        class="modal-form__input"
                        :class="{error: this.isCheckEmail === false || isEmptyEmail}">
                    <template v-if="this.isCheckEmail === false && email !== '' || isEmptyEmail">
                      <div class="icon-error">
                      </div>
                      <label v-if="this.isCheckEmail === false" class="modal-input-error">
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
                        @blur="checkPassword"
                        @focus="isCheckPassword = undefined"
                        @input="isEmptyPassword = false"
                        :class="{error: this.isCheckPassword === false || isEmptyPassword}"
                        :type="isHidePassword ? 'password' : 'text'"
                        class="modal-form__input">
                    <template v-if="(this.isCheckPassword === false && password !== '') || isEmptyPassword">
                      <template v-if="!isCheckPassword && password !== ''">
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
      </Transition>
      <Transition name="modal">
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
                      v-model.trim="email"
                      @blur="checkEmail"
                      @input="isEmptyEmail = false"
                      @focus="isCheckEmail = undefined"
                      type="text"
                      class="modal-form__input"
                      :class="{error: this.isCheckEmail === false || isEmptyEmail}">
                  <template v-if="this.isCheckEmail === false && email !== '' || isEmptyEmail">
                    <div class="icon-error">
                    </div>
                    <label v-if="this.isCheckEmail === false" class="modal-input-error">
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
                <label class="modal-form-name">Пароль</label>
                <div class="modal-form__password-wrapper">
                  <input
                      v-model.trim="password"
                      @blur="checkPassword"
                      @focus="isCheckPassword = undefined"
                      @input="isEmptyPassword = false"
                      :class="{error: this.isCheckPassword === false || isEmptyPassword}"
                      :type="isHidePassword ? 'password' : 'text'"
                      class="modal-form__input">
                  <template v-if="(this.isCheckPassword === false && password !== '') || isEmptyPassword">
                    <template v-if="!isCheckPassword && password !== ''">
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
      </Transition>
      <Transition name="modal">
        <modal-window
            @close="onCloseModalResetPass"
            :isVisible="isModalWinResetPass">
          <div class="modal-reg-wrapper">
            <p class="modal-title modal-title-reg">Восстановление пароля</p>
            <form action="#" class="modal-form modal-form-reset">
              <div class="modal-form-block">
                <label v-if="resetPasswordCurrentStep === 0" class="modal-form-name">Укажите E-mail, который вы
                  использовали при регистрации</label>
                <label v-if="resetPasswordCurrentStep === 1" class="modal-form-name">Введите код восстановления
                  пароля<br>
                  (письмо с кодом отправлено на указанный E-mail)</label>
                <label v-if="resetPasswordCurrentStep === 2" class="modal-form-name">Придумайте новый пароль (минимум 8
                  символов)</label>

                <div v-if="resetPasswordCurrentStep === 0 || resetPasswordCurrentStep === 1"
                     class="modal-wrapper-input">
                  <input
                      v-model.trim="email"
                      @blur="checkEmail"
                      @input="isEmptyEmail = false"
                      @focus="isCheckEmail = undefined"
                      :class="{error: this.isCheckEmail === false}"
                      type="text"
                      class="modal-form__input">
                  <template v-if="this.isCheckEmail === false && email !== ''">
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
              <button type="button" @click.stop="refreshPassword()"
                      class="modal-form__submit button-orange-another">Далее
              </button>
            </form>
          </div>
        </modal-window>
      </Transition>
      <button
          @click="openItem"
          :class="{active: isMenuActive}"
          class="header__menu-btn">
        <span class="header__menu-btn__line"></span>
        <span class="header__menu-btn__line"></span>
        <span class="header__menu-btn__line"></span>
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
      password: '',
      userName: '',
      userType: '',

      isCheckEmail: undefined,
      isCheckPassword: undefined,
      isEmptyEmail: false,
      isEmptyPassword: false,
      isEmptyName: false,

      isHidePassword: true,
      resetPasswordCurrentStep: 0,
      ModalWinRegCurrentStep: 0,

      isModalVisSwitch: false,
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
    validFormReg() {
      return this.isEmptyEmail || this.isCheckEmail || this.isEmptyPassword || this.isCheckPassword
    },
    async submitFormReg() {
      const presentUser = {
        email: this.email,
        password: this.password,
        usertype: this.userType,
      };
      try {
        if (this.validFormReg()) {
          await axios.post('/api/users/', presentUser);
          this.authentication(presentUser);
          this.onCloseModalReg();
        }
      } catch (error) {
        console.log(error.request.response)
        console.error(error);
      }
    },
    async authentication(presentUser) {
      axios.defaults.headers.common['Authorization'] = ''
      localStorage.removeItem('access')
      try {
        const response = await axios.post('/api/jwt/create/', presentUser);
        const access = response.data.access;
        const refresh = response.data.refresh;
        this.$store.commit('setAccess', access);
        this.$store.commit('setRefresh', refresh);
        this.isAutoRization = true;
        this.isModalWinLog = false;
        axios.defaults.headers.common['Authorization'] = 'JWT ' + access;
        localStorage.setItem('isAutoRization', this.isAutoRization);
        const response_id = await axios.get('/api/me/')
        const id = response_id.data.id
        this.$store.commit('setId', id)
        location.reload();
      } catch (error) {
        console.error(error);
      }
    },
    async logIn() {
      try {
        const presentUser = {
          email: this.email,
          password: this.password,
        }
        axios.defaults.headers.common['Authorization'] = ''
        localStorage.removeItem('access')
        if (this.validFormReg()) {
          const response = await axios.post('/api/jwt/create/', presentUser)
          const access = response.data.access
          const refresh = response.data.refresh
          this.$store.commit('setAccess', access)
          this.$store.commit('setRefresh', refresh)
          this.isAutoRization = true;
          this.isModalWinLog = false;
          axios.defaults.headers.common['Authorization'] = 'JWT ' + access
          localStorage.setItem('isAutoRization', this.isAutoRization);
          const response_id = await axios.get('/api/me/')
          const id = response_id.data.id
          this.$store.commit('setId', id)
          location.reload()
        }
      } catch (error) {
        console.log(error)
      }
    },
    getMe() {
      axios.get('/api/me/')
          .then(response => {
            this.userName = response.data.first_name
          })
          .catch(error => {
            console.log(error)
          })
    },
    logOut() {
      localStorage.removeItem('id')
      localStorage.removeItem('access')
      localStorage.removeItem('refresh')
      localStorage.removeItem('isAutoRization')
      location.reload()
      this.$router.push('/')
    },
    checkRegFields() {
      this.isEmptyEmail = _.isEmpty(this.email);
      this.isEmptyName = _.isEmpty(this.userName);
      this.isEmptyPassword = _.isEmpty(this.password);
      if (this.isEmptyEmail || this.isEmptyName || this.isEmptyPassword) {
        return;
      }
    },
    openNextStep() {
      this.checkRegFields();

      if (this.isEmptyName || this.isEmptyPassword || this.isEmptyName || this.isCheckPassword || this.isCheckEmail) {
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
    openModalWinReg(type) {
      this.userType = type
      this.clearModalData();
      //
      if (this.isModalVisSwitch === true) {
        this.isModalVisSwitch = false;
      }
      this.isModalWinReg = true;
      this.isModalWinLog = false
    },
    openModalWinReset() {
      this.clearModalData();
      this.isModalWinResetPass = true;
      this.isModalWinLog = false
    },
    onCloseModalSwitch() {
      this.isModalVisSwitch = false
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
      this.isHidePassword = true;
      this.isCheckEmail = true;
      this.isCheckPassword = undefined;
      this.isEmptyEmail = false;
      this.isEmptyPassword = false;
      this.isEmptyName = false;
    },
    checkEmail() {
      if (this.email === '') {
        return;
      }
      let re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return this.isCheckEmail = re.test(this.email);
    },
    checkPassword() {
      if (this.password === '') {
        return;
      }
      return this.isCheckPassword = this.password.length >= 8
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
    //   this.email = this.email.charAt(0).toUpperCase() + this.email.slice(1).toLowerCase().replace(/\s/g, '');
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
        return this.email
      },
      set: function (value) {
        this.email = value.charAt(0).toUpperCase() + value.slice(1).toLowerCase().replace(/\s/g, '');
      }

    }
  }
}
</script>

<style lang="scss">
@import "@/style/header";

</style>

<style>

.modal-enter-active, .modal-leave-active {
  transition: opacity .3s;
}

.modal-enter, .modal-leave-to {
  opacity: 0;
}

</style>
