<template>
  <div v-if="isVisible" ref="chat" class="chat">
    <div class="chat__wrapper">
      <button @click="closeChat" class="chat__close">
        <img src="@/assets/close-icon.svg" alt="кнопка закрытия">
      </button>
      <template v-if="!isLoader">
        <div class="chat__top">
          <span @click="getUser" ref="title" class="chat__title">Чат</span>
          <div v-if="currentDialog?.conversation?.id" ref="currentUser" class="chat__current-user">
            <button @click.stop="returnDialog()" class="chat__return"></button>
            <template v-if="activeInterlocutor.users.length">
              <img v-if="activeInterlocutor.users[0].avatar !== null" class="chat__current-user-img"
                   :src='"/img/" + activeInterlocutor.users[0].avatar' alt="">
              <img v-else class="chat__current-user-img" src="@/assets/header/anonim-logo.svg" alt="">
              <div class="chat__current-user-data">
                <p class="chat__current-user-name">{{ activeInterlocutor.users[0].first_name }}</p>
                <template v-if="currentDialog.vacancy">
                  <router-link
                      :to="{ name: 'vacancy', params: { id: currentDialog.vacancy.id} }"
                      tag="a"
                      target="_blank"
                      class="chat__current-user-link">
                    {{ currentDialog.vacancy.job_title }}
                  </router-link>
                </template>
                <template v-else>
                  <router-link
                      :to="{ name: 'resume', params: { id: currentDialog.resume.id} }"
                      tag="a"
                      target="_blank"
                      class="chat__current-user-link">
                    {{ currentDialog.resume.resume_title }}
                  </router-link>
                </template>
                <p class="chat__current-user-visit">Последний визит: {{ activeInterlocutor.users[0].last_login }}</p>
              </div>
            </template>
            <template v-else>
              <img v-if="activeInterlocutor.history[0].avatar !== null" class="chat__current-user-img"
                   :src='"/img/" + activeInterlocutor.history[0].avatar' alt="">
              <img v-else class="chat__current-user-img" src="@/assets/header/anonim-logo.svg" alt="">
              <div class="chat__current-user-data">
                <p class="chat__current-user-name">{{ activeInterlocutor.history[0].first_name }}</p>
                <p class="chat__current-user-visit">Последний визит: {{ activeInterlocutor.history[0].last_login }}</p>
              </div>
            </template>
          </div>
        </div>
        <div class="chat__main">
          <template v-if="chatsList.length">
            <div ref="users" class="chat__main-left">
              <ul class="chat__main-list">
                <li
                    v-for="item in chatsList"
                    :key="item.id"
                    @click="openDialog(item)"
                    :class="{'active': currentDialog.id === item.id}"
                    class="chat__main-list__item">
                  <div class="chat__main-list__wrapper">
                    <div class="chat__main-list__element">
                      <!--                      <span v-if="item.unread_count" class="chat__main-list__new-massage">{{item.unread_count}}</span>-->
                      <button v-if="userData.usertype === 'employer'" @click.stop="deleteChat(item.id)"
                              class="chat__main-list__delete"></button>
                    </div>
                    <template v-if="item.users.length">
                      <img v-if="item.users[0].avatar !== null" class="chat__main-list__image"
                           :src='"/img/" + item.users[0].avatar' alt="">
                      <img v-else class="chat__main-list__image" src="@/assets/header/anonim-logo.svg" alt="">
                    </template>
                    <template v-else>
                      <img v-if="item.history[0].avatar !== null" class="chat__main-list__image"
                           :src='"/img/" + item.history[0].avatar' alt="">
                      <img v-else class="chat__main-list__image" src="@/assets/header/anonim-logo.svg" alt="">
                    </template>
                    <div class="chat__main-list__info">
                      <template v-if="item.users.length">
                        <p class="chat__main-list__name">{{ item.users[0].first_name }}</p>
                        <p class="chat__main-list__massage">
                          <template v-if="item.last_message?.created_by.id === userData.id">
                            Вы:
                          </template>
                          {{ item.last_message?.body }}
                        </p>
                      </template>
                      <template v-else>
                        <p class="chat__main-list__name">{{ item.history[0].first_name }}</p>
                        <p class="chat__main-list__massage">
                          <template v-if="item.last_message?.created_by.id ===userData.id">
                            Вы:
                          </template>
                          {{ item.last_message.body }}
                        </p>
                      </template>
                    </div>
                  </div>
                </li>
              </ul>
            </div>
            <div ref="dialog" class="chat__main-right">
              <template v-if="currentDialog?.conversation?.id">
                <div class="chat__main-right__wrapper">
                  <p v-if="!activeInterlocutor.users.length" class="chat__main-massage__leave">Работодатель вышел из
                    чата</p>
                  <div
                      v-for="message in currentDialog.conversation.messages"
                      :key="message.id"
                      class="chat__main-massage-wrapper"
                      :class="{'another': userData.id !== message.created_by.id}">
                    <template v-if="userData.id !== message.created_by.id">
                      <img v-if="message.created_by.avatar !== null" class="chat__main-massage__avatar"
                           :src='"/img/" + message.created_by.avatar' alt="аватар">
                      <img v-else class="chat__main-massage__avatar" src="@/assets/header/anonim-logo.svg"
                           alt="анонимный аватар">
                    </template>
                    <div class="chat__main-massage">
                      <p class="chat__main-massage__text">{{ message.body }}</p>
                      <p class="chat__main-massage__link">{{ message.created_at }}</p>
                    </div>
                  </div>
                </div>
                <div class="chat__main-send" :class="{'disabled': !activeInterlocutor.users.length}">
            <textarea
                ref="send"
                v-model="message"
                @input="autoResize"
                @blur="resetStyle"
                @keydown.enter="sendMessage(activeInterlocutor.id, activeInterlocutor.users[0], $event)"
                class="chat__main-send__input"
                :class="{'disabled': !activeInterlocutor.users.length}"
                placeholder="Введите ваше сообщение...">
            </textarea>
                  <span v-if="message.length === 2000"
                        class="chat__main-send__error">Максимальное количество символов</span>
                  <button @click="sendMessage(activeInterlocutor.id, activeInterlocutor.users[0], $event)" type="submit"
                          class="chat__main-send__button"></button>
                </div>
              </template>
              <template v-else>
                <span class="chat__main-right__choice">Выберите чат, чтобы начать диалог</span>
              </template>
            </div>
          </template>
          <template v-else>
            <div class="chat__main-empty">
              <p class="chat__main-empty__title">Сообщений пока нет</p>
              <a class="button-orange" href="/vacancy">Перейти к вакансиям</a>
            </div>
          </template>
        </div>
      </template>
      <the-loader :is-visible="isLoader"></the-loader>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import TheLoader from "@/components/ui/loader.vue";

