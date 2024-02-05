<template>
  <form class="filters">
    <div class="filters__top">
      <p class="filters__title">Фильтры</p>
      <button
          @click="closeFilters()"
          type="button"
          class="filters__close-btn"></button>
    </div>
    <div class="filters__block">
      <p class="filters__block-title">Уровень дохода</p>
      <div class="filters__item">
        <input v-model="filterParameters.salary" type="radio" value="" name="salary" class="filters__item-input" id="salary-1">
        <label for="salary-1" class="filters__item-label radio">Не имеет значение</label>
      </div>
      <div class="filters__item">
        <input v-model="filterParameters.salary" type="radio" value="25000" name="salary" class="filters__item-input" id="salary-2">
        <label for="salary-2" class="filters__item-label radio">от 25 000 руб.</label>
      </div>
      <div class="filters__item">
        <input v-model="filterParameters.salary" type="radio" value="55000" name="salary" class="filters__item-input" id="salary-3">
        <label for="salary-3" class="filters__item-label radio">от 55 000 руб.</label>
      </div>
      <div class="filters__item">
        <input v-model="filterParameters.salary" type="radio" value="85000" name="salary" class="filters__item-input" id="salary-4">
        <label for="salary-4" class="filters__item-label radio">от 85 000 руб.</label>
      </div>
      <div class="filters__item">
        <input v-model="filterParameters.salary" type="radio" value="145000" name="salary" class="filters__item-input" id="salary-5">
        <label for="salary-5" class="filters__item-label radio">от 145 000 руб.</label>
      </div>
      <div class="filters__item">
        <input v-model="filterParameters.salary" type="radio" value="175000" name="salary" class="filters__item-input" id="salary-6">
        <label for="salary-6" class="filters__item-label radio">от 175 000 руб.</label>
      </div>
      <div class="filters__item">
        <input :checked="isCheckOwnSalary === true" type="radio" name="salary" class="filters__item-input" id="salary-7" @change="handleRadioChange">
        <label for="salary-7" class="filters__item-label radio">Своя зарплата</label>
      </div>
      <input
          v-model="filterParameters.salary"
          @focus="isCheckOwnSalary = true"
          @blur="isCheckOwnSalary = false"
          ref="customSalaryInput"
          type="number"
          placeholder="от"
          class="filters__item-input salary"
          >
    </div>
    <div class="filters__block">
      <p class="filters__block-title">Опыт работы</p>
      <div class="filters__item">
        <input v-model="filterParameters.experience" type="radio" value="Не имеет значения" name="exp" class="filters__item-input" id="exp-1">
        <label for="exp-1" class="filters__item-label radio">Не имеет значения</label>
      </div>
      <div class="filters__item">
        <input v-model="filterParameters.experience" type="radio" value="Нет опыта" name="exp" class="filters__item-input" id="exp-2">
        <label for="exp-2" class="filters__item-label radio">Нет опыта</label>
      </div>
      <div class="filters__item">
        <input v-model="filterParameters.experience" type="radio" value="от 1 года до 3 лет" name="exp" class="filters__item-input" id="exp-3">
        <label for="exp-3" class="filters__item-label radio">от 1 года до 3 лет</label>
      </div>
      <div class="filters__item">
        <input v-model="filterParameters.experience" type="radio" value="От 3 до 6 лет" name="exp" class="filters__item-input" id="exp-4">
        <label for="exp-4" class="filters__item-label radio">От 3 до 6 лет</label>
      </div>
      <div class="filters__item">
        <input v-model="filterParameters.experience" type="radio" value="Более 6 лет" name="exp" class="filters__item-input" id="exp-5">
        <label for="exp-5" class="filters__item-label radio">Более 6 лет</label>
      </div>
    </div>
    <div class="filters__block">
      <p class="filters__block-title">Тип занятости</p>
      <div class="filters__item">
        <input v-model="filterParameters.employ" type="checkbox" value="Полная занятость" class="filters__item-input" id="employ-1">
        <label for="employ-1" class="filters__item-label check">Полная занятость</label>
      </div>
      <div class="filters__item">
        <input v-model="filterParameters.employ" type="checkbox" value="Частичная занятость" class="filters__item-input" id="employ-2">
        <label for="employ-2" class="filters__item-label check">Частичная занятость</label>
      </div>
      <div class="filters__item">
        <input v-model="filterParameters.employ" type="checkbox" value="Стажировка" class="filters__item-input" id="employ-3">
        <label for="employ-3" class="filters__item-label check">Стажировка</label>
      </div>
      <div class="filters__item">
        <input v-model="filterParameters.employ" type="checkbox" value="Проектная работа" class="filters__item-input" id="employ-4">
        <label for="employ-4" class="filters__item-label check">Проектная работа</label>
      </div>
      <div class="filters__item">
        <input v-model="filterParameters.employ" type="checkbox" value="Волонтерство" class="filters__item-input" id="employ-5">
        <label for="employ-5" class="filters__item-label check">Волонтерство</label>
      </div>
    </div>
    <div class="filters__block">
      <p class="filters__block-title">График работы</p>
      <div class="filters__item">
        <input v-model="filterParameters.graph" type="checkbox" class="filters__item-input" id="graph-1" value="Полный день">
        <label for="graph-1" class="filters__item-label check">Полный день</label>
      </div>
      <div class="filters__item">
        <input v-model="filterParameters.graph" type="checkbox" class="filters__item-input" id="graph-2" value="Удаленная работа">
        <label for="graph-2" class="filters__item-label check">Удаленная работа</label>
      </div>
      <div class="filters__item">
        <input v-model="filterParameters.graph" type="checkbox" class="filters__item-input" id="graph-3" value="Сменный график">
        <label for="graph-3" class="filters__item-label check">Сменный график</label>
      </div>
      <div class="filters__item">
        <input v-model="filterParameters.graph" type="checkbox" class="filters__item-input" id="graph-4" value="Гибкий график">
        <label for="graph-4" class="filters__item-label check">Гибкий график</label>
      </div>
      <div class="filters__item">
        <input v-model="filterParameters.graph" type="checkbox" class="filters__item-input" id="graph-5" value="Вахтовый метод">
        <label for="graph-5" class="filters__item-label check">Вахтовый метод</label>
      </div>
    </div>
    <button
        type="submit"
        class="filters__apply button-orange-another">Показать результаты
    </button>
  </form>
</template>

<script>
export default {
  name: 'the-filters',

  data() {
    return {
      filterParameters: {
        salary: '',
        experience: 'Не имеет значения',
        employ: [],
        graph: [],
      },
      isCheckOwnSalary: false,
    }
  },
  methods: {
    closeFilters() {
      this.isFilterVisible = false;
      this.$emit('closeFilters')
    },
    handleRadioChange() {
      this.$refs.customSalaryInput.focus();
    }
  },
  computed: {

  }
}
</script>

<style src="@/style/ui/filters.scss" lang="scss" scoped>

</style>