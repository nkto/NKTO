import Vue from 'vue'
import ProductDetail from './ProductDetail'
import iView from 'iview'
import '../../mytheme/dist/iview.css'

Vue.use(iView)

/* eslint-disable no-new */
new Vue({
  el: '#productdetail',
  components: { ProductDetail }
})
