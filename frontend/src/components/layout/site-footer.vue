<template>
  <footer class="footer">
    <div class="wrapper footer__wrapper">
      <ul class="footer-list footer__list">
        <li class="footer__list-item">
          <img src="../../assets/logo.svg" alt="логотип" class="footer__logo">
        </li>
        <li class="footer__list-item">
          <a href="/vacancy/" class="footer__list-link">
            Вакансии
          </a>
          <a href="/YoungWork/frontend/static" class="footer__list-link">Отзывы</a>
        </li>
        <li class="footer__list-item">
<!--          <a href="#" class="footer__list-link">Служба поддержки</a>-->
          <a href="/about" class="footer__list-link">О сервисе</a>
        </li>
        <li class="footer__list-item">
          <a href="/agreement" class="footer__list-link">Пользовательское соглашение</a>
          <a href="/privacy" class="footer__list-link">Политика конфиденциальности</a>
        </li>
      </ul>
      <div class="footer__bottom">
        <span class="footer-bottom__copy">© 2024 YoungWork. Все права защищены.</span>
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

<!--<style src="@/style/layout/footer.scss" lang="scss" scoped>-->

<!--</style>-->
