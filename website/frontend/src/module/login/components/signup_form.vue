<template>
    <div class="form">
    <Input v-model="username" placeholder="用户名" class="input" type="text"></Input>
    <Input v-model="password" placeholder="密码" class="input" type="password"></Input>
    <Input v-model="email" placeholder="学生邮箱" class="input" type="text"></Input>
    <Input v-model="phonenumber" placeholder="手机号" class="input" type="text"></Input>
    <Button type="primary" shape="circle" class="input input-btn" @click="submit">注册</Button>
    </div>
</template>
<script>
export default {
  data () {
    return {
        username: '',
        password: '',
        email: '',
        phonenumber: ''
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
        this.email = ''
        this.phonenumber = ''
    },
    async submit () {
        // 检查数据合法性
        if(this.checkEmail(this.email.trim()) === false) {
            this.$Message.warning('必须要南开邮箱')
            this.clear()
            return
        }
        if(this.checkPhone(this.phonenumber.trim()) === false) {
            this.$Message.warning('手机号码不对')
            this.clear()
            return
        }
        if(this.password.length < 8) {
            this.$Message.warning('密码长度不能小于8')
            this.clear()
            return
        }
        // 发送请求
        let res = await this.fetchBase('/api/user/signup/', {
            'email': this.email.trim(),
            'password': this.password.trim(),
            'username': this.username.trim(),
            'phonenumber': this.phonenumber.trim()
        })
        if (res['flag'] > 0) {
            this.$Message.success('注册成功')
        } else if (res['flag'] === -1) {
            this.$Message.error('注册失败') 
        } else if (res['flag'] === -2) {
            this.$Message.warning('账号已经存在')
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
