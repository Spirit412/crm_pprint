import axios from "axios";

export default {
    namespaced: true,
    state: {
        data_djobs: []
    },

    getters: {
        ALL_DJOBS(state) {
            return state.data_djobs
        },
    },
    actions: {
        GET_ALL_DJOBS_FROM_API({commit},) {
            return axios('api/v1/djob/', {
                method: 'GET'
            })
                .then((data_db) => {
                    console.log('получил данные с сервера')
                    commit('SET_ALL_DJOBS_TO_STATE', data_db.data);
                })
                .catch((error) => {
                    console.warn('Получаем данные "api/v1/djob/" - гл что-то пошло не так')
                    console.log(error)
                    return error
                })
        }
    },
    mutations: {
        SET_ALL_DJOBS_TO_STATE: (state, djobs) => {
            state.data_djobs = djobs
        },
    },
}