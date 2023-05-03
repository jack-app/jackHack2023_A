import Vue from 'vue';
import Router from 'vue-router'
import AboutPage from '../views/About.vue'

Vue.use(Router) // プラグイン（どこでも使える機能）を適用するために記載

export default new Router({
    mode: 'history',
    routes:[
        {
            path:'/',      // URL 
            name: "home",
            component: AboutPage,
             // 上記URLのときに表示するコンポーネント
        },
    ]
})