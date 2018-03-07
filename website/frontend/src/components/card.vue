<template>
<div class="card">
  <header>
    <img class="avatar" width="40" height="40" :src="icon">
    <p class="name">{{ name }}</p>
  </header>
</div>
</template>
<script>
  export default {
    props: {
      icon: {
        type: String
      },
      name: {
        type: String
      }
    }
  }
</script>
<style scoped lang="less" scoped>
.card {
  padding: 12px;
  border-bottom: solid 1px #24272C;
  .avatar, .name {
    vertical-align: middle;
  }
  .avatar {
    border-radius: 2px;
  }
  .name {
    display: inline-block;
    margin: 0 0 0 15px;
    font-size: 16px;
  }
}
</style>
