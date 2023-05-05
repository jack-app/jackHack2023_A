<template>
  <div>
    <v-card
      style="border-width: 5px; border-color: #c08a9b; margin: 20px 0px 0px 0px"
      class="mx-auto"
      width="80%"
      height="auto"
      outlined
    >
      <v-card-item>
        <div class="text-h6 mb-1">
          <p class="ruletellerT-title">--ルール説明--</p>
        </div>
        <div class="div-equal-box-title">
          <p class="ruletellerM-title">
            みんなが出した単語を使ってロマンチックな文章を作ろう！
          </p>
          <p class="ruletellerM-title">
            1. お題に合わせて好きな単語を打ち込んでください！
          </p>
          <p class="ruletellerM-title">
            2.
            ５人それぞれが選んだ単語を使ってロマンチックな文章を作りましょう！
          </p>
          <p class="ruletellerM-title">
            3. 一番ロマンチックな文章を書いた人に投票しよう！
          </p>
        </div>
      </v-card-item>
    </v-card>
    <div class="alignment">
      <input
        v-model="message"
        outlined
        style="#C08A9B;width: 500px;height:60px;margin:40px 0px 0px 300px;
        border: 3px solid #C08A9B;  /* 枠線 */ border-radius: 10em;   /* 角丸 */"
        placeholder="名前を入力してね"
      />
      <v-container class="text-center">
        <v-row justify="center">
          <v-col cols="12" sm="6" md="4">
            <v-btn
              height="100px"
              block
              color="#C08A9B"
              size="large"
              v-on:click="start"
            >
              <div class="buttonGS-title">GAME START</div>
            </v-btn>
          </v-col>
        </v-row>
      </v-container>
    </div>
  </div>
</template>

<script>
import io from "socket.io-client";
export default {
  name: "TitlePage",

  components: {},

  data() {
    return {
      socket: io("localhost:3000/"),
    };
  },
  methods: {
    start: function () {
      // this.messageをバックエンドに送信する
      const player_name = this.message;
      this.socket.emit("start", player_name);
      this.$router.push({ path: "/standby", query: { tag: "title" } });
    },
  },
};
</script>

<style>
.ruletellerM-title {
  color: #c08a9b;
  font-size: 30px;
}
.text-center {
  position: relative;
  left: 0px;
  top: 3%;
}
.buttonGS-title {
  font-size: 70px;

  color: white;
}
.ruletellerT-title {
  color: #c08a9b;
  font-size: 50px;
  margin: 15px;
}
.div-equal-box-title {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
}
.alignment {
  display: inline-flex;
  flex-direction: row;
  /* justify-content: space-around;   */
}
</style>
