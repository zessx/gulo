import axios from 'axios'

const state = () => ({
  all: [],
  recipe: null,
  search: {
    dish: 'main_course',
    text: null,
    tags: []
  }
})

const getters = {}

const mutations = {
  setRecipes (state, recipes) {
    state.all = recipes
  },
  setRecipe (state, recipe) {
    state.recipe = recipe
  },
  setSearch (state, dish, text, tags) {
    state.search = {
      dish,
      text,
      tags
    }
  }
}

const actions = {
  getRecipesList (context, dish = 'main_course', text = null, tags = []) {
    context.commit('setSearch', dish, text, tags)
    let payload = { dish, tags }
    if (text) {
      payload.text = text
    }
    return axios.post('/api/recipes/search', payload)
      .then(response => { context.commit('setRecipes', response.data) })
      .catch(e => { console.log(e) })
  },
  getRecipe (context, recipeId) {
    return axios.get('/api/recipes/' + recipeId)
      .then(response => { context.commit('setRecipe', response.data) })
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
