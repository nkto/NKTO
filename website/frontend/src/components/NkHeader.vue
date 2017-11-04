<template>
  <div class="header">
    <img src="/static/logo.jpg" class="img">
    <Input icon="search" class="search" placeholder="请输入搜索内容"></Input>
    <div class="car">我的购物车</div>
    <div>
      <div class="bg"></div>
      <div class="shouye">首页</div>
      <Menu mode="horizontal" theme="primary" active-name="1" class="menu">
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
</script>
<style scoped>
  .img {
    width: 100px;
    height: 100px;
    margin-left: 7%;
  }
  .search {
    width: 300px;
    margin-left: 25%;
    margin-top: -45px;
  }
  .menu {
    width: 82%;
    display: inline-block;
  }
  .car {
    display: inline-block;
    overflow: hidden;
    height: 70px;
    width: 10%;
    margin-left: 150px;
    outline: none;
    border:  1px solid#C0C0C0;
    background-color: #FFFFFF;
    background-image: url('/static/car.jpg');
    background-size: 40px 40px;
    background-repeat: no-repeat;
    background-position: 2%;
    font-family: "宋体";
    font-size: 15px;
    padding-left: 60px;
    padding-top: 20px;
  }
  .bg {
    display: inline-block;
    width: 10%;
    padding-top: 60px;
    overflow: hidden;
    background-color: #eb6133;
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