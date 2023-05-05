<template>
   <div class="container-standby">
        <div class="maintext-standby">
            NOW LOADING ...
        </div>
        
        <div class="subtext-standby">
            参加者{{ message }}を集めています
        </div>
    </div>
</template>

<script>
import io from "socket.io-client";

export default {
  name: 'StandByPage',

  components: {
      
  },

  data () {
    return{
      socket: io("localhost:3000/"),
      message: ""
    }
  },
  created(){
    //すけのタスク これを編集して、適切な文章にしてください。
    if (this.$route.query.tag == "inpuword"){
      this.message = ""
    }
    if (this.$route.query.tag == "submittext"){
      this.message = ""
    }
    console.log(this.$route.query.tag)
  },
  mounted(){
    const in_socket_this = this;
    this.socket.on("room_full", function (room_id, player_name_list) {
      console.log("room_full")
      localStorage.setItem('room_id', room_id);
      let player_name_list_json = JSON.stringify(player_name_list, undefined, 1);
      localStorage.setItem('name_list', player_name_list_json);
      in_socket_this.socket.emit("login", room_id);
      console.log("人数がいっぱいになったので、ゲームを開始します");
      in_socket_this.$router.push({ path: '/inputword' })
    });

    this.socket.on("done_submit_word", function () {
      console.log("全員の単語入力が完了しました");
      in_socket_this.$router.push({ path: '/submittext' })
    });

    this.socket.on("done_submit_text", function () {
      console.log("全員の文章入力が完了しました");
      in_socket_this.$router.push({ path: '/vote' })
    });

    this.socket.on("done_vote", function () {
      console.log("全員の投票が完了しました");
      in_socket_this.$router.push({ path: '/result' })
    });
  }
};
</script>
<style>
  .maintext-standby{
    font-size: 100px;
    color:#C08A9B;
    text-align: center;
    /* position: absolute;
    top: 50%;
    left: 50%; */
    /* margin: -25px 0 0 -25px; */
  }
  .container-standby{
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  .subtext-standby{
    color:#C08A9B;
    font-size:xx-large;
  }
</style>