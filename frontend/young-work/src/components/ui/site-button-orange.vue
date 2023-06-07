<template>
  <button class="button">
    <slot></slot>
  </button>
</template>

<script>
export default {
  name: 'button-orange',
}
</script>

<style lang="scss" scoped>
@import "src/style/varibles";

.button {
  padding: 15px 25px;
  border: 1px solid $colorOrangeM;
  border-radius: 60px;
  color: $colorOrangeM;
}

</style>