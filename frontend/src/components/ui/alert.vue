<template>
  <div class="alert">
    <span class="alert__text">{{text}}</span>
  </div>
</template>

<script>
export default {
  name: 'the-alert',
  props: {
    text: {
      type: String,
      required: true,
    }
  },
  data() {
    return {

    }
  }
}
</script>

<!--<style src="@/style/components/alert.scss" lang="scss" scoped>-->

<!--</style>-->