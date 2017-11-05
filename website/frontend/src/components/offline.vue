<template>
<Row type="flex" justify="center" align="middle">
    <Col span="4">
    <Button type="ghost" shape="circle" class="avatar-btn"><Img class="user-avatar" src="/static/img/user.png"/></Button>
    </Col>
    <Col span="4">
    <Button class="login-btn" type="text">尚未登录？点我注册</Button>
    </Col>
</Row>
</template>
<script>
export default {
  
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
  .login-btn {
    font-size: 15px;
  }
</style>

