import Vue from 'vue'
import iView from 'iview'
import App from './App'
import 'iview/dist/styles/iview.css'


Vue.use(iView)
/* eslint-disable no-new */
new Vue({
	el: '#app',
	components: {App}
})