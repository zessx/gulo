import Vue from 'vue'
import VueRouter from 'vue-router'

import Styleguide from '@/components/Styleguide.vue'
import Recipes from '@/components/Recipes.vue'
import Agenda from '@/components/Agenda.vue'
import Shopping from '@/components/Shopping.vue'

const routes = [
  { path: '/', redirect: '/recipes' },
  { path: '/recipes', component: Recipes },
  { path: '/agenda', component: Agenda },
  { path: '/shopping', component: Shopping },
  { path: '/styleguide', component: Styleguide },
]

Vue.use(VueRouter)
const router = new VueRouter({
  scrollBehavior (to, from, savedPosition) { return { x: 0, y: 0 } },
  mode: 'history',
  routes
})

export default router
