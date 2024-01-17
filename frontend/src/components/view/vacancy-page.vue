<template>
  <section class="vacancy">
    <div class="wrapper vacancy-wrapper">
      <h1 class="inner-title">Сервис по поиску работы для подростков </h1>
      <div class="vacancy-item">
        <div class="vacancy-item__info">
          <div class="vacancy-item__block">
            <p class="vacancy-item__title">Дизайнер интерфейсов</p>
            <p class="vacancy-item__salary">35 000 рублей</p>
          </div>
          <div class="vacancy-item__block">
            <p class="vacancy-item__text">Опыт работы: не имеет значения</p>
            <p class="vacancy-item__text">Частичная занятость</p>
            <p class="vacancy-item__text response">Сейчас эту вакансию смотрят 3 человека</p>
          </div>
          <div class="vacancy-item__btns">
            <button class="vacancy-btn button-orange-another">Откликнуться</button>
            <button class="vacancy-btn button-orange">В избранное</button>
          </div>
        </div>
        <div class="vacancy-item__employer">
          <img src="@/assets/vacancy/company-logo.svg" alt="логотип компании" class="vacancy-item__img">
          <p class="vacancy-item__company">ООО ЦТД</p>
          <p class="vacancy-item__text vacancy-item__addres">Владивосток, ул. Ленина, 25</p>
          <p class="vacancy-item__text vacancy-item__phone">8(999)888-77-66</p>
          <p class="vacancy-item__text vacancy-item__hr">HR, Самохина Людмила</p>
        </div>
      </div>
      <div class="vacancy-info">
        <div class="vacancy-info__block">
          <p class="vacancy-info__title">О компании/ заказчике:</p>
          <p class="vacancy-info__text">Рыбатекст используется дизайнерами, проектировщиками
            и фронтендерами, когда нужно быстро заполнить макеты или прототипы содержимым. Это тестовый контент, который
            не должен нести никакого смысла, лишь показать наличие самого текста или продемонстрировать типографику в
            деле.</p>
        </div>
        <div class="vacancy-info__block">
          <p class="vacancy-info__title">Обязанности:</p>
          <p class="vacancy-info__text">Рыбатекст используется дизайнерами, проектировщиками
            и фронтендерами, когда нужно быстро заполнить макеты или прототипы содержимым. Это тестовый контент, который
            не должен нести никакого смысла, лишь показать наличие самого текста или продемонстрировать типографику в
            деле.</p>
        </div>
        <div class="vacancy-info__block">
          <p class="vacancy-info__title">Требования:</p>
          <p class="vacancy-info__text">Рыбатекст используется дизайнерами, проектировщиками
            и фронтендерами, когда нужно быстро заполнить макеты или прототипы содержимым. Это тестовый контент, который
            не должен нести никакого смысла, лишь показать наличие самого текста или продемонстрировать типографику в
            деле.</p>
        </div>
        <div class="vacancy-info__block">
          <p class="vacancy-info__title">Условия:</p>
          <p class="vacancy-info__text">Рыбатекст используется дизайнерами, проектировщиками
            и фронтендерами, когда нужно быстро заполнить макеты или прототипы содержимым. Это тестовый контент, который
            не должен нести никакого смысла, лишь показать наличие самого текста или продемонстрировать типографику в
            деле.</p>
        </div>
        <p class="vacancy-info__date">Вакансия была опубликована сегодня, 16:25</p>
        <button class="button-orange-another">Откликнуться</button>
      </div>
      <div class="vacancy-recomendated">
        <h3 class="section-title">Рекомендуем вам</h3>
      </div>
    </div>
  </section>
</template>
<script>
export default {
  name: 'vacancy-page',
  props: ['id'],
  data() {
    return {

    };
  },
  mounted() {

  },
}
</script>
<style src="@/style/vacancy-page.scss" lang="scss" scoped>

</style>