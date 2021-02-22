import Vue from 'vue'
import Router from 'vue-router'

import Profile from '@/components/Profile'
import Index from '@/components/Index'

Vue.use(Router)

export default new Router({
  routes: [
    {
      name: 'profile',
      path: '/profile',
      component: Profile
    },
    {
      name: 'index',
      path: '/',
      component: Index
    }
  ]
})
