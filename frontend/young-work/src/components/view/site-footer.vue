<template>
<footer class="footer">
  <div class="wrapper wrapper-footer">
    <ul class="footer-list">
      <li class="footer-list__item">
        <p class="footer-logo">ЛОГО</p>
      </li>
      <li class="footer-list__item">
        <a href="#"><span class="footer-list__item-link">Вакансии</span></a>
        <a href="#"><span class="footer-list__item-link">Отзывы</span></a>
      </li>
      <li class="footer-list__item">
        <a href="#"><span class="footer-list__item-link">Служба поддержки</span></a>
        <a href="#"><span class="footer-list__item-link">О сервисе</span></a>
      </li>
    </ul>
    <div class="footer-bottom">
      <span class="footer-bottom__copy">© 2023 название сайта. Все права защищены.</span>
      <span class="footer-bottom__developers">Сайт разработан КОМАНДА</span>
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
@import "src/style/footer.scss";

</style>
