<template>
  <div>
    <nktoHeader></nktoHeader>
    <Carousel autoplay class="carou">
      <CarouselItem>
        <img src="/static/img/zoumadeng.jpg" class="img">
      </CarouselItem>
      <CarouselItem>
        <img src="/static/img/zoumadeng.jpg" class="img">
      </CarouselItem>
      <CarouselItem>
        <img src="/static/img/zoumadeng.jpg" class="img">
      </CarouselItem>
      <CarouselItem>
       <img src="/static/img/zoumadeng.jpg" class="img">
      </CarouselItem>
    </Carousel>
    <Card>
    <p slot="title" class="card-title">专区分类</p>
    <Row class="classify">
      <Col span="4" offset="4">
        <Card :bordered="false">
          <div style="text-align:center">
            <h3>收纳整理专区</h3>
            <img src="/static/img/shouna.jpg" class="classimg">
          </div>
        </Card>
      </Col>
      <Col span="4">
        <Card :bordered="false">
          <div style="text-align:center">
            <h3>教材杂志专区</h3>
            <img src="/static/img/jiaocai.jpg" class="classimg">
          </div>
        </Card>
      </Col>
      <Col span="4">
        <Card :bordered="false">
          <div style="text-align:center">
            <h3>办公文具专区</h3>
            <img src="/static/img/bangong.jpg" class="classimg">
          </div>
        </Card>
      </Col>
      <Col span="4">
        <Card :bordered="false">
          <div style="text-align:center">
            <h3>服装鞋帽专区</h3>
            <img src="/static/img/fushi.jpg" class="classimg">
          </div>
        </Card>
      </Col>
    </Row>
    </Card>
    <Card class="newitem">
      <div>
        <p slot="title" class="card-title">今日上新</p>
        <Row>
          <Col v-for = "(item,index) in newitems" :key = "index "span="5" :offset="index == 0 ? 0 : 1">
            <Card>
              <div style="text-align:center">
              <img :src="item.src" class="newitemimg">
              <p class="goods-name">{{item.name}}</p>
              <div style="margin-bottom:10px">
              <p class="goods-price">{{item.value}}元</p>
              <p class="label" style="">现价:</p>
              </div>
              </div>
            </Card>
          </Col>
        </Row>
      </div>
    </Card>
    <Card class="auctionitem">
      <div>
        <p slot="title" class="card-title">拍卖专区</p>
        <Row>
          <Col span="5">
            <Card>
              <div style="text-align:center">
              <img src="/static/img/a1.jpg" class="newitemimg">
              </div>
            </Card>
          </Col>
          <Col span="5" offset="1">
            <Card>
              <div style="text-align:center">
              <img src="/static/img/a2.jpg" class="newitemimg">
              </div>
            </Card>
          </Col>
          <Col span="5" offset="1">
            <Card>
              <div style="text-align:center">
              <img src="/static/img/a3.jpg" class="newitemimg">
              </div>
            </Card>
          </Col>
          <Col span="5" offset="1">
            <Card>
              <div style="text-align:center">
              <img src="/static/img/a4.jpg" class="newitemimg">
              </div>
            </Card>
          </Col>
        </Row>
      </div>
    </Card>
    <BackTop></BackTop>
    <nktoFooter></nktoFooter>
  </div>
</template>
<script>
  import nktoHeader from '../../components/nktoHeader'
  import nktoFooter from '../../components/nktoFooter'
  export default {
    components: {nktoHeader, nktoFooter},
    data () {
      return {
        newitems: [{
            name: '手机架',
            value: 14,
            src: '/static/img/t1.jpg'
        }, {
            name: '厨具',
            value: 15,
            src: '/static/img/t2.jpg'
        }]
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
      fetchBase (url, body) {
          return fetch(url, {
            method: 'post',
            credentials: 'same-origin',
            headers: {
              'X-CSRFToken': this.getCookie('csrftoken'),
              'Accept': 'application/json',
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(body)
          })
          .then((res) => res.json())
      }
    },
    created: function () {
        fetch('/api/goods/newitems/', {
          method: 'post',
          credentials: 'same-origin',
          headers: {
            'X-CSRFToken': this.getCookie('csrftoken'),
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          }
        }).then((res) => res.json()).then((res) => {
            this.newitems.splice(0, this.newitems.length)
            for (let i = 0; i < res['message'].length; ++i) {
            let data = {}
            data['src'] = res['message'][i]['src']
            data['name'] = res['message'][i]['name']
            data['value'] = res['message'][i]['value']
            this.newitems.push(data)
          }
        })
    }
  }
</script>
<style scoped>
  .img {
    width: 100%;
    height: 400px;
  }
  .carou {
    margin-bottom: 50px;
    margin-left: 0;
    margin-right: 0;
  }
  .classify {
    width: 100%;
  }
  .classimg {
    width: 100px;
    height: 100px;
  }
  .newitem {
    margin-top: 30px;
  }
  .newitemimg {
    width: 100%;
    height: 100%;
  }
  .auctionitem {
    margin-top: 50px;
  }
  .card-title {
    font-size: 20px;
  }
  .goods-name {
    font-size: 18px;
    display: block;
    width: 100%;
    text-align: start;
  }
  .goods-price {
    color: #ca0c4b;
    font-style: italic;
    font-weight: bold;
    text-align: end;
    padding-right: 10px;
    width: fit-content;
    float: right;
  }
  .price {
    display: block;
    width: 100%;
  }
  .label {
    width: fit-content;
    float: right;
    margin-right: 10px;
  }
</style>