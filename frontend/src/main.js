import Vue from 'vue'
import store from '@/store'
import router from '@/router'

import axios from 'axios'
import upperFirst from 'lodash/upperFirst'
import camelCase from 'lodash/camelCase'

import App from '@/App.vue'
import './registerServiceWorker'
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

Vue.config.productionTip = false

/**
 * Require components globally.
 */
const requireComponents = require.context('./components', true, /\w+\.(vue)$/)
requireComponents.keys().forEach(fileName => {
  const componentConfig = requireComponents(fileName)
  const componentName = upperFirst(
    camelCase(
      fileName
        .split('/')
        .pop()
        .replace(/\.\w+$/, '')
    )
  )

  Vue.component(
    componentName,
    componentConfig.default || componentConfig
  )
})

new Vue({
  router,
  store,

  render: h => h(App)
}).$mount('#app')
