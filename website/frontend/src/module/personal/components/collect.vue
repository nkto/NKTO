<template>
  <div>
      <historyitem name="[八成新]Vivo X20 128G 金色" imgUrl="/static/img/vivo.jpg" price="2500 元" state="已卖" fav="true"></historyitem>
      <historyitem name="[八成新]华硕飞行堡垒四代 GTX1060 6G 15.6英寸 i5-7300HQ 128GSSD+1T 黑色" imgUrl="/static/img/hs.jpg" price="6900 元" state="已卖" fav="true"></historyitem>
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
