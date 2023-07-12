<template>
  <footer class="footer">
    <div class="wrapper wrapper-footer">
      <ul class="footer-list">
        <li class="footer-list__item">
          <img src="@/assets/logo.svg" alt="логотип" class="header-logo">
        </li>
        <li class="footer-list__item">
          <a href="#" class="footer-list__item-link"><span class="footer-list__item-text">Вакансии</span></a>
          <a href="#" class="footer-list__item-link"><span class="footer-list__item-text">Отзывы</span></a>
        </li>
        <li class="footer-list__item">
          <a href="#" class="footer-list__item-link"><span class="footer-list__item-text">Служба поддержки</span></a>
          <a href="#" class="footer-list__item-link"><span class="footer-list__item-text">О сервисе</span></a>
        </li>
      </ul>
      <div class="footer-bottom">
        <span class="footer-bottom__copy">© 2023 YoungWork. Все права защищены.</span>
        <span class="footer-bottom__developers">Сайт разработан Dark Hub</span>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: "site-footer"
}
</script>

<style lang="scss">
@import "@/style/footer";

</style>
