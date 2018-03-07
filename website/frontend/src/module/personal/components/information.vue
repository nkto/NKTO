<template>
  <div>
    <Card dis-hover class="card">
        <p slot="title">修改头像</p>
        <Row>
            <Col span="12">
                <div>
                  <p>当前头像</p>
                  <Avatar src="/static/img/shouna.jpg" shape="circle" />
                </div>
            </Col>
            <Col span="12">
              <div>
                <Upload action="" :before-upload="handleUpload" >
                  <Button type="ghost" icon="ios-cloud-upload-outline" >上传头像</Button>
                </Upload>
                <img :src="upload" class="image" v-show="show" />
              </div>
            </Col>
        </Row>
    </Card>
    <Card dis-hover class="card">
        <p slot="title">更改个人设置</p>
    </Card>
  </div>
</template>
<script>
export default {
    data () {
      return {
        show: false,
        upload: ''
      }
    },
    methods: {
      getCookie (cName) {
        if (document.cookie.length > 0) {
          let cStart = document.cookie.indexOf(cName + '=')
          if (cStart !== -1) {
            cStart = cStart + cName.length + 1
            let cEnd = document.cookie.indexOf(';', cStart)
            if (cEnd === -1) {
              cEnd = document.cookie.length
            }
            return unescape(document.cookie.substring(cStart, cEnd))
          }
        }
        return ''
      },
      handleUpload (file) {
        /* global FormData: true */
        let image = new FormData()
        image.append('image', file)
        fetch('/api/user/storeimage/', {
          method: 'post',
          credentials: 'same-origin',
          headers: {
            'X-CSRFToken': this.getCookie('csrftoken'),
            'Accept': 'application/json'
          },
          body: image
        }).then((res) => res.json()).then((res) => {
          this.upload = res['url']
          this.show = true
        })
        return false
      }
    }
}
</script>
<style scoped>
 .card {
     width: 100%;
     margin-top: 10px;
 }
 .image {
    max-height: 310px;
 }
</style>
