import Vue from 'vue'
import Vuelidate from 'vuelidate'
import App from '../src/App'
import './registerServiceWorker'
import router from './router'
import dateFilter from './filters/date.filter'
import 'materialize-css/dist/js/materialize.min'


//Vuex
import store from './store'

// AXIOS
import axios from './axios'


Vue.config.productionTip = false

Vue.use(Vuelidate)
Vue.filter('date', dateFilter)


const vm = new Vue({
    el: '#app',
    router,
    store,
    render: h => h(App)
})

export {vm}