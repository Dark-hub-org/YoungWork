import Vue from 'vue'
import Vuex from 'vuex'
import axios from "axios";

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        isAuthorization: false,
        userData: {},
        access: '',
        refresh: '',
        searchValue: '',
        isProfileEdit: false,
    },
    mutations: {
        initializeStore(state) {
            if (localStorage.getItem("access")) {
                state.access = localStorage.getItem("access")
                state.refresh = localStorage.getItem("refresh")
            } else {
                state.access = ''
                state.refresh = ''
            }
        },
        setSearchValue(state, value) {
            state.searchValue = value
        },
        setUserData(state, data) {
            state.userData = data
        },
        async getUserData(state) {
            try {
                const response = await axios.get('/api/me/')
                state.userData = response.data
                await this.dispatch('getUserTypeData', state.userData);
            } catch (error) {
                console.log(error)
            }
        },
        changeAuthorization(state, value) {
            state.isAuthorization = value
            localStorage.setItem('isAuthorization', value)
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
    actions: {
        setUserData({commit}) {
            commit('getUserData')
        },
        changeAuthorization({commit}, value) {
            commit('changeAuthorization', value)
        },
        getAuthorization({state}) {
            state.isAuthorization = Boolean(localStorage.getItem('isAuthorization'))
        },
        async getUserTypeData({state},userData) {
            try {
                const response = await axios.get(`/${userData.usertype}/data/${userData.id}/`);
                // eslint-disable-next-line no-unused-vars
                // const { user, ...dataWithoutUser } = response.data;
                state.userData = Object.assign({}, state.userData, response.data);
            } catch (error) {
                console.log(error);
            }
        },
    },
    getters: {},
    modules: {}
})
