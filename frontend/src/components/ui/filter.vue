<template>
  <div class="vacancy-falters">
    <div
        v-if="screenWidth"
        class="vacancy-filter__top"
    >
      <p class="vacancy-title">Фильтры</p>
      <button
          @click="closeFilters()"
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
        <input type="checkbox" value="fullEmploy" class="vacancy-filter__input" id="employ-1">
        <label for="employ-1" class="vacancy-filter-label check">Полная занятость</label>
      </div>
      <div class="vacancy-filter__block employ">
        <input type="checkbox" value="partialEmploy" class="vacancy-filter__input" id="employ-2">
        <label for="employ-2" class="vacancy-filter-label check">Частичная занятость</label>
      </div>
      <div class="vacancy-filter__block employ">
        <input type="checkbox" value="internship" class="vacancy-filter__input" id="employ-3">
        <label for="employ-3" class="vacancy-filter-label check">Стажировка</label>
      </div>
      <div class="vacancy-filter__block employ">
        <input type="checkbox" value="projectWork" class="vacancy-filter__input" id="employ-4">
        <label for="employ-4" class="vacancy-filter-label check">Проектная работа</label>
      </div>
      <div class="vacancy-filter__block employ">
        <input type="checkbox" value="volunteering" class="vacancy-filter__input" id="employ-5">
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
        class="vacancy-apply button-orange-another">Показать результаты
    </button>
  </div>
</template>

<script>
export default {
  name: 'the-filters',

  data() {
    return {

    }
  },
  methods: {
    closeFilters() {
      this.isFilterVisible = false;
      this.$emit('closeFilters')
    }
  },
  computed: {
    screenWidth() {
      if (window.innerWidth < 1024) {
        return true
      }
      return false
    },
  }
}
</script>

<style src="@/style/ui/filters.scss" lang="scss" scoped>

</style>