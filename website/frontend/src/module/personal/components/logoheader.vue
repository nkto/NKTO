<template>
  <div class="header">
    <Row type="flex" justify="center" align="middle">
      <Col span="3"><img src="/static/img/logo.jpg" class="img hov" @click="gotoHome" /></Col>
      <Col span="21"></Col>
    </Row>
  </div>
</template>
<script>
  export default {
    methods: {
      gotoHome () {
        this.$Message.warning('fuck')
        location.href = '/'
      }
    }
  }
</script>
<style scoped>
  .img {
    width: 150px;
    height: 100px;
    margin-left: 30px;
  }
  .search {
    width: 300px;
    margin-left:30px
  }
  .hov:hover {
    cursor: pointer;
  }
</style>