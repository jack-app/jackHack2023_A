<template>
  <div>
    <div class="firsttext">
      <img class="hidari-resu" src="../assets/hidari.jpg" alt="" />
      <p class="result-text">
        sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss
      </p>
      <img class="migi-resu" src="../assets/migi.jpg" alt="" />
    </div>
    <div class="under">
      <div class="allresult">
        <div style="display: flex">
          <div style="font-size: 40px">１位</div>
          <div style="font-size: 40px; margin-left: 30px">一位の名前</div>
        </div>
        <div class="No2345-result">
          <div class="resultNo-result">２位</div>
          <div class="name-result">２位の名前</div>
          <div class="resultNo-result">３位</div>
          <div class="name-result">３位の名前</div>
        </div>
        <div class="No2345-result">
          <div class="resultNo-result">４位</div>
          <div class="name-result">４位の名前</div>
          <div class="resultNo-result">５位</div>
          <div class="name-result">５位の名前</div>
        </div>
      </div>

      <div class="myresult">
        <P>--MY RESURT--</P>
        <p>
          AI採点 ○点<br />
          投票数 ○票
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "ResultPage",

  data() {
    return {
      winner: "",
      //今回の勝者の名前がここに入ります
    };
  },
  components: {},
  created() {
    axios.get("http://localhost:3000/get_winner").then((res) => {
      console.log(res.data);
      let name_list_json = localStorage.getItem("name_list");
      let name_list = JSON.parse(name_list_json);
      this.winner = name_list[res.data];
    });
  },
};
</script>

<style>
.firsttext {
  display: flex;
  margin: 50px;
  width: 1150px;
  height: 200px;
}

.hidari-resu {
  width: 250px;
  height: 150px;
  z-index: 1;
  position: fixed;
}

.result-text {
  padding: 50px;
  z-index: 2;
  word-break: break-all;
}

.migi-resu {
  width: 250px;
  height: 150px;
  margin-top: 30px;
  margin-left: 900px;
  z-index: 1;
  position: fixed;
}

.under {
  display: flex;
}

.allresult {
  border: 1px solid #000;
  color: white;
  background-color: #c08a9b;

  margin-left: 70px;
  width: 700px;
  height: 150px;
}

.myresult {
  border: 1px solid #c08a9b;
  background-color: #c08a9b;
  margin-left: 30px;
  width: 300px;
  height: 150px;
  color: #fff;
  font-size: 20px;
  text-align: center;
  vertical-align: middle;
  line-height: 30px;
}
/* 一位以外の〇位の装飾 */
.resultNo-result {
  font-size: 30px;
}
/* ２，３,4,5位の並び方 */
.No2345-result {
  display: flex;
  gap: 40px;
}
.No1-result {
  color: black;
  font-size: 40px;
}
/* 名前の装飾 */
.name-result {
  font-size: 30px;
  margin-left: px;
}
</style>
