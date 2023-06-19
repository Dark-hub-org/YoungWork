<template>
  <div @mousedown="onMouseDown" @mouseup="onMouseUp" @touchstart="onTouchStart" @touchend="onTouchEnd" class="noselect">
    <span @click="goPrev">Prev</span>
    <slider-item
        v-for="(review) in computedData"
        :review="review"
        :key="review.id"
    ></slider-item>
    <span @click="goNext">Next</span>
  </div>
</template>

<script>
import _ from 'lodash'
import SliderItem from "@/components/ui/sliderItem.vue";

export default {
  name: "the-slider",
  props: {
    data: {
      type: Array,
      default() {
        return []
      }
    }
  },
  components: {
    SliderItem,
  },
  data() {
    return {
      currentStep: 0,
      touchstartX: 0,
      touchendX: 0,
    }
  },
  methods: {
    goNext () {
      if (this.currentStep + 1 !== this.data.length) {
        this.currentStep++;
      }
    },
    goPrev () {
      if (this.currentStep > 0) {
        this.currentStep--;
      }
    },
    onTouchStart (e) {
      this.touchstartX = e.changedTouches[0].screenX;
    },
    onTouchEnd (e) {
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
  computed: {
    computedData () {
      return _.filter(this.data, (itm, ind) => {
        return Number(ind) === Number(this.currentStep);
      })
    }
  }
}
</script>

<style scoped>

</style>
