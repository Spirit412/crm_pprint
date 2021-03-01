import axios from "axios";

export default {
    namespaced: true,
    state: {
        zubs: [],
        zubs_count: null
    },
    getters: {
        ALL_ZUBS(state) {
            return state.zubs
        },
    },
    mutations: {
        SET_ALL_ZUBS_TO_STATE: (state, zubs) => {
            state.zubs = zubs
            if (state.zubs) {
                state.zubs_count = 0
            }
            state.zubs_count = zubs.length
        },
    },
    actions: {
        GET_ALL_ZUBS_FROM_API({commit},) {
            return axios('api/v1/zub/', {
                method: 'GET'
            })
                .then((resronse) => {
                    commit('SET_ALL_ZUBS_TO_STATE', resronse.data)
                })
                .catch((error) => {
                    console.warn('GET LIST ZUUBS что-то пошло не так :(')
                    // console.warn(error)
                    // return error
                })
        },
    }

}