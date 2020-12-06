import axios from 'axios'

const state = () => ({
  all: [],
  recipe: null
})

const getters = {}

const mutations = {
  setRecipes (state, recipes) {
    state.all = recipes
  },
  setRecipe (state, recipe) {
    state.recipe = recipe
  }
}

const actions = {
  getRecipesList (context) {
    return axios.get('/api/recipes')
      .then(response => { context.commit('setRecipes', response.data) })
      .catch(e => { console.log(e) })
  },
  getRecipe (context, recipeId) {
    return axios.get('/api/recipes/' + recipeId)
      .then(response => { context.commit('setRecipe', response.data) })
      .catch(e => { console.log(e) })
  },
  // createRecipe (context, payload) {
  //   var avatar = payload.avatar
  //   delete payload.avatar

  //   return axios.post('/api/recipes/', payload)
  //     .then(response => {
  //       // Image upload
  //       if (typeof avatar === 'object') {
  //         let data = new FormData()
  //         data.append('avatar', avatar)
  //         return axios.patch('/api/recipes/' + response.data.id, data)
  //       }
  //     })
  //     .catch(e => { console.log(e) })
  // },
  // editRecipe (context, payload) {
  //   var avatar = payload.avatar
  //   delete payload.avatar

  //   return axios.patch('/api/recipes/' + payload.id, payload)
  //     .then(response => {
  //       // Image upload
  //       if (typeof avatar === 'object') {
  //         let data = new FormData()
  //         data.append('avatar', avatar)
  //         return axios.patch('/api/recipes/' + payload.id, data)
  //       }
  //     })
  //     .catch(e => { console.log(e) })
  // },
  // deleteRecipe (context, recipeId) {
  //   return axios.delete('/api/recipes/' + recipeId)
  //     .then(response => {})
  //     .catch(e => { console.log(e) })
  // },
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
