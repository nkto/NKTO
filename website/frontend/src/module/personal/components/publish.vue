<template>
  <div>
    <p class="wenzi">请上传商品图片</p>
    <div class="demo-upload-list" v-for="item in uploadList">
        <template v-if="item.status === 'finished'">
            <img :src="item.url">
            <div class="demo-upload-list-cover">
                <Icon type="ios-eye-outline" @click.native="handleView(item.name)"></Icon>
                <Icon type="ios-trash-outline" @click.native="handleRemove(item)"></Icon>
            </div>
        </template>
        <template v-else>
            <Progress v-if="item.showProgress" :percent="item.percentage" hide-info></Progress>
        </template>
    </div>
    <Upload
        ref="upload"
        :show-upload-list="false"
        :default-file-list="defaultList"
        :format="['jpg','jpeg','png']"
        :max-size="2048"
        :on-format-error="handleFormatError"
        :on-exceeded-size="handleMaxSize"
        :before-upload="handleBeforeUpload"
        action=""
        multiple
        type="drag"
        style="display: inline-block;width:58px;">
        <div style="width: 58px;height:58px;line-height: 58px;">
            <Icon type="camera" size="20"></Icon>
        </div>
    </Upload>
    <Modal title="View Image" v-model="visible">
        <img :src="'https://o5wwk8baw.qnssl.com/' + imgName + '/large'" v-if="visible" style="width: 100%">
    </Modal>
     <Form :model="formItem" :label-width="80">
      <FormItem label="商品名称">
        <Input v-model="formItem.name" placeholder="请输入名称" class="input"></Input>
      </FormItem>
      <FormItem label="商品原价">
        <Input v-model="formItem.price" placeholder="请输入价格" class="input"></Input>
      </FormItem>
      <FormItem label="商品类别">
        <RadioGroup v-model="formItem.category">
          <Radio label="book">书籍</Radio>
          <Radio label="cloth">电子产品</Radio>
          <Radio label="electric">服饰</Radio>
          <Radio label="daily">生活用品</Radio>
          <Radio label="other">其他</Radio>
        </RadioGroup>
      </FormItem>
      <div class="special" v-show="formItem.category != ''">
        <Form :model="specialform" :label-width="80">
          <div v-if="formItem.category=='book'">
            <FormItem label="是否折角">
              <i-switch v-model="specialform.zhejiao">
                <span slot="open">On</span>
                <span slot="close">Off</span>
              </i-switch>
            </FormItem>
            <FormItem label="笔记情况">
              <Select v-model="specialform.biji" class="input">
                <Option value="1">几乎没有</Option>
                <Option value="2">较多</Option>
                <Option value="3">十分详细</Option>
              </Select>
            </FormItem>
            <FormItem label="破损情况">
              <Select v-model="specialform.posun" class="input">
                <Option value="4">几乎没有</Option>
                <Option value="5">较严重</Option>
                <Option value="6">十分严重</Option>
              </Select>
            </FormItem>
          </div>
          <div v-else>
            <FormItem label="是否保修">
              <i-switch v-model="specialform.baoxiu">
                <span slot="open">On</span>
                <span slot="close">Off</span>
              </i-switch>
            </FormItem>
            <FormItem label="破损情况">
              <Select v-model="specialform.posun" class="input">
                <Option value="7">几乎没有</Option>
                <Option value="8">较严重</Option>
                <Option value="9">十分严重</Option>
              </Select>
            </FormItem>
          </div>
        </Form>
      </div>
      <FormItem label="新旧程度">
        <Select v-model="formItem.xinjiu" class="input">
          <Option value="1">1</Option>
          <Option value="2">2</Option>
          <Option value="3">3</Option>
          <Option value="4">4</Option>
          <Option value="5">5</Option>
          <Option value="6">6</Option>
          <Option value="7">7</Option>
          <Option value="8">8</Option>
          <Option value="9">9</Option>
        </Select>
      </FormItem>
      <FormItem label="购买日期">
        <Row>
          <Col span="11">
            <FormItem prop="date">
              <DatePicker type="date" placeholder="Select date" v-model="formItem.date"></DatePicker>
            </FormItem>
          </Col>
        </Row>
      </FormItem>
      <FormItem label="详细情况">
        <Input v-model="formItem.textarea" type="textarea" :autosize="{minRows: 2,maxRows: 5}" placeholder="描述商品具体情况" class="input"></Input>
      </FormItem>
      <FormItem label="估计价格" v-if="formItem.gujia !=''" disabled>
        <Input v-model="formItem.gujia" class="input"></Input>
      </FormItem>
      <FormItem label="实际定价">
        <Input v-model="formItem.shijia" placeholder="请输入价格" class="input"></Input>
      </FormItem>
      <FormItem>
        <Button type="primary" @click="generate()">生成估价</Button>
        <Button type="primary" @click="submit()">提交</Button>
      </FormItem>
     </Form>

  </div>
</template>
<script>
  export default {
    data () {
      return {
        defaultList: [],
        imgName: '',
        visible: false,
        uploadList: [],
        formItem: {
          name: '',
          xiniju: '',
          price: '',
          date: '',
          textarea: '',
          category: '',
          gujia: '',
          shijia: ''
        },
        specialform: {
          biji: '',
          zhejiao: '',
          posun: '',
          baoxiu: ''
        }
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
      },
      async generate() {
        let res = await this.fetchBase('/api/goods/generate/', {
          'formitem': this.formItem,
          'special': this.specialform
        })
        this.formItem.gujia = res['price']
      },
      handleView (name) {
        this.imgName = name;
        this.visible = true;
      },
      handleRemove (file) {
        const fileList = this.$refs.upload.fileList;
        this.$refs.upload.fileList.splice(fileList.indexOf(file), 1);
      },
      handleFormatError (file) {
        this.$Notice.warning({
          title: 'The file format is incorrect',
          desc: 'File format of ' + file.name + ' is incorrect, please select jpg or png.'
        });
      },
      handleMaxSize (file) {
        this.$Notice.warning({
          title: 'Exceeding file size limit',
          desc: 'File  ' + file.name + ' is too large, no more than 2M.'
        });
      },
      handleBeforeUpload (file) {
        const check = this.uploadList.length < 5;
        if (!check) {
          this.$Notice.warning({
            title: 'Up to five pictures can be uploaded.'
          });
        }
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
          let temp = file
          temp.url = res['url']
          temp.status = 'finished'
          //temp.name = res['url']
          this.uploadList.push(temp)
        })
        return false
      }
    },
    created: function () {
    }
  }
</script>
<style scoped>
  .input{
    width: 50%;
  }
  .wenzi{
    font-size: 2em;
  }
  .demo-upload-list{
    display: inline-block;
    width: 60px;
    height: 60px;
    text-align: center;
    line-height: 60px;
    border: 1px solid transparent;
    border-radius: 4px;
    overflow: hidden;
    background: #fff;
    position: relative;
    box-shadow: 0 1px 1px rgba(0,0,0,.2);
    margin-right: 4px;
  }
  .demo-upload-list img{
    width: 100%;
    height: 100%;
  }
  .demo-upload-list-cover{
    display: none;
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background: rgba(0,0,0,.6);
  }
  .demo-upload-list:hover .demo-upload-list-cover{
    display: block;
  }
  .demo-upload-list-cover i{
    color: #fff;
    font-size: 20px;
    cursor: pointer;
    margin: 0 2px;
  }
</style>