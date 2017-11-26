<template>
  <div class="header">
    <Row type="flex" justify="center" align="middle">
      <Col span="6"><img src="/static/img/logo.jpg" class="img"></Col>
      <Col span="8"><Input icon="search" class="search" placeholder="请输入搜索内容"></Input></Col>
      <Col span="6">
        <div>
          <div :is="userstate" :icon="usericon"></div>
          <!-- <offline></offline> -->
        </div>
      </Col>
    </Row>
    <div>
      <div class="bg"></div>
      <Menu mode="horizontal" theme="primary" active-name="1" class="menu">
        <MenuItem name = "0">
          &nbsp;&nbsp;首页
        </MenuItem>
        <MenuItem name="1">
          <Icon type="ios-paper"></Icon>
          收纳整理
        </MenuItem>
        <MenuItem name="2">
          <Icon type="ios-people"></Icon>
          教材杂志
        </MenuItem>
        <Submenu name="3">
          <template slot="title">
            <Icon type="stats-bars"></Icon>
            办公文具
          </template>
          <MenuGroup title="使用">
            <MenuItem name="3-1">新增和启动</MenuItem>
            <MenuItem name="3-2">活跃分析</MenuItem>
            <MenuItem name="3-3">时段分析</MenuItem>
          </MenuGroup>
          <MenuGroup title="留存">
            <MenuItem name="3-4">用户留存</MenuItem>
            <MenuItem name="3-5">流失用户</MenuItem>
          </MenuGroup>
        </Submenu>
        <MenuItem name="4">
          <Icon type="settings"></Icon>
          服装鞋帽
        </MenuItem>
      </Menu>
    </div>
  </div>
</template>
<script>
  import online from './online'
  import offline from './offline'
  export default {
    components: {online, offline},
    data () {
      return {
        userstate: 'offline',
        usericon: ''
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
          })
          .then((res) => res.json())
      }      
    },
    async created () {
      // 先發送一個請求驗證是否已經登錄
      let res = await this.fetchBase('/api/user/checkstate/', {})
      console.log(res)
      if (res['flag'] === 1) {
        this.userstate = 'online'
        this.usericon = res['msg']
      } else {
        this.userstate = 'offline'
      }
    }
  }
</script>
<style scoped>
  .img {
    width: 150px;
    height: 100px;
    margin-left: 60px;
  }
  .search {
    width: 300px;
    margin-left:30px
  }
  .menu {
    width: 100%;
  }
  .car {
    display: inline-block;
    overflow: hidden;
    height: 70px;
    outline: none;
    border:  1px solid#C0C0C0;
    background-color: #FFFFFF;
    background-image: url('/static/img/car.jpg');
    background-size: 40px 40px;
    background-repeat: no-repeat;
    background-position: 2%;
    font-family: "宋体";
    font-size: 15px;
    padding-left: 60px;
    padding-top: 20px;
  }
  .bg {
    width: 10%;
    padding-top: 60px;
    overflow: hidden;
    background-color: #eb6133;
    float: left;
  }
  .shouye {
    display: inline-block;
    text-align: center;
    width: 7%;
    padding-bottom: 20px;
    overflow: hidden;
    font-size: 20px;
  }
</style>