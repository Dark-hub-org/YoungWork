<template>
  <div v-if="isVisible" class="notification" ref="notification">
    <div v-if="notifications.length" class="notification__list">
      <div
          v-for="item in notifications"
          :key="item.id"
          @click.stop="fullText(item, $event)"
          :class="{read: item.is_read}"
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
      notifications: [],
    }
  },
  methods: {
    async fullText(item, event) {
      try {
        if(!item.is_read) {
          await axios.post(`/api/not/read/${item.id}/`)
          this.notifications = this.notifications.map(item => {
            if (item.id === item.id) {
              return { ...item, is_read: true };
            }
            return item;
          });
        }
        event.currentTarget.classList.toggle('active');
      } catch (error) {
        console.log(error)
      }
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
        this.notifications = response.data.reverse()
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