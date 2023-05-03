<template>
  <v-app>
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
