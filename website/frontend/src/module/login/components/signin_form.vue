<template>
    <div class="form">
    <Input v-model="username" placeholder="注册邮箱/手机号" class="input" type="text"></Input>
    <Input v-model="password" placeholder="密码" class="input" type="password"></Input>
    <div class="input">
        <Input v-model="vertifycode" placeholder="验证码" class="vertifycode-input" type="text"></Input>
        <img src="/static/img/a1.jpg" class="vertifycode-img"/>
    </div>
    <Button type="primary" shape="circle" class="input input-btn">登录</Button>
    </div>
</template>
<script>
export default {
  
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
