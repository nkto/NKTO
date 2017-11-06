<template>
    <div class="total" style="height:100%">
    <logoheader></logoheader>
    <hr>
    <Menu :theme="theme3" active-name="1" class="menu">
        <MenuGroup title="个人相关信息" @click.native="transfer('information')">
            <MenuItem name="1">
                <Icon type="settings" ></Icon>
                修改个人信息
            </MenuItem>
        </MenuGroup>
        <MenuGroup title="商品相关">
            <MenuItem name="2" @click.native="transfer('publish')">
                <Icon type="lightbulb"></Icon>
                上架新商品
            </MenuItem>
            <MenuItem name="3" @click.native="transfer('pubed')">
                <Icon type="folder"></Icon>
                发布商品记录
            </MenuItem>
            <MenuItem name="4" @click.native="transfer('collect')">
                <Icon type="bookmark"></Icon>
                查看收藏列表
            </MenuItem>
            <MenuItem name="5" @click.native="transfer('history')">
                <Icon type="compass"></Icon>
                我的浏览历史
            </MenuItem>
            <MenuItem name="6" @click.native="transfer('order')">
                <Icon type="ios-cart-outline"></Icon>
                查看已下订单
            </MenuItem>
        </MenuGroup>
    </Menu>
    <div :is="form" style="height:100%">
    </div>
    <nkto-footer></nkto-footer>
    </div>
</template>
<script>
import logoheader from './components/logoheader'
import nktoFooter from '../../components/nktoFooter'
import collect from './components/collect'
import history from './components/history'
import information from './components/information'
import order from './components/order'
import publish from './components/publish'
import pubed from './components/pubed'
export default {
    components: {collect,history,information,order,publish,pubed,logoheader,nktoFooter},
    data() {
        return {
            form: 'information'
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
 .menu {
     height: 100%;
     float: left;
 }
</style>

