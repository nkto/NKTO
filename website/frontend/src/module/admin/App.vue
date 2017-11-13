<template>
  <div class="layout">
    <Row type="flex">
      <Col span="5" class="layout-menu-left">
        <Menu active-name="1-2" theme="dark" width="auto" :open-names="['1']">
          <div class="layout-logo-left"></div>
          <Submenu name="1">
            <template slot="title">
              <Icon type="ios-navigate"></Icon>
              用户管理
            </template>
            <MenuItem name="1-1" @click.native="toggle('user1')">用户1</MenuItem>
            <MenuItem name="1-2" @click.native="toggle('user2')">用户2</MenuItem>
            <MenuItem name="1-3" @click.native="toggle('user3')">用户3</MenuItem>
          </Submenu>
          <Submenu name="2">
            <template slot="title">
              <Icon type="ios-keypad"></Icon>
              商品管理
            </template>
            <MenuItem name="2-1" @click.native="toggle('goods1')">在售商品</MenuItem>
            <MenuItem name="2-2" @click.native="toggle('goods2')">下架商品</MenuItem>
          </Submenu>
          <Submenu name="3">
            <template slot="title">
              <Icon type="ios-analytics"></Icon>
              历史交易
            </template>
            <MenuItem name="3-1">交易1</MenuItem>
            <MenuItem name="3-2">交易2</MenuItem>
          </Submenu>
          <Submenu name="4">
            <template slot="title">
              <Icon type="ios-analytics"></Icon>
              网站管理
            </template>
            <MenuItem name="4-1">管理1</MenuItem>
            <MenuItem name="4-2">管理2</MenuItem>
          </Submenu>
        </Menu>
      </Col>
      <Col span="19" class="right-content">
				<div class="layout-header">
				  <Menu mode="horizontal" class="nav">
				    <Menu-item name="1">
				      <Icon type="home"></Icon>
				      网站首页
				      </Menu-item>
				      <Menu-item name="2">
				        <Icon type="ios-paper"></Icon>
				        帮助中心
				      </Menu-item>
				      <Submenu name="3" class="person">
				        <template slot="title">
				          Admin
				        </template>
				        <Menu-item name="3-1">
				          个人中心  
				        </Menu-item>
				        <Menu-item name="3-2">
				          退出登录
				        </Menu-item>
				      </Submenu>
				    </Menu>
				</div>
        <div class="layout-content">
          <div class="layout-content-main">
					  <div :is="comp"></div>
          </div>
        </div>
        <div class="layout-copy">
          2017-2018 &copy; NKTO
        </div>
      </Col>
    </Row>
  </div>
</template>
<script>
import User1 from "./components/User1.vue"
import User2 from "./components/User2.vue"
import Goods1 from "./components/Goods1.vue"
import Goods2 from "./components/Goods2.vue"
import Deal1 from "./components/Deal1.vue"
export default {
  components: {User1, User2, Goods1, Goods2, Deal1
  },
  data() {
    return {
      comp: "deal1"
    };
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
        })
        .then((res) => res.json())
    },
    toggle (comp) {
      this.comp = comp
    }
  },
  async created () {
    let res = await this.fetchBase('/api/user/validate/', {
      'type': 2
    })
    if (res['flag'] === -1) {
      this.$Message.warning('未登录')
    } else if (res['flag'] === 1 || res['flag'] === 2) {
      this.$Message.success('您已登录')
    }
  }
}
</script>
<style scoped>
.layout {
  border: 1px solid #d7dde4;
  background: #f5f7f9;
  position: relative;
}
.layout-breadcrumb {
  padding: 10px 15px 0;
}
.layout-content {
  min-height: 83vh;
  margin: 15px;
  overflow: hidden;
  background: #fff;
  border-radius: 4px;
}
.right-content {
  margin-left: 20.83333333%;
}
.layout-content-main {
  padding: 10px;
}
.layout-copy {
  text-align: center;
  padding: 10px 0 20px;
  color: #9ea7b4;
}
.layout-menu-left {
  background: #464c5b;
  position: fixed;
  height: 98vh;
}
.layout-header {
  text-align: right;
  height: 60px;
  background: #fff;
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.1);
}
.layout-logo-left {
  width: 90%;
  height: 30px;
  background: #5b6270;
  border-radius: 3px;
  margin: 15px auto;
}
.nav {
  position: fixed;
  right: 0;
  top: 0;
}
.person {
  text-align: left;
}
</style>