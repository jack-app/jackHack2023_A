<template>
  <div class="container-input">
    <div class="box-input">
      <p class="title-theme-input">今回のお題</p>
      <p class="text-input">今回のお題は {{ theme }} です！</p>
    </div>
    <div class="textbox-input">
      <div class="label-left-input"></div>
      <div class="label-right-input"></div>
      <div class="form-input">
        <input
          class="input-form-input"
          v-model="message"
          placeholder="お題に沿った単語を入力してね"
        />
        <v-btn v-on:click="submitTheme" class="submit-button-input">
          決定
        </v-btn>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import io from "socket.io-client";
export default {
  name: "InputWordPage",
  components: {},
  data() {
    return {
      socket: io("localhost:3000/"),
      theme: "",
      message: "",
    };
  },
  created() {
    const room_id = localStorage.getItem("room_id");
    this.socket.emit("room_join", room_id);
    const candidates = [
      "花",
      "夏",
      "海",
      "山",
      "星",
      "恋",
      "星",
      "風",
      "花",
      "瞳",
      "夢",
      "愛",
      "時",
      "音楽",
      "海",
      "切なさ",
      "天使",
      "希望",
      "闇",
      "笑顔",
      "月",
      "命",
      "温もり",
      "青春",
      "街",
      "涙",
      "旅",
      "祈り",
      "心",
      "幸せ",
      "静寂",
      "癒し",
      "輝き",
      "出会い",
      "花束",
      "恋愛",
      "夕陽",
      "星空",
      "ダンス",
      "絆",
      "幸福",
      "甘い",
      "誓い",
      "彼氏",
      "彼女",
      "君に逢いたい",
      "愛してる",
      "瞳",
      "ハグ",
      "キス",
      "お互い様",
      "運命",
      "プロポーズ",
      "結婚式",
    ];
    const numArr = room_id.match(/\d+/g).map(Number);
    const randomIndex = parseInt(numArr) % candidates.length;
    this.theme = candidates[randomIndex];
  },
  methods: {
    submitTheme: function () {
      const word = this.message;
      const room_id = localStorage.getItem("room_id");
      axios
        .post("http://localhost:3000/input_word", {
          room_id: room_id,
          word: word,
        })
        .then(() => {
          this.$router.push({ path: "/standby", query: { tag: "inputword" } });
        });
    },
  },
};
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
  padding: 10px;
}
.text-input {
  font-size: 40px;
  text-align: center;
}

.title-theme-input {
  font-size: 30px;
  color: #c08a9b;
}

.textbox-input {
  margin-top: 60px;
  height: 150px;
  background: #c08a9b;
}
.form-input {
  position: relative;
  left: 35%;
}
.input-form-input {
  width: 300px;
  padding: 30px;
  text-align: center;
}
.label-left-input {
  position: relative;
  right: 40px;
  width: 12%;
  height: 10%;
  background: #fcdcca;
  transform: rotate(-34.67deg);
}
.label-right-input {
  position: relative;
  left: 90%;
  top: 100px;
  width: 12%;
  height: 10%;
  background: #fcdcca;
  transform: rotate(-34.67deg);
}
.submit-button-input {
  margin: 5px;
  margin-top: 40px;
}
</style>
