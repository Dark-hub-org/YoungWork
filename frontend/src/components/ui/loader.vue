<template>
  <div v-if="isVisible" class="loader">
    <div class="loader__spinner"></div>
  </div>
</template>

<script>
export default {
  name: "the-loader",
  props: {
    isVisible: {
      type: Boolean,
      default: false,
    }
  }
}
</script>

<style src="@/style/ui/loader.scss" scoped lang="scss">

</style>