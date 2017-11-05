import Vue from 'vue'
import personal from './personal'
import iView from 'iview'
import '../../mytheme/dist/iview.css'

Vue.use(iView)

/* eslint-disable no-new */
new Vue({
  el: '#nkto',
  components: { personal }
})
