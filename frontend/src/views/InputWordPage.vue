<template>
    <div class = "container-input">
        <div class="box-input">
            <p class = "title-theme-input">
                今回のお題
            </p>
            <p class="text-input">今回のお題は {{ theme }} です！</p>
        </div>
        <div class = "textbox-input">
            <div class = "label-left-input"></div>
            <div class = "label-right-input"></div>
            <div class = "form-input">
            <input class = "input-form-input" v-model="message" placeholder="お題に沿った単語を入力してね" />
            <v-btn v-on:click="submitTheme" class = "submit-button-input">
                決定
            </v-btn>
            </div>
        </div>
    </div>
</template>
  
<script>
import io from "socket.io-client";
export default {
    
    name: 'InputWordPage',
    components: {
        
    },
    data() {
        return{
            socket: io("localhost:3000/api/"),
            theme: "",
            message: ""
        }
    },
    created(){
        this.theme = "花"
    },
    methods: {
      submitTheme: function () {
        const word = this.message;
        const room_id = localStorage.getItem('room_id');
        this.socket.emit("input_word",word, room_id);
        this.$router.push({ path: '/standby', query: { tag: "inputword" }});
      },
        
    },
}
</script>
<style>

.container-input {
    margin-top: 30px;
    margin-left: 20px;
    margin-right: 20px;
}

.box-input {
    height: 250px;
    border-radius: 10px; /*角丸の指定*/
    border: #c08a9b 3px solid; /*境界線の指定*/
    padding:10px;
}
.text-input {
    font-size: 40px;
    text-align: center;
}

.title-theme-input{
    font-size: 30px;
    color:#c08a9b;
}

.textbox-input{
    margin-top: 60px;
    height: 150px;
    background: #C08A9B;
}
.form-input{
    position: relative;
    left: 35%
}
.input-form-input{
    width: 300px;
    padding: 30px;
    text-align: center;
}
.label-left-input{
    position: relative;
    right: 40px;
    width: 12%;
    height: 10%;
    background: #FCDCCA;
    transform: rotate(-34.67deg);
}
.label-right-input{
    position: relative;
    left: 90%;
    top: 100px;
    width: 12%;
    height: 10%;
    background: #FCDCCA;
    transform: rotate(-34.67deg);
}
.submit-button-input{
    margin:5px;
    margin-top: 40px;
}
</style>
