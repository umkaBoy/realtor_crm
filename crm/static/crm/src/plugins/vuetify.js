import '@mdi/font/css/materialdesignicons.css'
import Vue from 'vue'
import Vuetify from 'vuetify'

Vue.use(Vuetify)

const vuetify = new Vuetify({
  theme: {
    themes: {
      light: {
        primary: '#005c89',
        secondary: '#edf2fa',
        accent: '#e7f5fe',
        error: '#b71c1c'
      }
    }
  },
  icons: {
    iconfont: 'mdi' // default - only for display purposes
  }
})

export default vuetify
