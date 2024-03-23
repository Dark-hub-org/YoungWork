<template>
  <div class="vacancy-card">
    <p class="vacancy-card__title">{{ vacancy.job_title }}</p>
    <ul class="vacancy-card__list">
      <li class="vacancy-card__item">
        <span class="vacancy-card__signature">Требования:</span>
        <span class="vacancy-card__text"> {{ vacancy.requirements }}</span>
      </li>
      <li class="vacancy-card__item">
        <span class="vacancy-card__signature">Задачи:</span>
        <span class="vacancy-card__text"> {{ vacancy.tasks }}</span>
      </li>
      <li class="vacancy-card__item">
        <span class="vacancy-card__signature">Оплата:</span>
        <span v-if="vacancy.salary_min || vacancy.salary_max" class="vacancy-card__text">
          <template
              v-if="vacancy.salary_min && vacancy.salary_max">
            от {{ vacancy.salary_min }} до {{ vacancy.salary_max }}
          </template>
          <template v-else-if="vacancy.salary_min">от {{ vacancy.salary_min }}</template>
          <template v-else>до {{ vacancy.salary_max }}</template>
          рублей
        </span>
      </li>
    </ul>
    <div class="vacancy-card__btns">
      <template v-if="userData.usertype === 'applicant'">
        <button
            v-if="!vacancy.response"
            @click="sendResponse(vacancy)"
            type="button"
            class="vacancy-card__response button-orange-another">
          Откликнуться
        </button>
        <span v-else class="button-orange vacancy__item-btn">Откликнулись</span>
        <button
            v-if="!vacancy.favorite"
            @click="addedFavorites(vacancy.id)"
            type="button"
            class="vacancy-card__favourites button-orange">
          В избранное
        </button>
        <span v-else class="button-orange vacancy__item-btn">В избранном</span>
      </template>
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
  },
  data() {
    return {

    }
  },
  methods: {
    sendResponse(vacancy) {
      const data = {
        vacancy: vacancy.id,
        org: vacancy.created_by,
        created_by: this.userData.usertype,
      }
      this.$emit('added-vacancy', data, vacancy)
    },

    addedFavorites(id) {
      this.$emit('added-favorite', id)
    },
  },
  computed: {
    userData() {
      return this.$store.state.userData
    },
  }
}
</script>

<style src="@/style/ui/vacancyItem.scss" lang="scss" scoped>

</style>
