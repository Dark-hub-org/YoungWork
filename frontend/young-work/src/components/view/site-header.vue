<template>
  <header class="header">
    <div class="wrapper">
      <a href="#" class="header-logo-link">
        <span>Лого</span>
      </a>
      <nav class="header-nav">
        <ul class="header-nav__list">
          <li class="header-nav__list-item">

          </li>
          <li class="header-nav__list-item">

          </li>
          <li class="header-nav__list-item">

          </li>
          <li class="header-nav__list-item">

          </li>
        </ul>
      </nav>

      <site-button-green>
        Hello
      </site-button-green>

      <site-button-orange>
        Hi
      </site-button-orange>
    </div>
  </header>

</template>

<script>
import siteButtonOrange from '../ui/site-button-orange';
import siteButtonGreen from '../ui/site-button-green'
export default {
  name: 'site-header',
  components: {
    siteButtonOrange,
    siteButtonGreen
  }
}
</script>

<style lang="scss">
@import "../../style/header";
@import "../../style/main";
</style>
