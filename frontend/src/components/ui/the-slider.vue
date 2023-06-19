<template>
  <div @mousedown="onMouseDown" @mouseup="onMouseUp" @touchstart="onTouchStart" @touchend="onTouchEnd" class="noselect">
    <span @click="goPrev">Prev</span>
    <slot></slot>
    <span @click="goNext">Next</span>
  </div>
</template>

<script>

export default {
  name: "the-slider",
  props: {
    limit: {
      type: Number,
      default: 0,
    }
  },
  data() {
    return {
      currentStep: 0,
      touchstartX: 0,
      touchendX: 0,
    }
  },
  methods: {
    goNext() {
      if (this.currentStep + 1 !== this.limit) {
        this.currentStep++;
        this.$emit('changedStep', this.currentStep)
      }
    },
    goPrev() {
      if (this.currentStep > 0) {
        this.currentStep--;
        this.$emit('changedStep', this.currentStep)
      }
    },
    onTouchStart(e) {
      this.touchstartX = e.changedTouches[0].screenX;
    },
    onTouchEnd(e) {
      this.touchendX = e.changedTouches[0].screenX;
      this.swipeSlider();
    },
    swipeSlider() {
      if (this.touchendX < this.touchstartX) {
        this.goNext();
      }
      if (this.touchendX > this.touchstartX) {
        this.goPrev();
      }
    },
    onMouseUp(e) {
      this.touchendX = e.clientX;
      this.swipeSlider();
    },
    onMouseDown(e) {
      this.touchstartX = e.clientX;
    }

  },
  computed: {}
}
</script>

<style scoped>

</style>
