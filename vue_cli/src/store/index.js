import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

import user from './modules/user'
import zub from './modules/zub'
import diecut from './modules/diecut'
// import djob from './modules/djob'
// import customer from './modules/customer'


export default new Vuex.Store({
    modules: {
        user,
        zub,
        diecut,
        // djob,
        // customer,
    }
});