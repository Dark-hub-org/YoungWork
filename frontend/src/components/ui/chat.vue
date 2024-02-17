<template>
  <div class="chat">
    <div class="chat__wrapper">
      <div class="chat__top">
        <span class="chat__title">Чат</span>
        <div class="chat__current-user">
          <div class="chat__current-user-img"></div>
          <div class="chat__current-user-data">
            <p class="chat__current-user-name">Евгений</p>
            <a href="#" class="chat__current-user-link">Дизайнер UI/UX</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'the-chat',
  data() {
    return {

    }
  }
}
</script>

<style src="@/style/ui/chat.scss" lang="scss" scoped>

</style>