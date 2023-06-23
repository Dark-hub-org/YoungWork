<template>
  <main class="main">
    <router-view></router-view>
  </main>
</template>
<script>
export default {
  name: "site-content"
}
</script>

<style lang="scss" scoped>
@import "@/style/main";

.main {
  margin-bottom: 158px;
}

</style>
