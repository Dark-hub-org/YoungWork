import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './style/main.scss'
import axios from 'axios'

axios.defaults.baseUrl = 'http://127.0.0.1:8080'

Vue.config.productionTip = false

new Vue({
    router,
    store,
    axios,
    render: h => h(App)
}).$mount('#app')
