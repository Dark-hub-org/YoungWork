<template>
  <div v-if="isVisible" class="notification" ref="notification">
    <div class="notification__list">
      <div
          v-for="item in items"
          :key="item.text"
          @click.stop="fullText"
          class="notification__item">
        <p class="notification__item-text">{{item.text}}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "the-notification",
  props: {
    isVisible: {
      type: Boolean,
      required: false,
    },
    alertsButton: {
      type: HTMLButtonElement ,
      required: false,
    },
    alertsButtonMobile: {
      type: HTMLDivElement,
      required: false,
    }
  },
  data() {
    return {
      items: [
        {text: "на вашу вакансию откликнулись"},
        {text: "на вашу вакансию откликнулись"},
        {text: "на вашу вакансию откликнулись"}
      ]
    }
  },
  methods: {
    fullText(event) {
      event.currentTarget.classList.toggle('active');
    },
    closeOnOutsideClick(event) {
      const notification = this.$refs.notification
      if(notification && !notification.contains(event.target) && !this.alertsButton.contains(event.target) && !this.alertsButtonMobile.contains(event.target)) {
        this.$emit('close-notification');
      }
    },
    async getNotifications() {
      try {
        const response = await axios.get('/api/not/notes/')
        console.log(response)
      } catch (error) {
        console.log(error)
      }
    }
  },

  mounted() {
    this.getNotifications()
    document.addEventListener('click', this.closeOnOutsideClick);
  },
  beforeDestroy() {
    document.removeEventListener('click', this.closeOnOutsideClick);
  }
}
</script>

<style src="@/style/ui/notifications.scss" lang="scss" scoped>

</style>