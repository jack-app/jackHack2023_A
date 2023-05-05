<template>

    <div>

            <div class="firsttext">
                <img class="hidari-resu" src="../assets/hidari.jpg" alt=""> 
                <p class="result-text">sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss</p>
                <img class="migi-resu" src="../assets/migi.jpg" alt="">
                
            </div>
        <div class="under">
            <div class="allresult">
                bbb
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

    display: flex;
    margin:50px;
    width:1150px;
    height:200px;

}

.hidari-resu{
    width:250px;
    height:150px;
    z-index: 1;
    position:fixed;
}

.result-text{
    padding:50px;
    z-index: 2;
    Word-break:break-all;
}

.migi-resu{
    width:250px;
    height:150px;
    margin-top:30px;
    margin-left: 900px;
    z-index: 1;
    position:fixed;
}

.under{
    display :flex;
}

.allresult{
    border:1px solid #000;
   
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

</style>