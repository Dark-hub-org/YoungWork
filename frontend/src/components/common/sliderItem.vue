<template>
  <div class="slider__item">
    <p class="slider__item-title">{{ review.title }}</p>
    <p class="slider__item-text">{{ review.text }}</p>
    <div class="slider__item-person">
      <img :src="require(`../../assets/reviews/${review.src}`)" alt="работадатель" class="slider__item-person__image">
      <div class="slider__item-person__info">
        <p class="slider__item-person__name">{{ review.name }}</p>
        <p class="slider__item-person__post">{{ review.post }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "slider-item",
  props: {
    review: {
      type: Object,
      required: true,
    }
  }
}
</script>