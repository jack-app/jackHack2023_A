<template>
   <div class="container-standby">
        <div class="maintext-standby">
            NOW LOADING ...
        </div>
        
        <div class="subtext-standby">
            参加者を集めています
        </div>
    </div>
</template>

<script>

export default {
name: 'StandByPage',

components: {
    
},

data: () => ({
    
}),
};
</script>
  <style>
.maintext-standby{
    font-size: 100px;
    color:#C08A9B;
    text-align: center;
    /* position: absolute;
  top: 50%;
  left: 50%; */
  /* margin: -25px 0 0 -25px; */
}
.container-standby{
    width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.subtext-standby{
color:#C08A9B;
font-size:xx-large;
}
</style>