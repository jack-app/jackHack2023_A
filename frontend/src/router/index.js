import Vue from 'vue';
import Router from 'vue-router'
import AboutPage from '../views/About.vue'
import InputWordPage from '../views/InputWordPage.vue'
import ResultPage from '../views/ResultPage.vue'
import StandByPage from '../views/StandByPage.vue'
import SubmitTextPage from '../views/SubmitTextPage.vue'
import TitlePage from '../views/TitlePage.vue'
import VotePage from '../views/VotePage.vue'


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
        {
            path:'/inputword',      // URL 
            name: "inputword",
            component: InputWordPage,
            meta:{
                title:'PICK UP WORD',
                hoge:'ほげほげ',
              },
             // 上記URLのときに表示するコンポーネント
        },
        {
            path:'/result',      // URL 
            name: "result",
            component: ResultPage,
             // 上記URLのときに表示するコンポーネント
        },
        {
            path:'/standby',      // URL 
            name: "standby", //
            component: StandByPage,
             // 上記URLのときに表示するコンポーネント
        },
        {
            path:'/submittext',      // URL 
            name: "submittext", //
            component: SubmitTextPage,
             // 上記URLのときに表示するコンポーネント
        },
        {
            path:'/title',      // URL 
            name: "title", //
            component: TitlePage,
             // 上記URLのときに表示するコンポーネント
        },
        {
            path:'/vote',      // URL 
            name: "vote", //
            component: VotePage,
             // 上記URLのときに表示するコンポーネント
        },
    ]
})