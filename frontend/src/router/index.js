import Vue from 'vue'
import Router from 'vue-router'
import PaginaPrincipal from '@/PaginaPrincipal'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'PaginaPrincipal',
      component: PaginaPrincipal
    }
  ]
})
