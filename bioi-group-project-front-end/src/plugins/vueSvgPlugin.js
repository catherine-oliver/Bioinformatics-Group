// Based on tutorial from: https://blog.carbonteq.com/creating-interactive-map-in-vue-js/
const svgJs = require("svg.js/dist/svg")

export default {
    install: Vue => {
        Vue.prototype.$svg = svgJs
    }
}