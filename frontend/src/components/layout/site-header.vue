<template>
  <header class="header">
    <div class="wrapper header__wrapper">
      <router-link
          to="/"
          tag="a"
          class="header-logo-link">
        <img src="../../assets/logo.svg" alt="логотип" class="header__logo">
      </router-link>
      <nav
          :class="{active: isMenuActive}"
          class="header__nav">
        <ul class="header__nav-list">
          <template v-if="!isAuthorization">
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
            <router-link to="/favorites/" tag="li" class="header__button">
              <img src="../../assets/star.svg" alt="кнопка избранных вакансий">
            </router-link>
            <button @click="isVisibleNotifications = !isVisibleNotifications" class="header__alerts" ref="alert">
              <img src="../../assets/alerts.svg" alt="кнопка оповещений">
            </button>
            <button ref="buttonChat" @click="isChatActive = !isChatActive" class="header__alerts">
              <img src="../../assets/message.svg" alt="кнопка чата">
            </button>
          </template>
        </ul>
        <div v-if="isAuthorization" class="header-supernova">
          <button
              @click="openSupernovaMenu"
              ref="supernovaBtn"
              type="button"
              class="supernova__btn">
            <img v-if="userData.avatar" class="header__avatar" style="width: 50px; height: 50px" :src='"/img" + userData.avatar' alt="">
          </button>
          <div
              :class="{'active': isSupernovaMenuActive}"
              ref="supernova"
              class="supernova-wrapper">
            <ul class="supernova-wrapper-list">
              <li class="supernova-wrapper-item">
                <a :href="`/${userData.usertype}/`" class="supernova-wrapper__name">{{
                    userData.firstName
                  }}</a>
              </li>
              <li class="supernova-wrapper-item supernova-wrapper-item--section">
                <div @click.stop="openSubMenu" class="supernova-wrapper-block">
                  <img src="../../assets/vacancy.svg" alt="кнопка избранное" class="supernova-wrapper-image">
                  <button class="supernova-wrapper-text">
                    <template v-if="userData.usertype === 'employer'">Вакансии</template>
                    <template v-if="userData.usertype === 'applicant'">Резюме</template>
                  </button>
                </div>
                <ul class="supernova-wrapper-sublist" :class="{active: isSubMenu}">
                  <template v-if="userData.usertype === 'employer'">
                    <router-link class="supernova-wrapper-sublist__link" to="/create-vacancy" tag="li">
                      <span>Создать вакансию</span>
                    </router-link>
                    <li @click="routeUserData" class="supernova-wrapper-sublist__link">
                      <span>Мои вакансии</span>
                    </li>
                  </template>
                  <template v-if="userData.usertype === 'applicant'">
                    <li class="supernova-wrapper-sublist__link">
                      <router-link  to="/create-resume" tag="a">
                        Создать резюме
                      </router-link>
                    </li>
                    <li @click="routeUserData" class="supernova-wrapper-sublist__link">
                      <span>Мои резюме</span>
                    </li>
                  </template>
                </ul>
              </li>
              <li class="supernova-wrapper-item supernova-wrapper-item--padding-top">
                <div class="supernova-wrapper-block">
                  <img src="../../assets/exit.svg" alt="кнопка избранное" class="supernova-wrapper-image">
                  <button @click="switchType" class="supernova-wrapper-text">Сменить аккаунт</button>
                </div>
              </li>
              <li class="supernova-wrapper-item">
                <button @click.prevent="logOut" class="supernova-exits-btn">Выйти</button>
              </li>
            </ul>
          </div>
        </div>
      </nav>
      <transition name="modal">
        <the-notification
            @close-notification="onCloseNotification"
            :alerts-button="this.$refs.alert"
            :is-visible="isVisibleNotifications">
        </the-notification>
      </transition>
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
            <form @submit.prevent="checkRegFields(); logIn()" class="modal-form modal-form-log">
              <p class="modal-form__error" v-if="formError">{{formError}}</p>
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
                  <template v-if="this.isCheckEmail === false && email.length || isEmptyEmail">
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
                      name="password"
                      autocomplete="on"
                      class="modal-form__input">
                  <template v-if="(this.isCheckPassword === false && password.length) || isEmptyPassword">
                    <template v-if="!this.isCheckPassword && password.length < 8">
                      <label class="modal-input-error">
                        Пароль должен быть минимум 8 символов
                      </label>
                    </template>
                    <template v-if="!this.isCheckPassword && password.length >= 8">
                      <label class="modal-input-error">
                        Неверный пароль
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
                  type="submit"
                  @click="checkRegFields(); logIn()"
                  class="modal-form__submit button-orange-another">
                Войти
              </button>
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
      <Transition name="chat">
        <the-chat
            :is-visible="isChatActive"
            :chat-button="this.$refs.buttonChat"
            @close-chat="closeChat()"
            />
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
    <transition name="alert">
      <the-alert
          v-if="isAlert"
          :text="alertText"
      ></the-alert>
    </transition>
  </header>
</template>

