<template>
  <div class="profile-contacts">
    <h3 class="profile-contacts__subtitle">Контакты</h3>
    <div class="profile-contacts__block">
      <img src="../../assets/telegram-icon.svg" alt="телеграмм иконка" class="profile-contacts__block-img">
      <a :href="'https://t.me/' + userContact.telegram" target="_blank" class="profile-contacts__block-link">
        <template v-if="!userContact.telegram">Не заданно</template>
        <template v-else>@{{userContact.telegram}}</template>
      </a>
    </div>
    <div class="profile-contacts__block">
      <img src="../../assets/email-icon.svg" alt="email иконка" class="profile-contacts__block-img">
      <a :href="'mailto:'+userContact.email" class="profile-contacts__block-link">
        <template v-if="!userContact.email">Не заданно</template>
        <template v-else>{{userContact.email}}</template>
      </a>
    </div>
    <div class="profile-contacts__block">
      <img src="../../assets/phone-icon.svg" alt="иконка телефона" class="profile-contacts__block-img">
      <a :href="'tel:'+userContact.phoneNumber" class="profile-contacts__block-link">
        <template v-if="userContact.phoneNumber === undefined">Не заданно</template>
        <template v-else>{{userContact.phoneNumber}}</template>
      </a>
    </div>
    <div class="profile-contacts__block">
      <img src="../../assets/link-icon.svg" alt="иконка ссылки" class="profile-contacts__block-img">
      <a :href="userContact.website" target="_blank" class="profile-contacts__block-link">
        <template v-if="!userContact.website">Не заданно</template>
        <template v-else>{{userContact.website}}</template>
      </a>
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
  },
  data() {
    return {
    }

  },
}
</script>

<!--<style src="@/style/components/userContacts.scss" lang="scss" scoped>-->

<!--</style>-->