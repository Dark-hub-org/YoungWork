import Vue from 'vue'
import Vuex from 'vuex'
import axios from "axios";
// import {commit} from "lodash/seq";

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        access: '',
        refresh: '',
        isProfileEdit: false,
        vacanciesList: [],
    },
    mutations: {
        initializeStore(state){
            if ( localStorage.getItem("access")) {
                state.access = localStorage.getItem("access")
                state.refresh = localStorage.getItem("refresh")
            } else {
                state.access = ''
                state.refresh = ''
            }
        },
        setAccess(state, access){
            state.access = access
            localStorage.setItem('access', access)
        },
        setRefresh(state, refresh){
            state.refresh = refresh
            localStorage.setItem('refresh', refresh)
        },
        editISProfileEdit(state, newVal) {
            state.isProfileEdit = newVal
        },
        setVacanciesList(state, vacancies) {
            state.vacanciesList = vacancies;
        },
    },
    actions: {
        getVacancies({commit}) {
            axios.get('/api/v1/vac')
                .then(response => {
                    console.log(response.data.results)
                    commit('setVacanciesList', response.data.results)
                })
                .catch(error => {
                    console.log(error)
                })
        },
    },
    getters: {
        getVacanciesList: state => state.vacanciesList
    },
    modules: {}
})
