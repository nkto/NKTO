<template>
<Row type="flex" justify="center" align="middle">
    <Col span="6">
    <Dropdown placement="bottom-start">
        <Button type="ghost" shape="circle" class="avatar-btn"><Img class="user-avatar" src="/static/img/a3.jpg"/></Button>
        <DropdownMenu slot="list">
            <DropdownItem >修改个人信息<Icon type="settings" style="margin-left:3px;"></Icon></DropdownItem>
            <DropdownItem >查看收藏列表<Icon type="bookmark" style="margin-left:5px;"></Icon></DropdownItem>
            <DropdownItem >历史浏览记录<Icon type="compass" style="margin-left:3px;"></Icon></DropdownItem>
            <DropdownItem divided>注销</DropdownItem>
        </DropdownMenu>
    </Dropdown>
    </Col>
    <Col span="9">
    <Button class="pub-btn" type="ghost" shape="circle" icon="lightbulb">发布新商品</Button>
    </Col>
    <Col span="9">
    <Button class="pub-btn" type="ghost" shape="circle" icon="ios-cart-outline">查看已下订单</Button>
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
  .pub-btn {
    font-size: 15px;
  }
</style>

