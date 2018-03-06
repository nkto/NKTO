<template>
  <div>
      <item v-for="id in ids" :id="id" type="history"></item>
  </div>
</template>
<script>
import item from './item.vue'
export default {
  components: {item},
  data () {
    return {
      ids: ['id1']
    }
  }
}
</script>
<style scoped>

</style>
