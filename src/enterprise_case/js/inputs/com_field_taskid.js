Vue.component('com-field-taskid',{
    props:['head','row'],
    template:`<div>
    <a v-text="row[head.name]" class="clickable" :href="mylink" target="_blank"></a>
    </div>`,
    computed:{
        mylink:function(){
            var taskid = this.row[this.head.name]
            return ex.template(this.head.sango_link,{taskid:taskid})
        }
    }
})