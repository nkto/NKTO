<template>
    <div class="total" style="height:100%">
    <logoheader></logoheader>
    <hr>
    <div style="height:100%">
    <Menu :theme="theme3" :active-name="activenum" class="menu">
        <MenuGroup title="个人相关信息">
            <MenuItem name="information" @click.native="transfer('information')">
                <Icon type="settings" ></Icon>
                修改个人信息
            </MenuItem>
            <MenuItem name="chat" @click.native="transfer('CustomerTalk')">
              <Icon type="document" ></Icon>
              聊天记录
            </MenuItem>
        </MenuGroup>
        <MenuGroup title="商品相关">
            <MenuItem name="publish" @click.native="transfer('publish')">
                <Icon type="lightbulb"></Icon>
                上架新商品
            </MenuItem>
            <MenuItem name="pubed" @click.native="transfer('pubed')">
                <Icon type="folder"></Icon>
                发布商品记录
            </MenuItem>
            <MenuItem name="collect" @click.native="transfer('collect')">
                <Icon type="bookmark"></Icon>
                查看收藏列表
            </MenuItem>
            <MenuItem name="history" @click.native="transfer('history')">
                <Icon type="compass"></Icon>
                我的浏览历史
            </MenuItem>
            <MenuItem name="order" @click.native="transfer('order')">
                <Icon type="ios-cart-outline"></Icon>
                查看已下订单
            </MenuItem>
        </MenuGroup>
    </Menu>
    <div :is="form" class="screen" @send="send" :content="currentcontent" :name="usrname" :uid="uid">
    </div>
    </div>
    </div>
</template>
<script>
import logoheader from './components/logoheader'
import nktoFooter from '../../components/nktoFooter'
import collect from './components/collect'
import history from './components/history'
import information from './components/information'
import order from './components/order'
import publish from './components/publish'
import pubed from './components/pubed'
import CustomerTalk from '../../components/CustomerTalk'
export default {
    components: {collect,history,information,order,publish,pubed,logoheader,nktoFooter, CustomerTalk},
    data() {
        return {
            form: 'CustomerTalk',
            currentcontent: [],
            usrname: 'hehe',
            uid: '1',
            socket: null,
            activenum: '1',
        }
    },
    methods: {
        getCookie (cName) {
          if (document.cookie.length > 0) {
            let cStart = document.cookie.indexOf(cName + '=')
            if (cStart !== -1) {
              cStart = cStart + cName.length + 1
              let cEnd = document.cookie.indexOf(';', cStart)
              if (cEnd === -1) {
                cEnd = document.cookie.length
              }
              return unescape(document.cookie.substring(cStart, cEnd))
            }
          }
          return ''
        },
        fetchBase (url, body) {
          return fetch(url, {
            method: 'post',
              credentials: 'same-origin',
              headers: {
                'X-CSRFToken': this.getCookie('csrftoken'),
                'Accept': 'application/json',
                'Content-Type': 'application/json'
              },
              body: JSON.stringify(body)
          }).then((res) => res.json())
        },
        transfer(newform) {
            this.form = newform
            location.href = '/setting/' + newform
        },
        dateformat (date) {
          let seperator1 = '-'
          let seperator2 = ':'
          let month = date.getMonth() + 1
          let strDate = date.getDate()
          if (month >= 1 && month <= 9) {
            month = '0' + month
          }
          if (strDate >= 0 && strDate <= 9) {
            strDate = '0' + strDate
          }
          var currentdate = date.getFullYear() + seperator1 + month + seperator1 + strDate + ' ' + date.getHours() + seperator2 + date.getMinutes() + seperator2 + date.getSeconds()
          return currentdate
        },
        myResponse () {
        this.socket.on('getresponse', (msg) => {
          let data = {}
          data['word'] = decodeURI(msg['data'])
          data['self'] = false
          data['time'] = msg['time']
          data['src'] = decodeURI(msg['src'])
          this.currentcontent.push(data)
        })
        },
        send (msg) {
          let data = {}
          data['word'] = msg
          data['self'] = true
          data['time'] = this.dateformat(new Date())
          data['src'] = '/static/img/user.png'
          this.currentcontent.push(data)
          this.socket.emit('sendmessage', {data: encodeURI(msg), time: data['time'], src: encodeURI(data['src']), uid: this.uid})
        }
    },
    async mounted () {
      // 先發送一個請求驗證是否已經登錄
      let res = await this.fetchBase('/api/user/checkstate/', {})
      console.log(res)
      if (res['flag'] !== 1) {
        location.href = '/'
      }
    },
    created: function () {
      if(this.socket === null) {
        this.socket = io.connect('http://' + document.domain + ':' + location.port + '/test')
        this.socket.emit('connected', {uid: this.uid})
        this.myResponse()
      }
      let last = location.href.split('/')[location.href.split('/').length - 1]
      if (last === 'information') {
        this.form = 'information'
        this.activenum = '1'
      } else if (last === 'pubed') {
        this.form = 'pubed'
        this.activenum = '3'
      } else if (last === 'collect') {
        this.form = 'collect'
        this.activenum = '4'
      } else if (last === 'history') {
        this.form = 'history'
        this.activenum = '5'
      } else if (last === 'publish') {
        this.form = 'publish'
        this.activenum = '2'
      } else if (last === 'order') {
        this.form = 'order'
        this.activenum = '6'
      }
    }
}
</script>
<style scoped>
 .menu {
     height: 100%;
     float: left;
     width: 16%;
 }
 .screen {
     height: 100%;
     width: 75%;
     float: left;
     margin-top: 15px;
     margin-left: 4%;
 }
</style>

