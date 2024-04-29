<template>
  <div v-if="isVisible" ref="chat" class="chat">
    <div class="chat__wrapper">
      <button @click="closeChat" class="chat__close">
        <img src="@/assets/close-icon.svg" alt="кнопка закрытия">
      </button>
      <div class="chat__top">
        <span ref="title" class="chat__title">Чат</span>
        <div  ref="currentUser" class="chat__current-user">
          <button @click="returnDialog()" class="chat__return"></button>
          <div class="chat__current-user-img"></div>
          <div class="chat__current-user-data">
            <p class="chat__current-user-name">Евгений</p>
            <a href="#" class="chat__current-user-link">Дизайнер UI/UX</a>
            <p class="chat__current-user-visit">Последний визит: 11.02.2024 в 23:42</p>
          </div>
        </div>
      </div>
      <div class="chat__main">
        <div ref="users" class="chat__main-left">
          <ul class="chat__main-list">
            <li
                v-for="item in dialogList"
                :key="item.id"
                @click="openDialog(item.id)"
                :class="{'active': activeId === item.id}"
                class="chat__main-list__item">
              <div class="chat__main-list__wrapper">
                <div class="chat__main-list__element">
                  <span class="chat__main-list__new-massage">1</span>
                  <button @click="deleteChat(item.id)" class="chat__main-list__delete"></button>
                </div>
                <div class="chat__main-list__image"></div>
                <div class="chat__main-list__info">
                  <p class="chat__main-list__name">{{item.name}}</p>
                  <p class="chat__main-list__massage">{{item.massage}}</p>
                </div>
              </div>
            </li>
          </ul>
        </div>
        <div ref="dialog" class="chat__main-right">
          <div class="chat__main-right__wrapper">
            <div class="chat__main-massage-wrapper another">
              <div class="chat__main-massage__avatar"></div>
              <div class="chat__main-massage">
                <p class="chat__main-massage__text">Отклик на вакансию</p>
                <p class="chat__main-massage__link">10.01.2024, 12:23</p>
              </div>
            </div>
            <div class="chat__main-massage-wrapper">
              <div class="chat__main-massage">
                <p class="chat__main-massage__text">Здравствуйте! Очень понравилось ваше резюме. Хотим пригласить вас на собеседование, по адресу: ул. Профинтернов, 21Б.</p>
                <p class="chat__main-massage__link">10.01.2024, 14:48</p>
              </div>
            </div>
            <div class="chat__main-massage-wrapper another">
              <div class="chat__main-massage__avatar"></div>
              <div class="chat__main-massage">
                <p class="chat__main-massage__text">Здравствуйте! Да, удобно, во сколько подходить?</p>
                <p class="chat__main-massage__link">10.01.2024, 14:55</p>
              </div>
            </div>
            <div class="chat__main-massage-wrapper ">
              <div class="chat__main-massage">
                <p class="chat__main-massage__text">Евгений, удобно на 10?</p>
                <p class="chat__main-massage__link">10.01.2024, 16:55</p>
              </div>
            </div>
            <div class="chat__main-massage-wrapper">
              <div class="chat__main-massage">
                <p class="chat__main-massage__text">Здравствуйте! Очень понравилось ваше резюме. Хотим пригласить вас на собеседование, по адресу: ул. Профинтернов, 21Б.</p>
                <p class="chat__main-massage__link">10.01.2024, 14:48</p>
              </div>
            </div>
            <div class="chat__main-massage-wrapper">
              <div class="chat__main-massage">
                <p class="chat__main-massage__text">Здравствуйте! Очень понравилось ваше резюме. Хотим пригласить вас на собеседование, по адресу: ул. Профинтернов, 21Б.</p>
                <p class="chat__main-massage__link">10.01.2024, 14:48</p>
              </div>
            </div>
          </div>
          <div class="chat__main-send">
            <textarea
                ref="send"
                v-model="massage"
                @input="autoResize"
                class="chat__main-send__input"
                placeholder="Введите ваше сообщение..." >
            </textarea>
            <span v-if="massage.length === 2000" class="chat__main-send__error">Максимальное количество символов</span>
            <button type="button" class="chat__main-send__button"></button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'the-chat',
  props: {
    isVisible: {
      type: Boolean,
      default: false,
    },
    chatButton: {
      type: HTMLButtonElement ,
      required: false,
    },
    chatButtonMobile: {
      type: HTMLDivElement,
      required: false,
    }
  },
  data() {
    return {
      massage: '',
      activeId: null,
      dialogList: [
        {
          id: 1,
          name: 'Екатерина',
          massage: 'Есть опыт разработки больших проектов в команде. Есть опыт разработки'
        },
        {
          id: 2,
          name: 'Екатерина',
          massage: 'Есть опыт разработки больших проектов в команде. Есть опыт разработки'
        },
        {
          id: 3,
          name: 'Екатерина',
          massage: 'Есть опыт разработки больших проектов в команде. Есть опыт разработки'
        },
        {
          id: 4,
          name: 'Екатерина',
          massage: 'Есть опыт разработки больших проектов в команде. Есть опыт разработки'
        },
        {
          id: 5,
          name: 'Екатерина',
          massage: 'Есть опыт разработки больших проектов в команде. Есть опыт разработки'
        },
        {
          id: 6,
          name: 'Екатерина',
          massage: 'Есть опыт разработки больших проектов в команде. Есть опыт разработки'
        },
        {
          id: 7,
          name: 'Екатерина',
          massage: 'Есть опыт разработки больших проектов в команде. Есть опыт разработки'
        },
        {
          id: 8,
          name: 'Екатерина',
          massage: 'Есть опыт разработки больших проектов в команде. Есть опыт разработки'
        },
        {
          id: 9,
          name: 'Екатерина',
          massage: 'Есть опыт разработки больших проектов в команде. Есть опыт разработки'
        },
        {
          id: 10,
          name: 'Екатерина',
          massage: 'Есть опыт разработки больших проектов в команде. Есть опыт разработки'
        },
        {
          id: 11,
          name: 'Екатерина',
          massage: 'Есть опыт разработки больших проектов в команде. Есть опыт разработки'
        },
      ]
    }
  },
  methods: {
    closeChat() {
      this.$emit('close-chat')
    },
    autoResize() {
      this.$refs.send.style.height = 'auto';
      this.$refs.send.style.height = this.$refs.send.scrollHeight + 'px';
      this.$refs.send.scrollTop = 0;
    },
    openDialog(id) {
      if(window.innerWidth <= 769) {
        this.$refs.users.classList.add('hide')
        this.$refs.dialog.classList.add('visible')
        this.$refs.currentUser.classList.add('visible')
        this.$refs.title.style.display = "none";
      }
      this.activeId = id
    },
    deleteChat(id) {
      this.dialogList = this.dialogList.filter(item => item.id !== id)
    },
    returnDialog() {
      this.$refs.users.classList.remove('hide')
      this.$refs.dialog.classList.remove('visible')
      this.$refs.currentUser.classList.remove('visible')
      this.$refs.title.style.display = "block";
    },
    handleClickOutside(event) {
      if (this.isVisible && !this.$refs.chat.contains(event.target) && !this.chatButton.contains(event.target) && !this.chatButtonMobile.contains(event.target)) {
        this.closeChat();
      }
    },
  },
  watch: {
    massage() {
      if(this.massage.length >= 2000) {
        this.massage = this.massage.slice(0, 2000)
      }
    },
    isVisible: {
      handler(val) {
        if(window.innerWidth <= 769) {
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
  mounted() {
    document.addEventListener('click', this.handleClickOutside);
  },
  beforeDestroy() {
    document.removeEventListener('click', this.handleClickOutside);
  }
}
</script>

<style src="@/style/ui/chat.scss" lang="scss" scoped>

</style>