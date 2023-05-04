<template>
    <div>
        <p class = "result">
            結果発表～～
        </p>
        <p class = "result-2">
            成功です！！！
            {{ winner }}
        </p>
    </div>
</template>
  
<script>
import axios from "axios";
export default {
    name: 'ResultPage',
    data() {
        return{
            winner : ""
            //今回の勝者の名前がここに入ります
        }
    },
    components: {
        
    },
    created(){
        axios.get("http://localhost:3000/get_winner")
        .then((res) => {
            console.log(res.data)
            let name_list_json = localStorage.getItem('name_list');
            let name_list = JSON.parse(name_list_json);
            this.winner = name_list[res.data]
        })
    },

    
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