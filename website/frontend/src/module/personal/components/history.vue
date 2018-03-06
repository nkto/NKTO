<template>
  <div>
      <historyitem name="[八成新]iPhone8 Plus 128G 黑色" imgUrl="/static/img/ip8.jpg" price="3500 元" state="已卖"></historyitem>
      <historyitem name="[九成新]西部数据 My Passport 1TB 2.5英寸 中国红 移动硬盘" imgUrl="/static/img/ydyp.jpg" price="350 元" state="未卖"></historyitem>
      <historyitem name="[九成新]华为Mate10 Pro 64G 樱粉金" imgUrl="/static/img/hw1.jpg" price="3500 元" state="已卖"></historyitem>
  </div>
</template>
<script>
import historyitem from './historyitem.vue'
export default {
  components: {historyitem},
  data () {
    return {
      ids: ['id1']
    }
  }
}
</script>
<style scoped>

</style>
