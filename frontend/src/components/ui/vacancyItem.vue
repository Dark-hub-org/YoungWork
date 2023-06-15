<template>
  <div class="vacancy-card">
    <p class="vacancy-card__title">{{vacancy.title}}</p>
    <ul class="vacancy-card__list">
      <li class="vacancy-card-list__item">
         <span>Требования:</span>{{vacancy.requirements}}
      </li>
      <li class="vacancy-card-list__item">
          <span>Задачи:</span>{{vacancy.tasks}}
      </li>
      <li class="vacancy-card-list__item">
          <span>Оплата:</span> {{vacancy.salary}}
      </li>
    </ul>
    <div class="vacancy-btns">
      <button type="button" class="vacancy-btns-respond button-orange-another">Откликнуться</button>
      <button type="button" class="vacancy-btns-favourites button-orange">В избранное</button>
    </div>
  </div>
</template>

<script>
export default {
name: 'vacancy-item',
  props: {
    vacancy: {
      type: Object,
      required: true,
    }
  }
}
</script>

<style lang="scss" scoped>

@import "src/style/ui/vacancyItem";

</style>
