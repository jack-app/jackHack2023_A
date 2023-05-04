<template>
  <v-app id = "app">
    <HeaderItem/>
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

  data: () => ({
    //
  }),
};
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