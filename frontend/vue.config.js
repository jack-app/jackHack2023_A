const { defineConfig } = require('@vue/cli-service')
const GoogleFontsPlugin = require("google-fonts-webpack-plugin");
module.exports = defineConfig({
  transpileDependencies: [
    'vuetify'
  ],
  entry: "index.js",
  /* ... */
  configureWebpack: {
    plugins: [
      new GoogleFontsPlugin({
        fonts: [
          { family: "Yomogi" },
          /*ここにフォントを追加していく．もちろん上のRobotoとSourse sans proは消してよい*/
        ],
        /* ...options */
      }),
    ],
  },
})
module.exports = {};