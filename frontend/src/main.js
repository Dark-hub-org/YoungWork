import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import CKEditor from 'ckeditor4-vue';
import VueMaskedInput from 'vue-masked-input'
// import io from 'socket.io-client';
// import VueSocketIOExt from 'vue-socket.io-extended';

axios.defaults.baseUrl = "http://127.0.0.1:8080"

// const socket = io('http://127.0.0.1:8080');
Vue.config.productionTip = false
Vue.component('vue-masked-input', VueMaskedInput)
Vue.use(CKEditor);



// Vue.prototype.$socket = socket;

new Vue({
    router,
    store,
    axios,
    render: h => h(App),
}).$mount('#app');