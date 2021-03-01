import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

import user from './modules/user'
import zub from './modules/zub'
import diecut from './modules/diecut'


export default new Vuex.Store({
    modules: {
        user,
        zub,
        diecut
    }
});