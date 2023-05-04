<template>
    <div class="vote-all">
        <div class="wrapper">
         
          <div class="oneone"><img class="hidari" src="../assets/hidariok.jpg" alt=""></div>
          <div class="onetwo">aiueokaki</div>
          <div class="onethree"><img class="migi" src="../assets/migiiii.jpg" alt=""></div>
          <div class="onefour"><button type="button" name="name" value="value">vote</button></div>

          <div class="oneone"><img class="hidari" src="../assets/hidariok.jpg" alt=""></div>
          <div class="onetwo"></div>
          <div class="onethree"><img class="migi" src="../assets/migiiii.jpg" alt=""></div>
          <div class="onefour"><button type="button" name="name" value="value">vote</button></div>

          <div class="oneone"><img class="hidari" src="../assets/hidariok.jpg" alt=""></div>
          <div class="onetwo"></div>
          <div class="onethree"><img class="migi" src="../assets/migiiii.jpg" alt=""></div>
          <div class="onefour"><button type="button" name="name" value="value">vote</button></div>

          <div class="oneone"><img class="hidari" src="../assets/hidariok.jpg" alt=""></div>
          <div class="onetwo"></div>
          <div class="onethree"><img class="migi" src="../assets/migiiii.jpg" alt=""></div>
          <div class="onefour"><button type="button" name="name" value="value">vote</button></div>
          
       </div>
 </div>
   
</template>
  

<script>

export default {
name: 'VotePage',

components: {
    
},

data: () => ({
    
}),
};
</script>
  
<style>
 

.wrapper {
  table-layout: fixed;
  margin: 40px;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-rows: 200px;
  
   }
   .onetwo{
    table-layout: fixed;
    font-size: 50px;
    text-align: center;
    padding: 40px;

}


.onefour{
    margin: 30px;
    padding: 10px;
    text-align: center;
    font-size: 70px;
    color: #FFFFFF;
    border-bottom: 1px solid;
    background-color: #C08A9B;

    
}

.hidari{
    width:300px;
    height:170px;
}

.migi{
    width:300px;
    height:170px; 
}
</style>