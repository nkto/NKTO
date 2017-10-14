<template>
  <div>
    <nktoheader></nktoheader>
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
    <Card class="newitem">
      <div>
        <h2>今日上新</h2>
        <Row>
          <Col span="5" offset="0">
            <Card>
              <img src="/static/img/t1.jpg" class="newitemimg">
            </Card>
          </Col>
          <Col span="5" offset="1">
            <Card>
              <img src="/static/img/t2.jpg" class="newitemimg">
            </Card>
          </Col>
          <Col span="5" offset="1">
            <Card>
              <img src="/static/img/t3.jpg" class="newitemimg">
            </Card>
          </Col>
          <Col span="5" offset="1">
            <Card>
              <img src="/static/img/t4.jpg" class="newitemimg">
            </Card>
          </Col>
        </Row>
      </div>
    </Card>
    <Card class="auctionitem">
      <div>
        <h2>拍卖专区</h2>
        <Row>
          <Col span="5">
            <Card>
              <img src="/static/img/a1.jpg" class="newitemimg">
            </Card>
          </Col>
          <Col span="5" offset="1">
            <Card>
              <img src="/static/img/a2.jpg" class="newitemimg">
            </Card>
          </Col>
          <Col span="5" offset="1">
            <Card>
              <img src="/static/img/a3.jpg" class="newitemimg">
            </Card>
          </Col>
          <Col span="5" offset="1">
            <Card>
              <img src="/static/img/a4.jpg" class="newitemimg">
            </Card>
          </Col>
        </Row>
      </div>
    </Card>
    <BackTop></BackTop>
    <nktofooter></nktofooter>
  </div>
</template>
<script>
  import nktoheader from '../../components/nktoheader.vue'
  import nktofooter from '../../components/nktofooter.vue'
  export default {
    components: {nktoheader, nktofooter},
    data () {
      return {
      }
    },
    methods: {

    }
  }
</script>
<style scoped>
  .img {
    width: 100%;
    height: 300px;
  }
  .carou {
    top: 20vh;
  }
  .classify {
    margin-top: 200px;
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
    width: 250px;
    height: 250px;
  }
  .auctionitem {
    margin-top: 50px;
  }
</style>
