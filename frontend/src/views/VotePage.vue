<template>
    <div>
        おはよう
        こんにちは
    </div>
</template>
  
<script>
import axios from "axios";
export default {
name: 'VotePage',

components: {
    
},
data() {
    return {
        items: [], 
        /*
        このitems のtextの中に本文が書かれています。
        <v-list>
            <v-list-item
            v-for="item in items"
            :key="item.text"
            :title="item.text"
            >
                {{ item.text }}
            </v-list-item>
        </v-list>
        このように書くことで、順に表示することが出来ます。
        これを使ってね。
        */
       vote: 0,
       /*
        投票先を表しています。
       */
    }
},
created(){
    const room_id = localStorage.getItem('room_id');
    axios.post("http://localhost:3000/get_text_list",{room_id: room_id})
    .then((res) => {
        const text_list = res.data
        text_list.map((test)=>{
            // 第一引数に配列の値が入ってくる
            let text_tmp = {}
            text_tmp.text = test["text"]
            this.items.push(text_tmp)
        });
    })
    console.log(this.items)

    /*
    以下数行テストコード
    */
    setTimeout(function () {
        let vote_subject = "リンゴ";
        console.log(vote_subject)
        const room_id = localStorage.getItem('room_id');
        axios.post("http://localhost:3000/submit_vote",
        {
            room_id: room_id,
            vote_subject: vote_subject
        })
        .then(()=>{
            this.$router.push({ path: '/standby', query: { tag: "vote" }});
        })
    }, 1000);
    /*
    ここまで
    */
},
methods: {
    submitVote: function () {
        //投票ボタンを押したときの処理です。ここでバックに投票先を送ります。
        const vote_subject = this.vote;
        const room_id = localStorage.getItem('room_id');
        axios.post("http://localhost:3000/submit_vote",
        {
            room_id: room_id,
            vote_subject: vote_subject
        })
        .then(()=>{
            this.$router.push({ path: '/standby', query: { tag: "vote" }});
        })
      },
}


};
</script>
  