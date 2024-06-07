<template>
  <div v-if="isVisible" class="notification" ref="notification">
    <div v-if="notifications.length" class="notification__list">
      <div
          v-for="item in notifications"
          :key="item.id"
          @click="toggleActive(item);"
          :class="{ 'active': item.isActive, 'read': item.is_read }"
          class="notification__item">
        <p class="notification__item-text">{{item.body}}</p>
      </div>
    </div>
    <p v-else >Оповещений нет</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "the-notification",
  props: {
    isVisible: {
      type: Boolean,
      required: true,
    },
    alertsButton: {
      type: HTMLButtonElement ,
      required: false,
    },
  },
  data() {
    return {
      notifications: [],
    }
  },
  methods: {
    async toggleActive(item) {
      try {
        if (!item.is_read) {
          await axios.post(`/api/not/read/${item.id}/`);
          item.is_read = true;
        }
        item.isActive = !item.isActive;
        this.notifications.push()
      } catch (error) {
        console.error(error);
      }
    },
    closeOnOutsideClick(event) {
      const notification = this.$refs.notification
      if(notification && !notification.contains(event.target) && !this.alertsButton.contains(event.target)) {
        this.$emit('close-notification');
      }
    },
    async getNotifications() {
      try {
        const response = await axios.get('/api/not/notes/')
        this.notifications = response.data.reverse()
      } catch (error) {
        console.log(error)
      }
    }
  },

  mounted() {
    if(localStorage.getItem('isAuthorization') !== null) {
      this.getNotifications()
    }
    document.addEventListener('click', this.closeOnOutsideClick);
  },
  beforeDestroy() {
    document.removeEventListener('click', this.closeOnOutsideClick);
  }
}
</script>

<!--<style src="@/style/components/notifications.scss" lang="scss" scoped>-->

<!--</style>-->
