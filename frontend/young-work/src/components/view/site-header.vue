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
            <button type="button" class="header-btn button-green">Вход</button>
          </li>
          <li class="header-nav__list-item">
            <button type="button" class="header-btn button-green">Регистрация</button>
            <modal-window :show="isModalWinReg"></modal-window>
          </li>
        </ul>
      </nav>
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
      isMenuActive: false,
    }
  },
  methods: {
    openItem() {
      this.isMenuActive = !this.isMenuActive;
    },
  }
}
</script>

<style lang="scss">
@import "../../style/header";
@import "../../style/main";
</style>
