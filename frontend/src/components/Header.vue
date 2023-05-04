<template>
    <v-app-bar
    app
    color="primary"
    height="100"
    >
        <v-app-bar-title
        color = "white"
        >
            {{ message }}
        </v-app-bar-title>
        <div class = "label-header"></div>
    </v-app-bar>
</template>

<script>
export default {
    name: 'HeaderItem',
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
</style>