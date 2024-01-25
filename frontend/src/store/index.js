import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        id: '',
        access: '',
        refresh: '',
        isProfileEdit: false,
    },
    mutations: {
        initializeStore(state) {
            if (localStorage.getItem("access")) {
                state.id = localStorage.getItem("id")
                state.access = localStorage.getItem("access")
                state.refresh = localStorage.getItem("refresh")
            } else {
                state.id = ''
                state.access = ''
                state.refresh = ''
            }
        },
        setId(state, id) {
            state.id = id
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