<script>
import ModalWindow from "@/components/common/modalWin.vue";
import _ from 'lodash';
import axios from "axios"
import TheChat from "@/components/common/chat.vue";
import TheNotification from "@/components/common/notifications.vue";
import TheAlert from "@/components/common/alert.vue";

export default {
  name: 'SiteHeader',
  components: {
    TheAlert,
    TheNotification,
    TheChat,
    ModalWindow
  },
  data() {
    return {
      email: '',
      password: '',
      userType: '',
      userId: '',
      formError: '',

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
      isAuthorization: false,
      isAuthorized: false,
      isSupernovaMenuActive: false,
      isSubMenu: false,

      isChatActive: false,

      isVisibleNotifications: false,

      isAlert: false,
      alertText: '',
    }
  },
  methods: {
    routeUserData() {
      if(this.userData.usertype === 'employer') {
        this.$router.push({name: 'employer', params: {id: this.userData.id}})
      } else {
        this.$router.push({name: 'applicant', params: {id: this.userData.id}})
      }
      if(this.$route.path === '/applicant/' || this.$route.path === '/employer/') {
        this.$store.dispatch('setUserData')
      }
      localStorage.setItem('applicantTab', JSON.stringify(2));
    },
    validFormReg() {
      return this.isEmptyEmail || this.isCheckEmail || this.isEmptyPassword || this.isCheckPassword
    },
    async submitUserType(usertype, userId) {
      try {
        await axios.post(`/api/${usertype}/`, {user: userId})
      } catch (error) {
        console.log(error)
      }
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
        this.showAlert(error.request.response.email)
      }
    },
    async authentication(presentUser) {
      axios.defaults.headers.common['Authorization'] = ''
      localStorage.removeItem('access')
      try {
        const response = await axios.post('api/jwt/create', presentUser);
        axios.defaults.headers.common['Authorization'] = 'JWT ' + response.data.access;
        this.$store.commit('setAccess', response.data.access);
        this.$store.commit('setRefresh', response.data.refresh);
        const user = await axios.get('/api/me/')
        await this.$store.dispatch('setUserData')
        await this.$store.dispatch('changeAuthorization', true)
        await this.submitUserType(this.userType, user.data.id)
        await this.$router.push(`/${this.userType}/edit/`)
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
          axios.defaults.headers.common['Authorization'] = 'JWT ' + response.data.access
          this.$store.commit('setAccess', response.data.access)
          this.$store.commit('setRefresh', response.data.refresh)
          this.$store.commit('changeAuthorization', true)
          await axios.get('/api/update_last_log_in/')
          window.location.reload();
        }
      } catch (error) {
        this.formError = error.response.data.detail
        this.isCheckEmail = false
        this.isCheckPassword = false
      }
    },
    logOut() {
      localStorage.removeItem('access')
      localStorage.removeItem('refresh')
      localStorage.removeItem('isAuthorization')
      this.$router.push('/')
      location.reload()
    },
    async switchType() {
      try {
        await axios.post('/api/switch/')
        this.$router.push('/')
        window.location.reload()
      } catch (error) {
        console.log(error)
      }
    },
    checkRegFields() {
      this.isEmptyEmail = _.isEmpty(this.email);
      this.isEmptyPassword = _.isEmpty(this.password);
      if (this.isEmptyEmail || this.isEmptyName || this.isEmptyPassword) {
        return;
      }
    },
    openModalWinLog() {
      this.clearModalData();
      this.isModalWinLog = true;
      this.isModalWinReg = false;
    },
    openModalWinReg(type) {
      this.userType = type
      this.clearModalData();
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

    onCloseNotification() {
      this.isVisibleNotifications = false
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
    closeDropdownOnOutsideClick(event) {
      const menu = this.$refs.supernova
      const menuBtn = this.$refs.supernovaBtn

      if (menu && menuBtn) {
        return !menu.contains(event.target) && !menuBtn.contains(event.target) ? this.isSupernovaMenuActive = false : this.isSupernovaMenuActive
      }
    },
    closeChat() {
      this.isChatActive = false
    },
    showAlert(text) {
      this.alertText = text
      this.isAlert = true;
      setTimeout(() => {
        this.isAlert = false
      }, 5000)
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
    '$store.state.isAuthorization': {
      handler(newEmail) {
        if (newEmail) {
          this.isAuthorization = true
        }
      },
      immediate: true,
    },
  },
  computed: {
    userData() {
      return this.$store.state.userData
    },

  },
  mounted() {
    document.addEventListener('click', this.closeDropdownOnOutsideClick)
  }
}
</script>

<style lang="scss">

.modal-enter-active, .modal-leave-active {
  transition: opacity .2s;
}

.modal-enter, .modal-leave-to {
  opacity: 0;
}

.chat-enter-active, .chat-leave-active {
  transition: opacity .2s ease, height .2s ease;
}

.chat-enter, .chat-leave-to {
  opacity: 0;
}

.alert-enter-active, .alert-leave-active {
  transition: all .2s ease;
}

.alert-enter, .alert-leave-to {
  opacity: 0;
  transform: translateX(30px);
}

</style>
