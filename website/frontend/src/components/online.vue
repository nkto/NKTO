<template>
<Row type="flex" justify="center" align="middle">
    <Col span="6">
    <Dropdown placement="bottom-start">
        <Button type="ghost" shape="circle" class="avatar-btn"><Img class="user-avatar" :src="icon"/></Button>
        <DropdownMenu slot="list">
            <DropdownItem @click.native="personsetting('information')">修改个人信息<Icon type="settings" style="margin-left:3px;"></Icon></DropdownItem>
            <DropdownItem @click.native="personsetting('pubed')">发布商品记录<Icon type="folder" style="margin-left:3px;"></Icon></DropdownItem>
            <DropdownItem @click.native="personsetting('collect')">查看收藏列表<Icon type="bookmark" style="margin-left:5px;"></Icon></DropdownItem>
            <DropdownItem @click.native="personsetting('his')">我的浏览历史<Icon type="compass" style="margin-left:3px;"></Icon></DropdownItem>
            <DropdownItem divided><a @click="logout">注销</a></DropdownItem>
        </DropdownMenu>
    </Dropdown>
    </Col>
    <Col span="9">
    <Button class="pub-btn" type="ghost" shape="circle" icon="lightbulb" @click="personsetting('publish')">发布新商品</Button>
    </Col>
    <Col span="9">
    <Button class="pub-btn" type="ghost" shape="circle" icon="ios-cart-outline" @click="personsetting('order')">查看已下订单</Button>
    </Col>
</Row>
</template>
<script>
export default {
  props: ['icon'],
  data () {
    return {

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
    },
    personsetting (item) {
      location.href = '/setting/' + item
    },
    async logout () {
      this.$Message.error('dd')
      let res = await this.fetchBase('/api/user/logout/')
      if (res['flag'] === -1) {
        this.$Message.error('注销失败')
      } else if (res['flag'] === 1) {
        this.$Message.success('注销成功')
      }
    }
  },
  async created () {
    console.log(this.icon)
    let res = await this.fetchBase('/api/user/validate/', {
      'type': 1
    })
    if (res['flag'] === -1) {
      this.$Message.warning('未登录')
    } else if (res['flag'] === 1) {
      this.$Message.success('您已登录')
    }
  }
}
</script>
<style scoped>
  .avatar-btn {
    height: 50px;
    width: 60px;
  }
  .user-avatar {
    height: 100%;
    width: 100%;
  }
  .pub-btn {
    font-size: 15px;
  }
</style>

