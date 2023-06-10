<template>
  <div class="reviews-slider__item">
    <p class="slider-item__title">{{review.title}}</p>
    <p class="slider-item-text">{{review.text}}</p>
    <div class="slider-item-person">
      <img src="" alt="работадатель" class="slider-item-person-image">
      <div class="slider-item-person__info">
        <p class="slider-item-person__info-name">{{review.name}}</p>
        <p class="slider-item-person__info-post">{{review.post}}</p>
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

<style lang="scss" scoped>
@import "src/style/ui/sliderItem";
</style>