Vue.component('com-field-taskid',{
    props:['head','row'],
    template:`<div>
    <a  class="clickable" :href="mylink" target="_blank">
        <span v-text="row[head.name]"></span><span>(点击完善企业信息)</span>
    </a>
    </div>`,
    computed:{
        mylink:function(){
            var taskid = this.row[this.head.name]
            return ex.template(this.head.sango_link,{taskid:taskid})
        }
    }
})