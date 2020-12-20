import axios from 'axios'

const state = () => ({
  results: [],
  selected: [],
  search: null
})

const getters = {}

const mutations = {
  setResults (state, tags) {
    state.results = tags
  },
  clearResults (state) {
    state.results = []
  },
  setSelected (state, tags) {
    state.selected = tags
  },
  addSelected (state, tag) {
    if (state.selected.filter(e => e.pk === tag.pk).length === 0) {
      state.selected.push(tag)
    }
  },
  removeSelected (state, tag) {
    state.selected = state.selected.filter(e => e.pk !== tag.pk)
  },
  clearSelected (state) {
    state.selected = []
  },
  setSearch (state, search) {
    state.search = search
  }
}

const actions = {
  getTagsList ({ commit }, text) {
    commit('setSearch', text)
    let payload = { text }
    return axios.post('/api/tags/search', payload)
      .then(response => { commit('setResults', response.data) })
      .catch(e => { console.log(e) })
  },
  selectTag ({ commit }, id) {
    return axios.get('/api/tags/' + id)
      .then(response => { commit('addSelected', response.data) })
      .catch(e => { console.log(e) })
  },
  unselectTag ({ commit }, id) {
    return axios.get('/api/tags/' + id)
      .then(response => { commit('removeSelected', response.data) })
      .catch(e => { console.log(e) })
  }
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
