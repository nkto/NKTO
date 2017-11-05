<template>
  <div>
    <nkto-header></nkto-header>
    <Carousel autoplay class="carou">
      <CarouselItem v-for="item in picturelist">
        <img :src="item" class="img">
      </CarouselItem>
    </Carousel>
    <div class="detail">
      <Card dis-hover>
        <h1>商品名称： {{ name }}</h1>
        <h2>价格:&nbsp;&nbsp;&nbsp;<span class="price">{{ price }}</span></h2>
        <h2>原价:&nbsp;&nbsp;&nbsp;<span class="price">{{ originalprice }}</span></h2>
      </Card>
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
  export default {
    components: {nktoHeader, nktoFooter},
    data () {
      return {
        picturelist: [],
        name: '笔记本',
        price: '150',
        originalprice: '300'
      }
    },
    methods: {

    },
    created: function () {
      this.picturelist.push('/static/p1.jpg')
      this.picturelist.push('/static/p2.jpg')
      this.picturelist.push('/static/p3.jpg')
    }
  }
</script>
<style scoped>
  .carou {
    margin: 50px 0;
    width: 700px;
    margin-left: 200px;
    display: inline-block;
  }
  .img {
    max-width: 730px;
    max-height: 490px;
    margin-left: 100px;
  }
  .detail {
    display: inline-block;
    height: 500px;
    width: 500px;
    overflow: hidden;
  }
  .price {
    color: red;
    font-size: 2em;
  }
  .allpicture {
    margin-left: 300px;
    width: 600px;
  }
  .smallimg {
    max-width: 96px;
    max-height: 60px;
  }
</style>