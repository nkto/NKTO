<template>
  <div class="header">
    <img src="/static/img/logo.jpg" class="img">
    <Input icon="search" class="search" placeholder="请输入搜索内容"></Input>
    <div class="car">我的购物车</div>
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
</template>
<script>
</script>
<style scoped>
  .img {
    width: 100px;
    height: 100px;
    position: absolute;
    left: 7%;
  }
  .search {
    position: absolute;
    width: 300px;
    margin-left: 30%;
    margin-top: 3%;
  }
  .menu {
    position: absolute;
    top: 12%;
    left: 20%;
    width: 80%;
  }
  .car {
    position: absolute;left: 60%;
    position: absolute;top: 5%;
    height: 6%;
    width: 10%;
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
    padding-top: 15px;
  }
</style>
