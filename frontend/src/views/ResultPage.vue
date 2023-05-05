<template>

    <div>

            <div class="firsttext">
                aaa
            </div>
        <div class="under">
            <!-- 順位 -->
            <div class="allresult">
                <div style="display: flex;">
                    <div style="font-size:40px;">１位</div>
                    <div style="font-size:40px;margin-left:30px">一位の名前</div>
                </div>
                <div class="No2345-result">
                    <div class="resultNo-result">２位</div>
                    <div class="name-result">２位の名前</div>
                    <div class="resultNo-result">３位</div>
                    <div class="name-result">３位の名前</div>
                </div>
                <div class="No2345-result">
                    <div class="resultNo-result">４位</div>
                    <div class="name-result">４位の名前</div>
                    <div class="resultNo-result">５位</div>
                    <div class="name-result">５位の名前</div>
                </div>
            </div>

            <div class="myresult">
                ccc
            </div>
        </div>
    </div>

    

    
</template>
  
<script>

export default {
name: 'ResultPage',

components: {
    
},

data: () => ({
    
}),
};
</script>

<style>

.firsttext{
    border:1px solid #000;
    margin:50px;
    width:1150px;
    height:200px;

}

.under{
    display :flex;
}

.allresult{
    border:1px solid #000;
    color:white;
    background-color:#C08A9B;
    margin-left :70px;
    width: 700px;
    height:150px; 
   
}

.myresult{
    
    border:1px solid #000;
    margin-left :30px;
    width:300px;
    height:150px;

}
/* 一位以外の〇位の装飾 */
.resultNo-result{
font-size: 30px;
}
/* ２，３,4,5位の並び方 */
.No2345-result{
display: flex;
gap:40px;
}
.No1-result{
    color:black;
    font-size:40px;
}
/* 名前の装飾 */
.name-result{
font-size:30px;
margin-left:px;
}
</style>