<template>
    <div class="form">
    <Input v-model="username" placeholder="注册邮箱/手机号" class="input" type="text"></Input>
    <Input v-model="password" placeholder="密码" class="input" type="password"></Input>
    <div class="input">
        <Input v-model="vertifycode" placeholder="验证码" class="vertifycode-input" type="text"></Input>
        <img src="/static/img/a1.jpg" class="vertifycode-img"/>
    </div>
    <Button type="primary" shape="circle" class="input input-btn" @click="submit">登录</Button>
    </div>
</template>
<script>
export default {
  data () {
    return {
        username: '',
        password: ''
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
    checkEmail (email) {
        var ePattern = /^([A-Za-z0-9])+@mail\.nankai\.edu\.cn$/g
        var ePattern2 = /^([A-Za-z0-9])+@nankai\.edu\.cn$/g
        return (ePattern.test(email) || ePattern2.test(email))
    },
    checkPhone (phone) {
        let ePattern = /^1[3|4|5|7|8][0-9]{9}$/g
        return ePattern.test(phone)
    },
    clear () {
        this.username = ''
        this.password = ''
    },
    async submit () {
        // 发送请求
        let res = await this.fetchBase('/api/user/signin/', {
            'username': this.username.trim(),
            'password': this.password.trim()
        })
        if (res['flag'] > 0) {
            this.$Message.success('登录成功')
            window.location.href = '/'
        } else if (res['flag'] === -1) {
            this.$Message.warning('密码错误')
        } else if (res['flag'] === -2) {
            this.$Message.warning('无此账号')
        } else if (res['flag'] === -3) {
            this.$Message.error('登录失败')
        }
        this.clear()
    }
  }
}
</script>
<style scoped>
 .form {
     text-align: center;
     margin-top: 15px;
 }
 .input {
     width: 300px;
     display: block;
     margin: auto;
     margin-bottom: 2px;
 }
 .input-btn {
     margin-top: 25px;
 }
 .vertifycode-input {
     width: 75%;
     float: left;
 }
 .vertifycode-img {
     width: 25%;
     height: 32px;
 }
</style>
