import axios from 'axios'
import randomId from '@/utils/randomId'

const state = () => ({
  all: []
})

const getters = {}

const mutations = {
  addNotice (state, notice) {
    notice.id = randomId(8)
    if (typeof notice.type === 'undefined') {
      notice.type = 'info'
    }
    state.all.push(notice)
    console.log(state.all)
  },
  removeNotice (state, id) {
    state.all = state.all.filter(notice => notice.id !== id)
  },
  clearNotices (state) {
    state.all = []
  }
}

const actions = {}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
