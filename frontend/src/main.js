import Vue from 'vue'
import VueI18n from 'vue-i18n'
import { VueHammer } from 'vue2-hammer'
import Hammer from 'hammerjs'
import store from './store'
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
 * Touch gestures
 */
Vue.use(VueHammer)
VueHammer.config.swipe = {
  direction: Hammer.DIRECTION_HORIZONTAL
}
VueHammer.config.pan = { enabled: false }
VueHammer.config.pinch = { enabled: false }
VueHammer.config.press = { enabled: false }
VueHammer.config.rotate = { enabled: false }
VueHammer.config.tap = { enabled: false }

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
