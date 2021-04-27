import axios from 'axios'

export default {
    namespaced: true,
    state: {
        token: null,
        email: null
    },
    getters: {
        USER_AUTH: state => {
            return state.email;
        },
        // USER_AUTH(state) {
        //     return state.email
        // }
    },
    actions: {
        async LOGIN_USER({ commit }, form) {
            const response = await axios.post('api/v1/user/login/', form)
            const user = await response.data
            console.log(user)
            commit('UPDATE_USER_AUTH', user)
        },
        async REGISTER_USER({ commit }, form) {
            const response = await axios.post('api/v1/user/register/', form)
            // .then(() => this.$router.push('/register'))
            // .catch(err => console.log(err))
            const user = await response.data
            commit('UPDATE_USER_AUTH', user)
        },
        LOGOUT({ commit }) {
            commit('LOGOUT')
        }
    },
    mutations: {
        UPDATE_USER_AUTH(state, user) {
            localStorage.token = user.token
            localStorage.email = user.email
            localStorage.name = user.name
            localStorage.role = user.role_user.role
            localStorage.description = user.description
            state.token = user.token
            state.email = user.email
            state.name = user.name
            state.role = user.role_user.role
            state.description = user.description
        },
        LOGOUT(state) {
            state.token = null
            state.email = null
            state.name = null
            state.role = null
            state.description = null
            localStorage.clear()
        }
    }
}