<template>
  <div>
    <nkto-header></nkto-header>
    <Carousel autoplay class="carou">
      <CarouselItem v-for="item in picturelist">
        <img :src="item" class="img">
      </CarouselItem>
    </Carousel>
    <div class="detail">
      <Card dis-hover :shadow="true" class="card">
        <h1 class="h1">商品名称： {{ name }}</h1>
        <Form :model="formItem" :label-width="80">
          <FormItem label="商品原价">
            <Input v-model="formItem.price" class="input" disabled></Input>
          </FormItem>
          <FormItem label="商品现价">
            <Input v-model="formItem.shijia" class="input" disabled></Input>
          </FormItem>
          <FormItem label="新旧程度">
            <Select v-model="formItem.xinjiu" class="input" disabled>
            </Select>
          </FormItem>
          <FormItem label="购买日期">
            <Row>
              <Col span="11">
                <FormItem prop="date">
                  <DatePicker type="date" v-model="formItem.date" disabled></DatePicker>
                </FormItem>
              </Col>
            </Row>
          </FormItem>
          <FormItem label="详细情况">
            <Input v-model="formItem.textarea" type="textarea" :autosize="{minRows: 2,maxRows: 5}" class="input"></Input>
          </FormItem>
        </Form>
      </Card>
      <Button type="primary" @click="display1">与卖家聊天</Button>
      <Modal v-model="modal1" width="700">
        <customer-talk  @send="send" :content="currentcontent" :name="usrname" :uid="uid"></customer-talk>
        <div slot="footer"></div>
      </Modal>
      <Button type="primary" @click="display2">通知卖家</Button>
      <Modal v-model="modal2" width="700">
        <Form :model="checkplace" :label-width="80">
          <FormItem label="约定地点">
            <Select v-model="checkplace.place" class="input">
              <Option value="1">理科食堂</Option>
              <Option value="2">文科食堂</Option>
              <Option value="3">图书馆</Option>
            </Select>
          </FormItem>
          <FormItem label="约定时间">
            <Select v-model="checkplace.time" class="input">
              <Option value="1">12:30</Option>
              <Option value="2">16:30</Option>
              <Option value="3">20:30</Option>
            </Select>
          </FormItem>
        </Form>
      </Modal>
    </div>
    <Card class="allpicture" dis-hover>
      <Row>
        <Col v-for="item in picturelist" span="4" offset="1">
          <Card>
            <img :src="item" class="smallimg">
          </Card>
        </Col>
      </Row>
    </Card>
    <nkto-footer></nkto-footer>
  </div>
</template>
<script>
  import nktoHeader from '../../components/nktoHeader'
  import nktoFooter from '../../components/nktoFooter'
  import CustomerTalk from '../../components/CustomerTalk'
  export default {
    components: {nktoHeader, nktoFooter, CustomerTalk},
    data () {
      return {
        picturelist: [],
        name: '笔记本',
        price: '150',
        originalprice: '300',
        modal1: false,
        modal2: false,
        formItem: {
          name: '',
          xiniju: '',
          price: '',
          date: '',
          textarea: '',
          category: '',
          shijia: ''
        },
        checkplace: {
          place: '',
          time: ''
        },
        socket: null,
        usrname: '',
        uid: '0',
        currentcontent: [],
      }
    },
    methods: {
      dateformat (date) {
        let seperator1 = '-'
        let seperator2 = ':'
        let month = date.getMonth() + 1
        let strDate = date.getDate()
        if (month >= 1 && month <= 9) {
          month = '0' + month
        }
        if (strDate >= 0 && strDate <= 9) {
          strDate = '0' + strDate
        }
        var currentdate = date.getFullYear() + seperator1 + month + seperator1 + strDate + ' ' + date.getHours() + seperator2 + date.getMinutes() + seperator2 + date.getSeconds()
        return currentdate
      },
      display1() {
        this.modal1 = true
        if (this.socket === null) {
          this.socket = io.connect('http://' + document.domain + ':' + location.port + '/test')
          console.log(document.domain)
          console.log(location.port)
          this.socket.emit('connected', {uid: this.uid})
          this.myResponse()
        }
      },
      display2() {
        this.modal2 = true
      },
      myResponse () {
        this.socket.on('getresponse', (msg) => {
          let data = {}
          data['word'] = decodeURI(msg['data'])
          data['self'] = false
          data['time'] = msg['time']
          data['src'] = decodeURI(msg['src'])
          this.currentcontent.push(data)
        })
      },
      send (msg) {
        let data = {}
        data['word'] = msg
        data['self'] = true
        data['time'] = this.dateformat(new Date())
        data['src'] = '/static/img/user.png'
        this.currentcontent.push(data)
        this.socket.emit('sendmessage', {data: encodeURI(msg), time: data['time'], src: encodeURI(data['src']), uid: this.uid})
      },
    },
    created: function () {
      this.picturelist.push('/static/img/a1.jpg')
      this.picturelist.push('/static/img/a2.jpg')
      this.picturelist.push('/static/img/a3.jpg')
    }
  }
</script>
<style scoped>
  .h1{
    margin-left: 10px;
  }
  .input{
    width: 75%;
  }
  .carou {
    margin: 50px 0;
    width: 700px;
    margin-left: 200px;
    display: inline-block;
  }
  .ivu-card-body{
    background-color: #ffffee;
  }
  .card{
    background-color: #f2f2f2;
    margin-top: 30px;
  }
  .img {
    max-width: 730px;
    max-height: 490px;
    margin-left: 100px;
    margin-bottom: 100px;
  }
  .detail {
    display: inline-block;
    width: 500px;
  }
  .price {
    color: red;
    font-size: 2em;
  }
  .allpicture {
    margin-left: 150px;
    width: 600px;
  }
  .smallimg {
    max-width: 96px;
    max-height: 60px;
  }
</style>