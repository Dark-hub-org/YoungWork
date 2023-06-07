<template>
  <button class="button">
    <slot></slot>
  </button>
</template>

<script>
export default {
name: 'button-green',
}
</script>

<style lang="scss" scoped>
@import "src/style/varibles";

.button {
  padding: 15px 25px;
  border-radius: 60px;
  color: $colorWhite;
  background-color: $colorWhite;
}
</style>