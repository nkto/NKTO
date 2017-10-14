import Vue from 'vue'
import iView from 'iview'
import 'iview/dist/styles/iview.css'
import User from './User.vue'

Vue.use(iView)

/* eslint-disable no-new */
new Vue({
  el: '#user',
  components: { User }
})
