<template>
    <div class="total">
        <div class="logo-div">
        <img src="/static/img/NKTO logo1.png" class="logo"/>
        </div>
        <!-- 注册登录选择栏 -->
        <Row>
        <Col span="6" offset="9">
        <Menu mode="horizontal" :theme="theme1" active-name="1" class="login-menu">
        <Row>
        <Col span="18">
        <MenuItem name="1" @click.native="transfer('signin_form')">
            登录
        </MenuItem>
        </Col>
        <Col span="6">
        <MenuItem name="2" @click.native="transfer('signup_form')">
            注册
        </MenuItem>
        </Col>
        </Row>
        </Menu>
        </Col>
        </Row>
        <div :is="form">
        </div>
    </div>
</template>
<script>
import signin_form from './components/signin_form'
import signup_form from './components/signup_form'
export default {
    components: {signin_form,signup_form},
    data() {
        return {
            form: 'signin_form'
        }
    },
    methods: {
        transfer(newform) {
            this.form = newform
        }
  }
}
</script>
<style scoped>
 .total {
     background-image: url("/static/img/background.jpeg");
     height: 100%;
 }
 .logo-div {
     width:100%;
     text-align: center;
     padding-top: 100px;
 }
 .logo {
     height: 200px;
 }
 .login-menu {
     background: transparent;
 }
</style>

