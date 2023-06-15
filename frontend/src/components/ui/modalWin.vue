<template>
  <div
      v-if="show"
      @click.stop="CloseModal"
      class="modal-wrapper" id="modal-wrapper">
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
    show: {
      handler(val) {
        if (val) {
          document.body.style.overflow = 'hidden'
          return;
        }
        this.$nextTick(() => {
          let wrapper = document.getElementById('modal-wrapper')
          if (!wrapper) {
            document.body.style.overflow = ''
          }
        })
      },
      immediate: true,
    }
  }
}
</script>

<style lang="scss" scoped>
@import "src/style/ui/modalWin";

</style>
