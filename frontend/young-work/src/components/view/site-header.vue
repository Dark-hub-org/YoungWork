<template>
  <header class="header">
    <div class="wrapper wrapper-header">
      <a href="#" class="header-logo-link">
        <span>Лого</span>
      </a>
      <nav class="header-nav">
        <ul class="header-nav__list">
          <li class="header-nav__list-item">
            <button type="button" class="button-orange">Услуги</button>
          </li>
          <li class="header-nav__list-item">
            <button type="button" class="button-orange">Работа</button>
          </li>
          <li class="header-nav__list-item">
            <button type="button" class="button-green">Вход</button>
          </li>
          <li class="header-nav__list-item">
            <button type="button" class="button-green">Регистрация</button>
            <modal-window></modal-window>
          </li>
        </ul>
      </nav>
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
    }
  },
}
</script>

<style lang="scss">
@import "../../style/header";
@import "../../style/main";
</style>
