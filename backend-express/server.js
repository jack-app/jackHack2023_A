import path from "path";
import { fileURLToPath } from "url";
import express from "express";
import importHttp  from "http";
import { Server } from "socket.io";
import serverStatic from "serve-static";
import cors from "cors";
import bodyParser from "body-parser";
import history from "connect-history-api-fallback";

const app = express();
const http = importHttp.Server(app);

const io = new Server(http, {
  cors: {
    origin: true,
    methods: ["GET", "POST"],
  },
});
const PORT = process.env.PORT || 3000;

let numClients = {};

const serveStatic = serverStatic

//post時にjsonファイルを扱えるようにする
app.use(express.json());
app.use(
  cors({
    origin: true,
    credentials: true,
    optionsSuccessStatus: 200,
  })
);
//post時にbodyを参照できるようにする
app.use(bodyParser.urlencoded({ extended: true }));

if (process.env.NODE_ENV !== "production") {
  app.use(
    cors({
      origin: true,
      credentials: true,
      optionsSuccessStatus: 200,
    }),
  );
}

const __filename = fileURLToPath(import.meta.url);
let __dirname = path.dirname(__filename);
__dirname = path.resolve(__dirname, "..")

app.use(serveStatic(__dirname + "/dist"));

app.use(
  history({
    disableDotRule: true,
    verbose: true,
  })
);

app.use(serveStatic(__dirname + "/dist"));
let stand_by_player = [];

let word_list = [];
let word_list_log = [];
let text_list = [];
let text_list_log = [];
let vote_subject_list = []
let winner = []

//WebSocket周りの処理
io.sockets.on("connection", function (socket) {
  //マッチング機能
  socket.on("start", function (player_name) {
    stand_by_player.push(player_name);
    function join_room(player_name_list) {
        console.log("満員です")
        const room_id = Math.random().toString(32).substring(2);
        io.emit("room_full", room_id, player_name_list);
        console.log("room_full",room_id);
    }
    if (stand_by_player.length >= 5) {
        let player_name_list = [];
        //5人超えたらマッチングするようにする。
        stand_by_player.map((player_name) => {
            player_name_list.push(player_name)
        })
        stand_by_player.splice(0, 5);
        setTimeout(function () {
            join_room(player_name_list);
        }, 1000);
    }
    
  });
  
  //ログイン時処理
  socket.on("login", function (room_id) {
    if (numClients[room_id] == undefined) {
      numClients[room_id] = 1;
    } else {
      numClients[room_id]++;
    }
    //もしルームの人数が5人以上ならルームに入れない
    if (numClients[room_id] > 5) {
      console.log("This room is full");
    } else {
      socket.join(room_id);
      console.log("Roomに入室が完了しました");
    }
  });
  socket.on("room_join", function (room_id) {
    socket.join(room_id);
  });
});

app.post("/input_word", (req, res) => {
    console.log(req.body.word)
    var data_tmp = {};
    data_tmp.word = req.body.word;
    data_tmp.room_id = req.body.room_id;
    word_list.push(data_tmp);
    console.log(word_list)
    if (word_list.length >= 5){
        console.log("全員入力し終わった")
        for(let i = 0; i < word_list.length; i++){
            word_list_log.push(word_list[i]);
        } 
        word_list.splice(0, 5);
        setTimeout(function () {
            io.emit("done_submit_word");
        }, 1000);
    }
    res.send()
});

app.post("/get_word_list", (req, res) => {
    const result = word_list_log.filter((u) => u.room_id === req.body.room_id);
    console.log(result)
    res.send(result)
});


app.post("/submit_text", (req, res) => {
    console.log(req.body.text)
    var data_tmp = {};
    data_tmp.text = req.body.text;
    data_tmp.room_id = req.body.room_id;
    text_list.push(data_tmp);
    console.log(text_list)
    if (text_list.length >= 5){
        console.log("全員入力し終わった")
        for(let i = 0; i < text_list.length; i++){
            text_list_log.push(text_list[i]);
        } 
        text_list.splice(0, 5);
        setTimeout(function () {
            io.emit("done_submit_text");
        }, 1000);
    }
    res.send()
});

app.post("/get_text_list", (req, res) => {
    const result = text_list_log.filter((u) => u.room_id === req.body.room_id);
    console.log(result)
    res.send(result)
});



app.post("/submit_vote", (req, res) => {
    console.log(req.body)
    vote_subject_list.push(req.body.vote_subject)
    console.log(vote_subject_list)
    if (vote_subject_list.length >= 5){
        console.log("全員投票し終わった")
        const c = (x, i, v) => (x[i] ? x[i].add(v) : x[i] = new Set(v), i);
        const result = vote_subject_list.reduce(function (x, v) { return (this.set(v, c(x, (this.get(v) + 1 || 1), v)), x); }.bind(new Map), []).pop();
        winner = [...result].join('');
        setTimeout(function () {
            io.emit("done_vote");
        }, 1000);

        vote_subject_list.splice(0, 5);
    }
    res.send()
});

app.get("get_winner", (req, res) => {
    res.send(winner)
})

http.listen(PORT, function () {
  console.log("server listening. Port:" + PORT);
});