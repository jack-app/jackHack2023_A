<template>
  <v-app id = "app">
    <HeaderItem :title = title></HeaderItem>
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import HeaderItem from './components/Header';

export default {
  name: 'App',

  components: {
    HeaderItem,
  },
  data(){
    return{
      title: ""
    }
  },
  methods: {
    createTitleDesc : function(routeInstance){
        //titleを設定する処理
        if(routeInstance.meta.title){
            var setTitle = routeInstance.meta.title;
            document.title = setTitle;
            this.title = document.title;
        } else {
            document.title = 'ルートでtitleがセットされていない場合に表示するテキスト'
        }
      }
  },
  mounted : function(){
      var routeInstance = this.$route;
      this.createTitleDesc(routeInstance);
  },
  watch: { 
      '$route' (routeInstance, from) {
        console.log(from)
        this.createTitleDesc(routeInstance);
      }
  },
  
}
</script>
<style>

template{margin:0px;}
@import url('https://fonts.googleapis.com/css2?family=Yomogi&display=swap');
#app {
  font-family: 'Yomogi', cursive;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

</style>