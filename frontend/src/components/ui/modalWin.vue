<template>
  <div
      v-if="show"
      @click.stop="CloseModal"
      class="modal-wrapper">
    <div @click.stop class="modal-window">
      <button
          @click="CloseModal"
          class="modal-window-close">
      </button>
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: 'modalWindow',
  props: {
    show: {
      type: Boolean,
      default: false,
    }
  },
  methods: {
    CloseModal() {
      this.$emit('show', false)
    }
  },
  watch: {
    show: function () {
      if (this.show == true) {
        document.documentElement.style.overflow = 'hidden'
        return;
      }
      document.documentElement.style.overflow = ''
    }
  }
}
</script>

<style lang="scss" scoped>
@import "src/style/ui/modalWin";

</style>
