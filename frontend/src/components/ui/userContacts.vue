<template>
  <div class="profile-contacts">
    <div v-if="userContact.logo" class="profile-contacts__img-wrapper">
      <div class="profile-contacts__img"></div>
      <div class="profile-contacts__img-control">
        <input type="file" class="profile-contacts__img-input">
      </div>
    </div>
    <h3 class="profile-contacts__subtitle">Контакты</h3>
    <div class="profile-contacts__block">
      <img src="@/assets/telegram-icon.svg" alt="телеграмм иконка" class="profile-contacts__block-img">
      <a :href="'https://t.me/' + userContact.telegram" target="_blank" class="profile-contacts__block-link">@{{userContact.telegram}}</a>
    </div>
    <div class="profile-contacts__block">
      <img src="@/assets/email-icon.svg" alt="email иконка" class="profile-contacts__block-img">
      <a :href="'mailto:'+userContact.email" class="profile-contacts__block-link">{{userContact.email}}</a>
    </div>
    <div class="profile-contacts__block">
      <img src="@/assets/telegram-icon.svg" alt="иконка телефона" class="profile-contacts__block-img">
      <a :href="'tel:'+userContact.telephone" class="profile-contacts__block-link">{{userContact.telephone}}</a>
    </div>
    <div class="profile-contacts__block">
      <img src="@/assets/link-icon.svg" alt="иконка ссылки" class="profile-contacts__block-img">
      <a :href="userContact.website" target="_blank" class="profile-contacts__block-link">{{userContact.website}}</a>
    </div>
  </div>
</template>

<script>
export default {
  name: 'user-contacts',
  props: {
    userContact: {
      type: Object,
      required: true,
    }
  }
}
</script>

<style src="@/style/ui/userContacts.scss" lang="scss" scoped>

</style>