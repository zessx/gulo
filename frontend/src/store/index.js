import Vue from 'vue'
import Vuex from 'vuex'

import notices from '@/store/modules/notices'
import recipes from '@/store/modules/recipes'
import tags from '@/store/modules/tags'

Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    notices,
    recipes,
    tags
  }
})

export default store
