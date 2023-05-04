<template>
    <div class="d-flex_align-center_flex-column">
        <v-card
    class="mx-auto"
    max-width="450"
    variant="outlined"
  >
    <v-card-item>
      <div>
    
        <div class="text-h6 mb-1">
          --ルール説明--
        </div>
        <div class="text-caption">
            <div class="ruleteller-title">
            <p>みんなが出した単語を使ってロマンチックな文章を作ろう！</p>
            <p>1. お題に合わせて好きな単語を打ち込んでください！</p> 
            <p>2. ５人それぞれが選んだ単語を使ってロマンチックな文章を作りましょう！</p>
            <p>3. 一番ロマンチックな文章を書いた人に投票しよう！</p>
        </div>
       </div>
      </div>
    </v-card-item>

  </v-card>
    </div>

</template>



<script>

export default {
name: 'TitlePage',

components: {
    
},

data: () => ({
    
}),
};
</script>
  
<style>
.d-flex_align-center_flex-column{
    display: flex;
  justify-content: center;
  align-items: center;
    /* width: 100%;
  margin: 0 auto;
  max-width: 500px; */
}
.ruleteller-title{
}
</style>