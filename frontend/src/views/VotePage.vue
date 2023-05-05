<template>
  <div class="wrapper">
    <div class="oneone">
      <img class="hidari" src="../assets/hidari.jpg" alt="" />
    </div>
    <div class="onetwo">
      Player 1
      <div class="text-center">
        <v-dialog v-model="dialog" width="auto">
          <template v-slot:activator="{ props }">
            <v-btn color="primary" v-bind="props"> Open Text </v-btn>
          </template>

          <v-card>
            <v-card-text>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
              eiusmod tempor incididunt ut labore et dolore magna aliqua.
            </v-card-text>
            <v-card-actions>
              <v-btn color="primary" block @click="dialog = false"
                >Close Text</v-btn
              >
            </v-card-actions>
          </v-card>
        </v-dialog>
      </div>
    </div>
    <div class="onethree">
      <img class="migi" src="../assets/migi.jpg" alt="" />
    </div>
    <div class="onefour">
      <v-btn size="x-large" color="primary" v-on:click="submitVote1">
        ---- vote----
      </v-btn>
    </div>

    <div class="oneone">
      <img class="hidari" src="../assets/hidari.jpg" alt="" />
    </div>
    <div class="onetwo">
      Player 2
      <div class="text-center">
        <v-dialog v-model="dialog" width="auto">
          <template v-slot:activator="{ props }">
            <v-btn color="primary" v-bind="props"> Open Text </v-btn>
          </template>

          <v-card>
            <v-card-text>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
              eiusmod tempor incididunt ut labore et dolore magna aliqua.
            </v-card-text>
            <v-card-actions>
              <v-btn color="primary" block @click="dialog = false"
                >Close Text</v-btn
              >
            </v-card-actions>
          </v-card>
        </v-dialog>
      </div>
    </div>
    <div class="onethree">
      <img class="migi" src="../assets/migi.jpg" alt="" />
    </div>
    <div class="onefour">
      <v-btn size="x-large" color="primary" v-on:click="submitVote2">
        ---- vote----
      </v-btn>
    </div>

    <div class="oneone">
      <img class="hidari" src="../assets/hidari.jpg" alt="" />
    </div>
    <div class="onetwo">
      Player 3
      <div class="text-center">
        <v-dialog v-model="dialog" width="auto">
          <template v-slot:activator="{ props }">
            <v-btn color="primary" v-bind="props"> Open Text </v-btn>
          </template>

          <v-card>
            <v-card-text>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
              eiusmod tempor incididunt ut labore et dolore magna aliqua.
            </v-card-text>
            <v-card-actions>
              <v-btn color="primary" block @click="dialog = false"
                >Close Text</v-btn
              >
            </v-card-actions>
          </v-card>
        </v-dialog>
      </div>
    </div>
    <div class="onethree">
      <img class="migi" src="../assets/migi.jpg" alt="" />
    </div>
    <div class="onefour">
      <v-btn size="x-large" color="primary" v-on:click="submitVote3">
        ---- vote----
      </v-btn>
    </div>

    <div class="oneone">
      <img class="hidari" src="../assets/hidari.jpg" alt="" />
    </div>
    <div class="onetwo">
      Player 4
      <div class="text-center">
        <v-dialog v-model="dialog" width="auto">
          <template v-slot:activator="{ props }">
            <v-btn color="primary" v-bind="props"> Open Text </v-btn>
          </template>

          <v-card>
            <v-card-text>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
              eiusmod tempor incididunt ut labore et dolore magna aliqua.
            </v-card-text>
            <v-card-actions>
              <v-btn color="primary" block @click="dialog = false"
                >Close Text</v-btn
              >
            </v-card-actions>
          </v-card>
        </v-dialog>
      </div>
    </div>
    <div class="onethree">
      <img class="migi" src="../assets/migi.jpg" alt="" />
    </div>
    <div class="onefour">
      <v-btn size="x-large" color="primary" v-on:click="submitVote4">
        ---- vote----
      </v-btn>
    </div>

    <div class="oneone">
      <img class="hidari" src="../assets/hidari.jpg" alt="" />
    </div>
    <div class="onetwo">
      Player 5
      <div class="text-center">
        <v-dialog v-model="dialog" width="auto">
          <template v-slot:activator="{ props }">
            <v-btn color="primary" v-bind="props"> Open Text </v-btn>
          </template>

          <v-card>
            <v-card-text>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
              eiusmod tempor incididunt ut labore et dolore magna aliqua.
            </v-card-text>
            <v-card-actions>
              <v-btn color="primary" block @click="dialog = false"
                >Close Text</v-btn
              >
            </v-card-actions>
          </v-card>
        </v-dialog>
      </div>
    </div>
    <div class="onethree">
      <img class="migi" src="../assets/migi.jpg" alt="" />
    </div>
    <div class="onefour">
      <v-btn size="x-large" color="primary" v-on:click="submitVote5">
        ---- vote----
      </v-btn>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "VotePage",

  components: {},
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
      vote: "",
      /*
        投票先を表しています。
       */
    };
  },
  created() {
    const room_id = localStorage.getItem("room_id");
    axios
      .post("http://localhost:3000/get_text_list", { room_id: room_id })
      .then((res) => {
        const text_list = res.data;
        text_list.map((test) => {
          // 第一引数に配列の値が入ってくる
          let text_tmp = {};
          text_tmp.text = test["text"];
          this.items.push(text_tmp);
        });
      });
    console.log(this.items);

    // /*
    // 以下数行テストコード
    // */
    // setTimeout(function () {
    //     let vote_subject = "リンゴ";
    //     console.log(vote_subject)
    //     const room_id = localStorage.getItem('room_id');
    //     axios.post("http://localhost:3000/submit_vote",
    //     {
    //         room_id: room_id,
    //         vote_subject: vote_subject
    //     })
    //     .then(()=>{
    //         this.$router.push({ path: '/standby', query: { tag: "vote" }});
    //     })
    // }, 1000);
    // /*
    // ここまで
    // */
  },
  methods: {
    submitVote1: function () {
      this.vote = "player 1";
      //投票ボタンを押したときの処理です。ここでバックに投票先を送ります。
      const vote_subject = this.vote;
      const room_id = localStorage.getItem("room_id");
      axios
        .post("http://localhost:3000/submit_vote", {
          room_id: room_id,
          vote_subject: vote_subject,
        })
        .then(() => {
          this.$router.push({ path: "/standby", query: { tag: "vote" } });
        });
    },
    submitVote2: function () {
      this.vote = "player 2";
      //投票ボタンを押したときの処理です。ここでバックに投票先を送ります。
      const vote_subject = this.vote;
      const room_id = localStorage.getItem("room_id");
      axios
        .post("http://localhost:3000/submit_vote", {
          room_id: room_id,
          vote_subject: vote_subject,
        })
        .then(() => {
          this.$router.push({ path: "/standby", query: { tag: "vote" } });
        });
    },
    submitVote3: function () {
      this.vote = "player 3";
      //投票ボタンを押したときの処理です。ここでバックに投票先を送ります。
      const vote_subject = this.vote;
      const room_id = localStorage.getItem("room_id");
      axios
        .post("http://localhost:3000/submit_vote", {
          room_id: room_id,
          vote_subject: vote_subject,
        })
        .then(() => {
          this.$router.push({ path: "/standby", query: { tag: "vote" } });
        });
    },
    submitVote4: function () {
      this.vote = "player 4";
      //投票ボタンを押したときの処理です。ここでバックに投票先を送ります。
      const vote_subject = this.vote;
      const room_id = localStorage.getItem("room_id");
      axios
        .post("http://localhost:3000/submit_vote", {
          room_id: room_id,
          vote_subject: vote_subject,
        })
        .then(() => {
          this.$router.push({ path: "/standby", query: { tag: "vote" } });
        });
    },
    submitVote5: function () {
      this.vote = "player 5";
      //投票ボタンを押したときの処理です。ここでバックに投票先を送ります。
      const vote_subject = this.vote;
      const room_id = localStorage.getItem("room_id");
      axios
        .post("http://localhost:3000/submit_vote", {
          room_id: room_id,
          vote_subject: vote_subject,
        })
        .then(() => {
          this.$router.push({ path: "/standby", query: { tag: "vote" } });
        });
    },
  },
};
</script>

<style>
.wrapper {
  table-layout: fixed;
  margin: 30px;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-rows: 200px;
}

.onetwo {
  table-layout: fixed;
  font-size: 30px;
  text-align: center;
  padding: 30px;
}

.onefour {
  margin-top: 50px;
  padding: 30px;
  text-align: center;
}

.hidari {
  width: 300px;
  height: 170px;
}

.migi {
  width: 300px;
  height: 170px;
}
</style>
