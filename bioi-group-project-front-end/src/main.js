import Vue from 'vue'
import App from './App.vue'
import router from './router'

// Based on tutorial from: https://blog.carbonteq.com/creating-interactive-map-in-vue-js/
import svgJs from "./plugins/vueSvgPlugin"
Vue.use(svgJs);

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
