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
    actions: {
        GET_ALL_ZUBS_FROM_API({commit},) {
            return axios('api/v1/zub', { method:'GET'
            })
                .then((zubs) => {
                    commit('SET_ALL_ZUBS_TO_STATE', zubs.data);
                    return zubs
                })
                .catch((error) => {
                    console.log(error)
                    return error
                })
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
}