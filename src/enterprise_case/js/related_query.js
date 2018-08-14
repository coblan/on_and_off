Vue.component('com-field-related-query',{
    props:['row','head'],
    template:`<div>
        <input type="text" v-model="row[head.name]">
        <button @click="info_query()">关联</button>
    </div>`,
    methods:{
        info_query:function(){
            var self=this
                this.head.table_ctx.search_args._q=this.row.enterpriseinvoledname
                pop_table_layer(this.row,this.head.table_ctx,function(selected_row){
                    for(var k in selected_row){
                        Vue.set(self.row,k,selected_row[k])
                    }
                    //ex.assign(self.row,selected_row)
                })


            //var post_data=[{fun:'info_enterprise',name:this.row[this.head.name]}]
            //ex.post('/d/ajax/enterprise_case',JSON.stringify(post_data),function(resp){

            //})
        }
    }
})