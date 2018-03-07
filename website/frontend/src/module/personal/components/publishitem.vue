<template>
	<Card>
    <Row :class="gl">
    <Col span="6"><img :src="imgUrl" height="180px"></Col>
      <Col span="15" >
        <div>
          <h2>
            {{name}}
          </h2>
        </div>
        <div style ="margin-top: 20px">
          <h4>名称：   {{name}}</h4>
          <h4>原价：   {{yuanjia}}</h4>
          <h4>新旧程度：   {{xinjiu}}</h4>
          <h4>购买日期：   {{date}}</h4>
          <h4>详细情况：   {{detail}}</h4>
          <h4>售价：   {{price}}</h4>
          <h3>状态：   {{state}}</h3>
        </div>
      </Col>
      <Col span="8" class="finished" v-if="state  === '已卖'">
        <img src="/static/img/ysc.png" alt="" class="finished-red">
      </Col>
      <Col span="8" class="afinished" v-if="state === '未卖'">
        <Button>编辑</Button>
      </Col>
    </Row>
  </Card>
</template>
<script>
	export default {
		props: ['name', 'yuanjia', 'xinjiu', 'date', 'detail', 'price', 'imgUrl', 'state'],
		data () {
			return {
				// 由于item组件要给其他不同的组件调用，所以下面的字段会根据上面的type来显示
				showname: true,
				showdealtime: true,
				showdealpos: true,
				showcate: true,
				showstate: true,
				showuptime: true,
        showprice: true,
        gl: '',
			}
		},
		mounted () {
      if (this.state === '已卖') {
        this.gl = 'lg'
      }
		}
	}
</script>
<style scoped>
.lg {
  color: lightgray;
}
.afinished-red {
  width: 200px;
  height: 200px;
}
.afinished {
  position: absolute;
  text-align: right;
  right: 30px;
  top: -10px;
}
.finished-red {
  width: 200px;
  height: 200px;
}
.finished {
  position: absolute;
  right: 130px;
}
</style>