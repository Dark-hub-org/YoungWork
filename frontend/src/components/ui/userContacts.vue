<template>
  <div class="profile-contacts">
    <div v-if="userContact.avatar" class="profile-contacts__img-wrapper">
      <div class="profile-contacts__img"></div>
      <div class="profile-contacts__img-control">
        <input type="file" class="profile-contacts__img-input">
      </div>
    </div>
    <h3 class="profile-contacts__subtitle">Контакты</h3>
    <div class="profile-contacts__block">
      <img src="@/assets/telegram-icon.svg" alt="телеграмм иконка" class="profile-contacts__block-img">
      <a :href="'https://t.me/' + userContact.telegram" target="_blank" class="profile-contacts__block-link">
        <template v-if="!userContact.telegram">Не заданно</template>
        <template v-else>@{{userContact.telegram}}</template>
      </a>
    </div>
    <div class="profile-contacts__block">
      <img src="@/assets/email-icon.svg" alt="email иконка" class="profile-contacts__block-img">
      <a :href="'mailto:'+userContact.email" class="profile-contacts__block-link">
        <template v-if="!userContact.email">Не заданно</template>
        <template v-else>{{userContact.email}}</template>
      </a>
    </div>
    <div class="profile-contacts__block">
      <img src="@/assets/telegram-icon.svg" alt="иконка телефона" class="profile-contacts__block-img">
      <a :href="'tel:'+userContact.telephone" class="profile-contacts__block-link">
        <template v-if="userContact.telephone === undefined">Не заданно</template>
        <template v-else>{{userContact.telephone}}</template>
      </a>
    </div>
    <div class="profile-contacts__block">
      <img src="@/assets/link-icon.svg" alt="иконка ссылки" class="profile-contacts__block-img">
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
  computed: {
    // userContacts() {
    //   return {
    //     avatar: this.$store.state.userData.telegram,
    //     telegram: this.$store.state.userData.telegram,
    //     email: this.$store.state.userData.email,
    //     telephone: this.$store.state.userData.telephone,
    //     website: this.$store.state.userData.website,
    //   }
    // }
  },
  mounted() {
    console.log(this.userContact)
  }
}
</script>

<style src="@/style/ui/userContacts.scss" lang="scss" scoped>

</style>