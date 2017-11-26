<template>
<Row type="flex" justify="center" align="middle">
    <Col span="4">
    <Button type="ghost" shape="circle" class="avatar-btn" @click.native="signin()"><Icon type="person" size="30"></Icon></Button>
    </Col>
    <Col span="4">
    <Button class="login-btn" type="text" @click.native="signin()">尚未注册?&emsp;<br>开启新世界大门！</Button>
    </Col>
</Row>
</template>
<script>
export default {
  methods: {
    signin () {
      location.href = '/signin/'
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
  .login-btn {
    font-size: 15px;
  }
</style>

