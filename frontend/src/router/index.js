import Vue from 'vue';
import Router from 'vue-router'
import InputWordPage from '../views/InputWordPage.vue'
import ResultPage from '../views/ResultPage.vue'
import StandByPage from '../views/StandByPage.vue'
import SubmitTextPage from '../views/SubmitTextPage.vue'
import TitlePage from '../views/TitlePage.vue'
import VotePage from '../views/VotePage.vue'


Vue.use(Router) // プラグイン（どこでも使える機能）を適用するために記載

const router = new Router({
    mode: 'history',
    routes:[
        {
            path:'/',      // URL 
            name: "title", //
            component: TitlePage,
            meta:{
                title:'タイトル',
            },
             // 上記URLのときに表示するコンポーネント
        },
        {
            path:'/inputword',      // URL 
            name: "inputword",
            component: InputWordPage,
            meta:{
                title:'PICK UP WORD',
            },
             // 上記URLのときに表示するコンポーネント
        },
        {
            path:'/result',      // URL 
            name: "result",
            component: ResultPage,
            meta:{
                title:'RESULT',
            },
             // 上記URLのときに表示するコンポーネント
        },
        {
            path:'/standby',      // URL 
            name: "standby", //
            component: StandByPage,
            meta:{
                title:'',
            },
             // 上記URLのときに表示するコンポーネント
        },
        {
            path:'/submittext',      // URL 
            name: "submittext", //
            component: SubmitTextPage,
            meta:{
                title:'MAKE A TEXT',
            },
             // 上記URLのときに表示するコンポーネント
        },
        {
            path:'/vote',      // URL 
            name: "vote", //
            component: VotePage,
            meta:{
                title:'VOTE THE BEST',
            },
             // 上記URLのときに表示するコンポーネント
        },
    ]
})

export default router;
router.afterEach((to,from) =>{
    console.log(from)
    if (to.meta && to.meta.title) {
        document.title = to.meta.title
    }
})