<template>
  <aside class="applicant-profile__contacts">
    <h3 class="applicant-profile__subtitle">Контакты</h3>
    <div class="applicant-profile__contacts__block">
      <img src="@/assets/telegram-icon.svg" alt="телеграмм иконка" class="applicant-profile__contacts__img">
      <a :href="'https://t.me/' + userContact.telegram" target="_blank" class="applicant-profile__contacts__link">@{{userContact.telegram}}</a>
    </div>
    <div class="applicant-profile__contacts__block">
      <img src="@/assets/email-icon.svg" alt="email иконка" class="applicant-profile__contacts__img">
      <a :href="'mailto:'+userContact.email" class="applicant-profile__contacts__link">{{userContact.email}}</a>
    </div>
    <div class="applicant-profile__contacts__block">
      <img src="@/assets/telegram-icon.svg" alt="иконка телефона" class="applicant-profile__contacts__img">
      <a :href="'tel:'+userContact.telephone" class="applicant-profile__contacts__link">{{userContact.telephone}}</a>
    </div>
    <div class="applicant-profile__contacts__block">
      <img src="@/assets/link-icon.svg" alt="иконка ссылки" class="applicant-profile__contacts__img">
      <a :href="userContact.website" target="_blank" class="applicant-profile__contacts__link">{{userContact.website}}</a>
    </div>
  </aside>
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