import Vue from 'vue'
import Vuex from 'vuex'

import recipes from '@/store/modules/recipes'

Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    recipes
  }
})

export default store
