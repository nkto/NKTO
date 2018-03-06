<template>
	<Card :class="aboutstate">
    <Row>
    <Col span="6"><img :src="imgUrl" height="180px"></Col>
      <Col span="15" >
        <div>
          <h2>
            {{name}}
          </h2>
        </div>
				<div class="areyouok">
					<h3>价格：   {{price}}</h3>
					<h3>状态：   {{state}}</h3>
				</div>
      </Col>
      <Col span="8" class="favo" v-if="showfav">
        <Button @click="no">取消收藏</Button>
      </Col>
    </Row>
  </Card>
</template>
<script>
	export default {
		props: ['name', 'imgUrl', 'price', 'state', 'fav'],
		data () {
			return {
				// 由于item组件要给其他不同的组件调用，所以下面的字段会根据上面的type来显示
				aboutstate: '',
				showname: true,
				showprice: true,
				showfav: false,
			}
		},
		methods: {
			no () {
				this.aboutstate = 'no'
			}
		},
		mounted () {
			if (this.state === '已卖') {
				this.aboutstate = 'lg'
			}
			if (this.fav === 'true') {
				this.showfav = true
			}
		}
	}
</script>
<style scoped>
.lg {
	color: lightgray;
}
.no {
	display: none;
}
.areyouok {
	margin-top: 50px;
}
.favo {
	margin-top: 20px;
}
</style>