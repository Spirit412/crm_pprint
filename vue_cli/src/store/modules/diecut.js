import axios from "axios";

export default {
    namespaced: true,
    state: {
        diecuts: [],
        diecuts_count: null
    },

    getters: {
        ALL_DIECUTS(state) {
            return state.diecuts
        },
    },
    actions: {
        GET_ALL_DIECUTS_FROM_API({commit},) {
            return axios('api/v1/diecuts/', { 
                method:'GET'
            })
                .then((diecuts) => {
                    console.log('получил данные с сервера')
                    commit('SET_ALL_DIECUTS_TO_STATE', diecuts.data);
                })
                .catch((error) =>{
                    console.warn('Получаем данные "api/v1/diecuts/" - гл что-то пошло не так')
                    console.log(error)
                    return error
                })
        },
        async ADD_DIECUT({commit}, form) {
            await axios.post('api/v1/diecuts/', form)
                .then((res) => {
                    console.log(res.data)
                })
                .catch((error) => {
                    // error.response.status Check status code
                    console.warn('ADD_DIECUT что-то пошло не так :(' + '  ' + error)
                })
                .finally(() => {
                    //Perform action in always
                })

        },
    },
    mutations: {
        SET_ALL_DIECUTS_TO_STATE: (state, diecuts) => {
            state.diecuts = diecuts
            if (state.diecuts) {
                state.diecuts_count = 'нет данных'
            }
                state.diecuts_count = diecuts.length
        },
    },
}