<template>
    <v-container>
        <v-row>
            <v-col cols="3">
                <div class = "container-submittext">
                    <div class="box-submittext">
                        <p class = "wordlist-title-submittext">WORD YOU MUST USE</p>
                        <v-list>
                            <v-list-item
                            v-for="item in items"
                            :key="item.title"
                            :title="item.title"
                            >
                                {{ item.title }}
                            </v-list-item>
                        </v-list>
                    </div>
                </div>
            </v-col>
            <v-col>
                <div class="container-text-submittext">
                    <div class="box-text-submittext">
                        <p class = "wordlist-title-submittext">text</p>
                        <div class="input-field-submittext">
                            <v-textarea 
                                clearable 
                                v-model="message" 
                                variant="filled"
                                auto-grow
                                placeholder="あなたの思う最高の告白文を、単語を使用して入力してね" 
                            ></v-textarea>
                            <v-btn v-on:click="submitText" class = "submit-button-input">
                                送信
                            </v-btn>
                        </div>
                    </div>
                </div>
            </v-col>
        </v-row>    
    </v-container>
</template>
  
<script>
import axios from "axios";
import io from "socket.io-client";
export default {
    name: 'SubmitTextPage',
    components: {
        
    },
    data() {
        return{
            socket: io("localhost:3000/api/"),
            items: [],
        }
    },
    created(){
        const room_id = localStorage.getItem('room_id');
        axios.post("http://localhost:3000/api/get_word_list",{room_id: room_id})
        .then((res) => {
            this.items = res.data.items.map((test)=>{
                // 第一引数に配列の値が入ってくる
                return test;
            });
            this.items = [
            {
                title: 'Item #1',
                value: 1,
            },
            {
                title: 'Item #2',
                value: 2,
            }
        ]
        })
        
    },
    methods: {
        submitText: function () {
            // this.messageをバックエンドに送信する
            const text = this.message;
            const room_id = localStorage.getItem('room_id');
            this.socket.emit("submit_text",text, room_id);
            this.$router.push({ path: '/standby', query: { tag: "submittext" }});
        },
    }
};
</script>
<style>
.container-submittext {
    margin-top: 50px;
    margin-left: 20px;
    margin-right: 20px;
}

.box-submittext {
    height: 400px;
    border-radius: 1px; /*角丸の指定*/
    border: #c08a9b 3px solid; /*境界線の指定*/
    background-color: #c08a9b;
    padding:10px;
    width: 100%;
}
.wordlist-title-submittext{
    color: #ffffff;
    font-size: 18px;
    margin: 10px;
}

.container-text-submittext {
    margin-top: 30px;
    margin-left: 20px;
    margin-right: 20px;
}
.box-text-submittext{
    height: 450px;
    border-radius: 1px; /*角丸の指定*/
    border: #c08a9b 3px solid; /*境界線の指定*/
    background-color: #c08a9b;
    padding:10px;
    width: 100%;
}
.input-field-submittext{
    height: 300px;
    background-color: #ffffff;
}
</style>