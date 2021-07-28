import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import(/* webpackChunkName: "Home" */ '../components/HomePage.vue')
  },
  {
    path: '/info',
    name: 'Info',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "Info" */ '../components/GeneralInfo.vue')
  },
  {
    path: '/data-visualization',
    name: 'data-visualization',
    component: () => import(/* webpackChunkName: "DataVisualization" */ '../components/DataVisualization.vue')
  },
  {
    path: '/create-user',
    name: 'create-user',
    component: () => import(/* webpackChunkName: "DataVisualization" */ '../components/CreateUser.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import(/* webpackChunkName: "DataVisualization" */ '../components/UserLogin.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
