import Vue from 'vue'
import VueI18n from 'vue-i18n'
import store from '@/store'
import router from '@/router'

import axios from 'axios'
import upperFirst from 'lodash/upperFirst'
import camelCase from 'lodash/camelCase'

import { messages as enMessages } from '@/locales/en'
import { messages as frMessages } from '@/locales/fr'

import App from '@/App.vue'
import './registerServiceWorker'
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

Vue.config.productionTip = false

/**
 * Internationalization
 */
Vue.use(VueI18n)
const messages = {
  en: enMessages,
  fr: frMessages
}
const i18n = new VueI18n({
  locale: navigator.language || navigator.userLanguage,
  fallbackLocale: 'en',
  silentFallbackWarn: true,
  messages
})

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
  i18n,

  render: h => h(App)
}).$mount('#app')
