<template>
  <div class="customertalk">
    <div id="app">
      <div class="sidebar">
        <card :name="name" :icon="icon"></card>
      </div>
      <div class="main">
        <message :content="content"></message>
        <text-input @onKeyup="send"></text-input>
      </div>
    </div>
  </div>
</template>
<script>
  import Card from './Card'
  import TextInput from './TextInput'
  import Message from './Message'
  export default {
    components: {Card, TextInput, Message},
    props: {
      content: {
        type: Array
      },
      icon: {
        type: String
      },
      name: {
        type: String
      },
      uid: {
        type: String
      }
    },
    methods: {
      send (message) {
        this.$emit('send', message)
      },
      swit (item) {
        this.$emit('swit', item)
      },
      close () {
        this.$emit('close', true)
      },
      transfer () {
        this.$emit('transfer', true)
      }
    }
  }
</script>
<style scoped>
.customertalk {
  display: flex;
}
#app {
  width: 100%;
  height: 75vh;
  overflow: hidden;
  border-radius: 3px;
}
#app .sidebar, #app .main {
  height: 100%;
}
#app .sidebar {
  float: left;
  width: 20%;
  color: #f4f4f4;
  background-color: #2d8cf0;
}
#app .main {
  position: relative;
  overflow: hidden;
  background-color: #eee;
}
#app .text {
  position: absolute;
  width: 100%;
  bottom: 0;
  left: 0;
}
#app .message {
  height: calc(100% - 160px);
}
.userinfo {
  width: 30%;
}
.buttongroup {
  margin-top: 20%;
}
.button {
  margin-left: 10%;
}
</style>