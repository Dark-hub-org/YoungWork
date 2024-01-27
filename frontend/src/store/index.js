import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        isAuthorization: false,
        userData: {},
        userId: '',
        access: '',
        refresh: '',
        isProfileEdit: false,
    },
    mutations: {
        initializeStore(state) {
            if (localStorage.getItem("access")) {
                state.userId = localStorage.getItem("id")
                state.access = localStorage.getItem("access")
                state.refresh = localStorage.getItem("refresh")
            } else {
                state.userId = ''
                state.access = ''
                state.refresh = ''
            }
        },
        setUserData(state, data) {
          state.userData = data
        },
        changeAuthorization(state, value) {
            state.isAuthorization = value
            localStorage.setItem('isAuthorization', value)
        },
        setId(state, id) {
            state.userId = id
            localStorage.setItem('id', id)
        },
        setAccess(state, access) {
            state.access = access
            localStorage.setItem('access', access)
        },
        setRefresh(state, refresh) {
            state.refresh = refresh
            localStorage.setItem('refresh', refresh)
        },
        editISProfileEdit(state, newVal) {
            state.isProfileEdit = newVal
        },
    },
    actions: {},
    getters: {},
    modules: {}
})
