<template>
    <v-app-bar
    app
    color="primary"
    height="100"
    >
        <v-app-bar-title
        color = "white"
        >
            <div class = "title-header">
                {{ title }}
            </div>
        </v-app-bar-title>
        <div class = "label-header"></div>
    </v-app-bar>
</template>

<script>
export default {
    name: 'HeaderItem',
    props:["title"],
    data() {
        return{
            message: "hoge"
        }
    },
    created(){
        this.message = "ページに応じたタイトルを設定"
    }
}
</script>
<style>
.label-header{
    position: absolute;
    left: 90%;
    width: 10%;
    height: 30%;
    background: #FCDCCA;
    transform: rotate(-90deg);
}
.title-header{
    color: #ffffff;
    font-size: 30px;
}
</style>