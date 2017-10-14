import Vue from 'vue'
import homepage from './homepage.vue'
import iView from 'iview'
import '../../mytheme/dist/iview.css'

Vue.use(iView)

/* eslint-disable no-new */
new Vue({
  el: '#homepage',
  components: { homepage }
})