export default {
  name: 'the-chat',
  components: {TheLoader},
  props: {
    isVisible: {
      type: Boolean,
      default: false,
    },
    chatButton: {
      type: HTMLButtonElement,
      required: false,
    },
  },
  data() {
    return {
      message: '',
      activeInterlocutor: null,
      chatsList: [],
      currentDialog: [],
      lastMessages: '',
      intervalChat: null,
      isLoader: true,
      socket: null,
    }
  },
  methods: {
    closeChat() {
      this.$emit('close-chat')
      // this.isLoader = true
    },
    handleClickOutside(event) {
      if (this.isVisible && !this.$refs.chat.contains(event.target) && !this.chatButton.contains(event.target)) {
        this.closeChat();
      }
    },
    async getChats() {
      try {
        if (this.isVisible) {
          const response = await axios.get('/api/chat/can')
          this.chatsList = response.data
          this.isLoader = false
        }
      } catch (error) {
        console.log(error)
      }
    },
    async openDialog(user) {
      try {
        if (this.currentDialog.conversation?.id !== user.id) {
          const chat = await axios.get(`/api/chat/${user.id}/${user.users[0].id}/${this.userData.usertype}/`)
          this.readItMessage(chat.data.conversation.messages)
          this.currentDialog = chat.data
          this.activeInterlocutor = user
          if (window.innerWidth <= 769) {
            this.$refs.users.classList.add('hide')
            this.$refs.dialog.classList.add('visible')
            this.$refs.title.style.display = "none";
          }
        }
      } catch (error) {
        console.log(error)
      }
    },
    async readItMessage(messages) {
      try {
        return messages.map(item => item.is_read = true).reverse()
      } catch (error) {
        console.log(error)
      }

    },
    async sendMessage(id, user, event) {
      try {
        if (this.message.length && !event.shiftKey && this.activeInterlocutor.users.length) {
          event.preventDefault()
          await axios.post(`/api/chat/${id}/send/`, {body: this.message})
          const chat = await axios.get(`/api/chat/${id}/${user.id}/${this.userData.usertype}/`)
          chat.data.conversation.messages = chat.data.conversation.messages.reverse()
          this.currentDialog = chat.data
          this.message = ''
          this.resetStyle()
        }
      } catch (error) {
        console.log(error)
      }
    },
    autoResize() {
      this.$refs.send.style.height = 'auto';
      this.$refs.send.style.height = this.$refs.send.scrollHeight + 'px';
      this.$refs.send.scrollTop = 0;
    },
    resetStyle() {
      if (!this.message.length) {
        this.$refs.send.style = '';
      }
    },
    async deleteChat(id) {
      try {
        await axios.delete(`/api/chat/${id}/remove/`)
        this.chatsList = this.chatsList.filter(item => item.id !== id)
        this.currentDialog = []
      } catch (error) {
        console.log(error)
      }
    },
    returnDialog() {
      this.$refs.users.classList.remove('hide')
      this.$refs.dialog.classList.remove('visible')
      this.$refs.title.style.display = "block";
      this.activeInterlocutor = null;
      this.currentDialog = []
    },
    getUser() {
      this.socket.send(JSON.stringify({
        action: "list",
        request_id: new Date().getTime()
      }))
    }
  },
  computed: {
    userData() {
      return this.$store.state.userData
    },
    userToken() {
      return localStorage.getItem('access')
    }
  },
  watch: {
    message() {
      if (this.message.length >= 2000) {
        this.message = this.message.slice(0, 2000)
      }
    },
    isVisible: {
      handler(val) {
        if (window.innerWidth <= 769) {
          if (val) {
            document.body.style.overflow = 'hidden'
            document.body.classList.add('manual-overflow-padding')
            return;
          }
          this.$nextTick(() => {
            let wrapper = this.$refs.chat
            if (!wrapper) {
              document.body.style.overflow = ''
              document.body.classList.remove('manual-overflow-padding')
            }
          })
        }
      },
      immediate: true,
    }
  },
  created() {
    this.socket = new WebSocket('ws://127.0.0.1:8000/ws/?token=' + this.userToken);
  },
  mounted() {
    document.addEventListener('click', this.handleClickOutside);
    if (localStorage.getItem('isAuthorization'))
      this.intervalChat = setInterval(this.getChats, 1000)
  },
  beforeDestroy() {
    document.removeEventListener('click', this.handleClickOutside);
    clearInterval(this.intervalChat);
  }
}
</script>

<style src="@/style/ui/chat.scss" lang="scss" scoped>

</style>