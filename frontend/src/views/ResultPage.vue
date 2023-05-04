<template>
    <div>
        <p class = "result">
            結果発表～～
        </p>
        <p class = "result-2">
            {{ result }}の勝ち！
        </p>
    </div>
</template>
  
<script>
import axios from "axios";
export default {
    name: 'ResultPage',
    components: {
        
    },

    data(){
        return{
            result: "",
        }
    },
    created(){
        const room_id = localStorage.getItem('room_id');
        axios.post("http://localhost:3000/api/get_result",{room_id: room_id})
        .then((res) => {
            this.result = res.data.result;
        })
    },
    methods:{
        
    }
};
</script>

<style>
.result{
    margin-top: 30px;
    font-size: 100px;
}
.result-2{
    font-size: 30px;
    color: blue;
    
}
</style>