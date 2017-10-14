<template>
  <div id="app">
    <div class="sidebar">
      {{ name }}
    </div>
    <Button type="primary" @click="func">点击改变</Button>
  </div>
</template>
<script>
  export default {
    data () {
      return {
        name: 'this is a test'
      }
    },
    methods: {
      func () {
        this.name = 'this is not a test'
      }
    }
  }
</script>
<style scoped>
#app {
  margin: 20px auto;
  width: 800px;
  height: 600px;
  overflow: hidden;
  border-radius: 3px;
}
</style>
