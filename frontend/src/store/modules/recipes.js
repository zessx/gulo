import axios from 'axios'

const state = () => ({
  all: [],
  recipe: null,
  search: {
    dish: 'main_course',
    text: null,
    tags: [],
    sort: 'date'
  }
})

const getters = {}

const mutations = {
  setRecipes (state, recipes) {
    state.all = recipes
  },
  clearRecipes (state) {
    state.all = []
  },
  setRecipe (state, recipe) {
    state.recipe = recipe
  },
  clearRecipe (state) {
    state.recipe = null
  },
  setSearch (state, { dish, text, tags, sort }) {
    state.search = {
      dish,
      text,
      tags,
      sort
    }
  }
}

const actions = {
  getRecipesList ({ commit }, { dish, text, tags, sort }) {
    commit('setSearch', { dish, text, tags, sort })
    let payload = { dish, tags, sort }
    if (text) {
      payload.text = text
    }
    return axios.post('/api/recipes/search', payload)
      .then(response => { commit('setRecipes', response.data) })
      .catch(e => { console.log(e) })
  },
  getRecipe ({ commit }, id) {
    return axios.get('/api/recipes/' + id)
      .then(response => { commit('setRecipe', response.data) })
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
