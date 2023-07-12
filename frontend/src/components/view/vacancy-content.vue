<template>
  <main>
    <section class="inner">
      <div class="wrapper wrapper-inner">
        <h1 class="inner-title">Сервис по поиску работы для подростков </h1>
        <div class="inner-slider">
          <div class="inner-slider__item">
            <img src="@/assets/vacancy/vacancy-1.png" alt="it профессии" class="slider-item__img">
            <div class="inner-slider__content">
              <router-link
                  to="/"
                  tag="a"
                  active-class="active"
                  class="button-orange-another slider-item__link">
                   Перейти
              </router-link>
              <h3 class="inner-slider__title" >IT-профессии</h3>
            </div>
          </div>
          <div class="inner-slider__item">
            <img src="@/assets/vacancy/vacancy-2.png" alt="строительные профессии" class="slider-item__img">
            <div class="inner-slider__content">
              <router-link
                  to="/"
                  tag="a"
                  active-class="active"
                  class="button-orange-another slider-item__link">
                   Перейти
              </router-link>
              <h5 class="inner-slider__title white" >Строительные профессии</h5>
            </div>
          </div>
          <div class="inner-slider__item">
            <img src="@/assets/vacancy/vacancy-3.png" alt="работа с детьми" class="slider-item__img">
            <div class="inner-slider__content">
              <router-link
                  to="/"
                  tag="a"
                  active-class="active"
                  class="button-orange-another slider-item__link">
                   Перейти
              </router-link>
              <h5 class="inner-slider__title white">Работа с детьми</h5>
            </div>
          </div>
        </div>
        <div class="inner-search">
          <div class="inner-search__wrapper">
            <input type="text" class="inner-search__input" placeholder="найти вакансию">
            <button type="button" class="inner-search__btn"></button>
          </div>
            <button
            v-if="screenWidth"
            @click="isFilterVisible = true"
            type="button"
            class="inner-filter-btn">
              <span class="text">Фильтр</span>
            </button>
        </div>
    </div>
  </section>
  <section class="vacancy">
    <div class="wrapper vacancy-wrapper">
      <h3 class="vacancy-quantity">32 вакансии “Дизайнер интерфейсов”</h3>
      <div class="vacancy-filter-and-list">
        <template>
          <div class="vacancy-falters" :class="{active: isFilterVisible}">
            <div
            v-if="screenWidth"
            class="vacancy-filter__top"
            >
              <h4 class="vacancy-title">Фильтры</h4>
              <button
              @click="isFilterVisible = false"
              type="button"
              class="filter-close-btn"></button>
            </div>
            <div class="vacancy-filter__wrapper">
              <p class="vacancy-filter__title">Уровень дохода</p>
              <div class="vacancy-filter__block">
                <input type="radio" value="25000" name="salary" class="vacancy-filter__input" id="salary-1">
                <label for="salary-1" class="vacancy-filter-label radio">от 25 000 руб.</label>
              </div>
              <div class="vacancy-filter__block">
                <input type="radio" value="25000" name="salary" class="vacancy-filter__input" id="salary-2">
                <label for="salary-2" class="vacancy-filter-label radio">от 25 000 руб.</label>
              </div>
              <div class="vacancy-filter__block">
                <input type="radio" value="55000" name="salary" class="vacancy-filter__input" id="salary-3">
                <label for="salary-3" class="vacancy-filter-label radio">от 55 000 руб.</label>
              </div>
              <div class="vacancy-filter__block">
                <input type="radio" value="85000" name="salary" class="vacancy-filter__input" id="salary-4">
                <label for="salary-4" class="vacancy-filter-label radio">от 85 000 руб.</label>
              </div>
              <div class="vacancy-filter__block">
                <input type="radio" value="145000" name="salary" class="vacancy-filter__input" id="salary-5">
                <label for="salary-5" class="vacancy-filter-label radio">от 145 000 руб.</label>
              </div>
              <div class="vacancy-filter__block">
                <input type="radio" value="175000" name="salary" class="vacancy-filter__input" id="salary-6">
                <label for="salary-6" class="vacancy-filter-label radio">от 175 000 руб.</label>
              </div>
              <input type="text" placeholder="от" class="vacancy-filter__input">
              <div class="vacancy-filter__block">
                <input type="radio" value="" name="salary" class="vacancy-filter__input" id="salary-7">
                <label for="salary-7" class="vacancy-filter-label radio">Доход указан</label>
              </div>
            </div>
            <div class="vacancy-filter__wrapper">
              <p class="vacancy-filter__title">Образование</p>
              <div class="vacancy-filter__block">
                <input type="checkbox" class="vacancy-filter__input" id="educ-1">
                <label for="educ-1" class="vacancy-filter-label check">Не требуется или не указано</label>
              </div>
              <div class="vacancy-filter__block">
                <input type="checkbox" class="vacancy-filter__input" id="educ-2">
                <label for="educ-2" class="vacancy-filter-label check">Среднее профессиональное</label>
              </div>
              <div class="vacancy-filter__block">
                <input type="checkbox" class="vacancy-filter__input" id="educ-3">
                <label for="educ-3" class="vacancy-filter-label check">Высшее</label>
              </div>
            </div>
            <div class="vacancy-filter__wrapper">
              <p class="vacancy-filter__title">Опыт работы</p>
              <div class="vacancy-filter__block exp">
                <input type="radio" value="" name="exp" class="vacancy-filter__input" id="exp-1">
                <label for="exp-1" class="vacancy-filter-label radio">Не имеет значения</label>
              </div>
              <div class="vacancy-filter__block exp">
                <input type="radio" value="" name="exp" class="vacancy-filter__input" id="exp-2">
                <label for="exp-2" class="vacancy-filter-label radio">Нет опыта</label>
              </div>
              <div class="vacancy-filter__block exp">
                <input type="radio" value="" name="exp" class="vacancy-filter__input" id="exp-3">
                <label for="exp-3" class="vacancy-filter-label radio">от 1 года до 3 лет</label>
              </div>
              <div class="vacancy-filter__block exp">
                <input type="radio" value="" name="exp" class="vacancy-filter__input" id="exp-4">
                <label for="exp-4" class="vacancy-filter-label radio">От 3 до 6 лет</label>
              </div>
              <div class="vacancy-filter__block exp">
                <input type="radio" value="" name="exp" class="vacancy-filter__input" id="exp-5">
                <label for="exp-5" class="vacancy-filter-label radio">Более 6 лет</label>
              </div>
            </div>
            <div class="vacancy-filter__wrapper">
              <p class="vacancy-filter__title">Тип занятости</p>
              <div class="vacancy-filter__block employ">
                <input type="checkbox" class="vacancy-filter__input" id="employ-1">
                <label for="employ-1" class="vacancy-filter-label check">Полная занятость</label>
              </div>
              <div class="vacancy-filter__block employ">
                <input type="checkbox" class="vacancy-filter__input" id="employ-2">
                <label for="employ-2" class="vacancy-filter-label check">Частичная занятость</label>
              </div>
              <div class="vacancy-filter__block employ">
                <input type="checkbox" class="vacancy-filter__input" id="employ-3">
                <label for="employ-3" class="vacancy-filter-label check">Стажировка</label>
              </div>
              <div class="vacancy-filter__block employ">
                <input type="checkbox" class="vacancy-filter__input" id="employ-3">
                <label for="employ-4" class="vacancy-filter-label check">Проектная работа</label>
              </div>
              <div class="vacancy-filter__block employ">
                <input type="checkbox" class="vacancy-filter__input" id="employ-3">
                <label for="employ-5" class="vacancy-filter-label check">Волонтерство</label>
              </div>
            </div>
            <div class="vacancy-filter__wrapper">
              <p class="vacancy-filter__title">График работы</p>
              <div class="vacancy-filter__block employ">
                <input type="checkbox" class="vacancy-filter__input" id="graph-1">
                <label for="graph-1" class="vacancy-filter-label check">Полный день</label>
              </div>
              <div class="vacancy-filter__block employ">
                <input type="checkbox" class="vacancy-filter__input" id="graph-2">
                <label for="graph-2" class="vacancy-filter-label check">Удаленная работа</label>
              </div>
              <div class="vacancy-filter__block employ">
                <input type="checkbox" class="vacancy-filter__input" id="graph-3">
                <label for="graph-3" class="vacancy-filter-label check">Сменный график</label>
              </div>
              <div class="vacancy-filter__block employ">
                <input type="checkbox" class="vacancy-filter__input" id="graph-4">
                <label for="graph-4" class="vacancy-filter-label check">Гибкий график</label>
              </div>
              <div class="vacancy-filter__block employ">
                <input type="checkbox" class="vacancy-filter__input" id="graph-5">
                <label for="graph-5" class="vacancy-filter-label check">Вахтовый метод</label>
              </div>
            </div>
            <button
            v-if="screenWidth"
            type="button"
            class="vacancy-apply button-orange-another">Показать результаты</button>
          </div>
        </template>
        <div class="vacancy-list">
          <div class="vacancy-item">
            <div class="vacancy-item__header">
              <div class="vacancy-item__block">
                <p class="vacancy-item__title">Дизайнер интерфейсов</p>
                <p class="vacancy-item__salary">35 000 рублей</p>
              </div>
              <img src="@/assets/vacancy/company-logo.svg" alt="логотип компании">
            </div>
            <div class="vacancy-item__info">
              <div class="vacancy-item__block">
                  <p class="vacancy-item__text vacancy-item__company">ООО ЦТД</p>
                  <p class="vacancy-item-text">Владивосток</p>
                </div>
                <div class="vacancy-item__block">
                  <p class="vacancy-item__text">Опыт работы: не имеет значения</p>
                  <p class="vacancy-item__text vacancy-item__experince">Частичная занятость</p>
                </div>
                <div class="vacancy-item__block">
                  <p class="vacancy-item__text"><span class="vacancy-item__subtitle">Задачи:</span> разработка макетов и адаптивов, упаковка готовых решений в презентации.</p>
                  <p class="vacancy-item__text"><span class="vacancy-item__subtitle">Требования:</span> хорошее понимание UI/UX базы; понимание всех нюансов разработки современных сайтов.</p>
              </div>
            </div>
            <div class="vacancy-item__btns">
              <button class="button-orange-another">Откликнуться</button>
              <button class="button-orange">В избранное</button>
            </div>
          </div>
          <div class="vacancy-list__pagination">
            <button class="vacancy-list__page">1</button>
          </div>
        </div>
      </div>
    </div>
  </section>
  </main>
</template>

<script>

export default {
name: 'vacancy-content',

  data() {
    return {
      isFilterVisible: false,
    }
  },
  computed: {
    screenWidth() {
      if(window.innerWidth < 1024) {
        return true
      }
      return false
    },
    // paginationQuantity() {
    //   return 
    // }
  }
}

</script>

<style src="@/style/vacancy.scss" lang="scss" scoped>

</style>