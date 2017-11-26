<template>
  <ul>
      <item v-for="id in ids" :id="id" type="order"></item>
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
