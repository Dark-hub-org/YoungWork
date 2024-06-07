<template>
  <div
      v-if="isVisible"
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
    isVisible: {
      type: Boolean,
      default: false,
    }
  },
  methods: {
    CloseModal() {
      this.$emit('close', false)
    }
  },
  watch: {
    isVisible: {
      handler(val) {
        if (val) {
          document.body.style.overflow = 'hidden'
          document.body.classList.add('manual-overflow-padding')
          return;
        }
        this.$nextTick(() => {
          let wrapper = document.getElementById('modal-wrapper')
          if (!wrapper) {
            document.body.style.overflow = ''
            document.body.classList.remove('manual-overflow-padding')
          }
        })
      },
      immediate: true,
    }
  }
}
</script>

<!--<style src="@/style/components/modalWin.scss" lang="scss" scoped>-->

<!--</style>-->