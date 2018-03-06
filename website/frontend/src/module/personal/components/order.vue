<template>
  <ul>
    <item name="[八成新] 书支架" dealtime="2017/08/02 12:30 pm" dealpos="津南 理科食堂一楼" cate="日用品" state="finished" uptime="2017/11/01" price="34 元" imgUrl="/static/img/t1.jpg"></item>
    <item name="[十成新] 扫把" dealtime="2018/03/01 17:20 pm" dealpos="津南 理科5A宿舍" cate="日用品" state="finished" uptime="2018/02/05" price="10 元" imgUrl="/static/img/saoba.jpg"></item>
  </ul>
</template>
<script>
import item from './item.vue'
export default {
  components: {item},
  data () {
    return {
      ids: ['id1', 'id2']
    }
  },
  created () {
    // 从数据库获取所有order的id，然后将id和type传给item
  }
}
</script>
<style scoped>

</style>
