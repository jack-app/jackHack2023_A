import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';
import { colors } from 'vuetify/lib';
Vue.use(Vuetify);

export default new Vuetify({
    theme: {
        themes: {
          light: {
            primary: "#c08a9b",
            secondary: colors.green,
            accent: "#fcdcca",
            error: colors.red,
            warning: colors.yellow,
            info: colors.grey,
            success: "#795548",
            mycolor: "#e0e0e0",
          },
        },
      },
});
