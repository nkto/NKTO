<template>
  <div id="app">
    <div class="head">
      <Input v-model="searchWord" @on-enter="search" placeholder="输入ID,邮箱,姓名查找用户" class="search-input"></Input>
      <Button @click="search">查询</Button>
      <div class="head-right">
      </div>
			<div class="head-right">
        <Select v-model="sortKeyWord" @on-change="changeSort" style="width:12vw;text-align:left;">
          <Option v-for="item of sortList" :value="item" :key="item">{{ item }}</Option>
        </Select>
        <Select v-model="sortOrder" @on-change="changeSort" style="width:12vw;text-align:left;margin-left:1vw;">
          <Option v-for="item of orderList" :value="item" :key="item">{{ item }}</Option>
        </Select>
      </div>
    </div>
    <Row class="table">
        <Table border :columns="goodsForm" :data="goodsDataShow" ref="table"></Table>
        <Page :total="goodsData.length" @on-change="changePage" :page-size="pageSize" style="margin-top:1vh;"></Page>
    </Row>
    <br>
    <Button type="primary" size="large" @click="exportData(1)"><Icon type="ios-download-outline"></Icon> 导出原始数据</Button>
    </div>
</template>
<script>
  export default {
    data () {
      return {
        stateMap: {
          '0': '在售',
          '1': '已售'
        }, // (要改)
        sortList: ['按关键字排序', '交易价格', '交易时间', '交易地点', '买家ID', '商品ID', '交易状态'], // 排序的所有关键字(要改)
        sortKeyWord: '按关键字排序', // 排序关键字
        sortOrder: '升序', // 升序或降序
        orderList: ['升序', '降序'],
        searchWord: '', // 搜索用户的关键词
        goodsEmail: '', // 邀请用户输入的邮箱
        goodsForm: [
          {
            'title': 'ID',
            'key': 'pid'
          }, {
            'title': '买家ID',
            'key': 'uid'
          }, {
            'title': '商品ID',
            'key': 'gid'
          }, {
            'title': '交易状态',
            'key': 'state'
          }, {
            'title': '交易时间',
            'key': 'tran_time'
          }, {
            'title': '交易价格',
            'key': 'tran_price'
          }, {
            'title': '交易地点',
            'key': 'tran_place'
          }
        ], // 用户表格格式
        goodsDataAll: [], // 所有用户数据
        goodsData: [], // 所有页面数据
        goodsDataShow: [], // 当前页的用户数据
        current: 1, // 当前页码
        pageSize: 10 // 每页数据条数
      }
    },
    methods: {
      init (iWantToChangePage) {
        // 根据当前情况将goodsDataAll中的数据传给goodsData和goodsDataShow
        this.goodsData = []
        if (this.searchWord.trim() === '') {
          this.goodsData = this.goodsDataAll
        } else {
          for (let i = 0; i < this.goodsDataAll.length; ++i) {
            if (this.goodsDataAll[i]['pid'].indexOf(this.searchWord) !== -1 ||
				this.goodsDataAll[i]['uid'].indexOf(this.searchWord) !== -1 ||
                this.goodsDataAll[i]['gid'].indexOf(this.searchWord) !== -1 ||
                this.goodsDataAll[i]['tran_time'].indexOf(this.searchWord) !== -1 ||
                this.goodsDataAll[i]['tran_place'].indexOf(this.searchWord) !== -1 ||
                this.goodsDataAll[i]['gid'].indexOf(this.searchWord) !== -1 ||
                this.goodsDataAll[i]['state'].indexOf(this.searchWord) !== -1) {
              this.goodsData.push(this.goodsDataAll[i])
            }
          }
        }
        if (iWantToChangePage) {
          this.goodsDataShow = this.goodsData.slice(0, Math.min(this.pageSize, this.goodsData.length))
          this.current = 1
        } else {
          this.goodsDataShow = this.goodsData.slice((this.current - 1) * this.pageSize, Math.min((this.current - 1) * this.pageSize + this.pageSize, this.goodsData.length))
        }
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
      },
      checkEmail (email) {
        var ePattern = /^([A-Za-z0-9])+@([A-Za-z0-9])+\.([A-Za-z]{2,4})$/g
        return ePattern.test(email)
      },
      changePage (current) {
        this.current = current
        this.init(false)
      },
      changeState (index) {
        // 修改用户状态
        let pid = this.goodsDataShow[index].pid
        let state = this.goodsDataShow[index].state
        let newState = ''
        if (state === this.stateMap['-1']) {
          newState = this.stateMap['0']
        } else if (state === this.stateMap['0']) {
          newState = this.stateMap['1']
        } else if (state === this.stateMap['1']) {
          newState = this.stateMap['2']
        } else if (state === this.stateMap['2']) {
          newState = this.stateMap['3']
        } else if (state === this.stateMap['3']) {
          newState = this.stateMap['-1']
        }
        for (let i = 0; i < this.goodsDataAll.length; ++i) {
          if (this.goodsDataAll[i].pid === pid) {
            this.goodsDataAll[i].state = newState
            this.goodsDataShow[index].state = newState
            break
          }
        }
        // 向服务器发送修改用户状态请求(先空着)
        this.$Message.success('状态修改成功')
      },
      search () {
        // 根据信息查找用户，支持模糊查询
        this.init(true)
        this.searchWord = ''
      },
      changeSort () {
        // 排序（需要修改）
        let key = ''
        if (this.sortKeyWord === '交易价格') {
          key = 'tran_price'
        } else if (this.sortKeyWord === '交易地点') {
          key = 'tran_place'
        } else if (this.sortKeyWord === '交易时间') {
          key = 'tran_time'
        } else if (this.sortKeyWord === '买家ID') {
          key = 'uid'
        } else if (this.sortKeyWord === '交易状态') {
          key = 'state'
        } else if (this.sortKeyWord === '按关键字排序') {
          return
        }
        let num = 1
        if (this.sortOrder === '降序') {
          num = -1
        }
        this.goodsData.sort((item1, item2) => {
          if (item1[key] > item2[key]) {
            return num
          } else if (item1[key] < item2[key]) {
            return -num
          } else {
            return 0
          }
        })
        this.init(true)
      },
      exportData (type) {
        // 根据传入的type导出不同的数据
        let csv = '\ufeff'
        let keys = []
        let temp = this.goodsDataAll
        if (type === 2) {
          temp = this.goodsData
        }
        this.goodsForm.forEach(function (item) {
          csv += '"' + item['title'] + '",'
          keys.push(item['key'])
        })
        csv = csv.replace(/,$/, '\n')
        temp.forEach(function (item) {
          keys.forEach(function (key) {
            csv += '"' + item[key] + '",'
          })
          csv = csv.replace(/,$/, '\n')
        })
        var blob = new window.Blob([csv], {
          type: 'text/csv,charset=UTF-8'
        })
        let csvUrl = window.URL.createObjectURL(blob)
        let a = document.createElement('a')
        a.download = '用户.csv'
        a.href = csvUrl
        document.body.appendChild(a)
        a.click()
        document.body.removeChild(a)
      },
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
      }
    },
    mounted () {
      // 初始化用户信息，这里应该是从数据库中获取到数据的，但是先手动模拟
      this.goodsDataAll = [
        {'pid': '001', 'uid': 'uid1', 'tran_price': 3.5, 'gid': 'gid1', 'tran_place': '小树林', 'tran_time': new Date(), 'state': this.stateMap['1']},
        {'pid': '002', 'uid': 'uid2', 'tran_price': 3.5, 'gid': 'gid2', 'tran_place': '小树林', 'tran_time': new Date(), 'state': this.stateMap['0']},
        {'pid': '003', 'uid': 'uid3', 'tran_price': 3.5, 'gid': 'gid3', 'tran_place': '小树林', 'tran_time': new Date(), 'state': this.stateMap['1']},
        {'pid': '004', 'uid': 'uid4', 'tran_price': 34.5, 'gid': 'gid1', 'tran_place': '小树林', 'tran_time': new Date(), 'state': this.stateMap['0']},
        {'pid': '005', 'uid': 'uid5', 'tran_price': 5.6, 'gid': 'gid1', 'tran_place': '小树林', 'tran_time': new Date(), 'state': this.stateMap['1']},
        {'pid': '006', 'uid': 'uid6', 'tran_price': 30.5, 'gid': 'gid1', 'tran_place': '小树林', 'tran_time': new Date(), 'state': this.stateMap['1']},
        {'pid': '007', 'uid': 'uid7', 'tran_price': 3.5, 'gid': 'gid1', 'tran_place': '小树林', 'tran_time': new Date(), 'state': this.stateMap['1']},
        {'pid': '008', 'uid': 'uid8', 'tran_price': 3.5, 'gid': 'gid1', 'tran_place': '小树林', 'tran_time': new Date(), 'state': this.stateMap['0']},
        {'pid': '009', 'uid': 'uid9', 'tran_price': 3.25, 'gid': 'gid1', 'tran_place': '小树林', 'tran_time': new Date(), 'state': this.stateMap['1']},
        {'pid': '0010', 'uid': 'uid10', 'tran_price': 3.5, 'gid': 'gid1', 'tran_place': '小树林', 'tran_time': new Date(), 'state': this.stateMap['1']},
        {'pid': '0011', 'uid': 'uid11', 'tran_price': 23.5, 'gid': 'gid1', 'tran_place': '小树林', 'tran_time': new Date(), 'state': this.stateMap['1']},
        {'pid': '0012', 'uid': 'uid12', 'tran_price': 3.5, 'gid': 'gid1', 'tran_place': '小树林', 'tran_time': new Date(), 'state': this.stateMap['0']}
      ]
      this.init(true)
    }
  }
</script>
<style scoped>
.search-input {
  width: 15%;
  height: 5%;
}
.table {
  margin-top: 2vh;
}
.head {
  display: block;
  width: 100%;
}
.head-left {
  display: inline-block;
  width: 35%;
}
.head-right {
  display: inline-block;
  position: absolute;
  right: 28px;
  width: 50%;
  text-align: right;
}
.head-right span {
  text-align: left;
}
</style>