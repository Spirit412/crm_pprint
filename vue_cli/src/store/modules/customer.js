import axios from "axios";

export default {
    namespaced: true,
    state: {
        customers: []
    },

    getters: {
        ALL_CUSTOMERS(state) {
            return state.customers
        },
    },
    actions: {
        GET_ALL_CUSTOMERS_FROM_API({commit},) {
            return axios('api/v1/customer/', {
                method: 'GET'
            })
                .then((customers) => {
                    console.log('получил данные с сервера')
                    commit('SET_ALL_CUSTOMERS_TO_STATE', customers.data);
                })
                .catch((error) => {
                    console.warn('Получаем данные "api/v1/customer/" - гл что-то пошло не так')
                    console.log(error)
                    return error
                })
        },
    },
    mutations: {
        SET_ALL_CUSTOMERS_TO_STATE: (state, get_data) => {
            state.customers = get_data
        },
    },
}