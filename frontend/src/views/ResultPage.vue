<template>

    <div>

            <div class="firsttext">
                aaa
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