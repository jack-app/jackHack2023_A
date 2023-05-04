<template>

  <div class="wrapper">

     <div class="oneone"><img class="hidari" src="../assets/hidari.jpg" alt=""></div>
     <div class="onetwo">
        Player 1
      <div class="text-center">
        <v-dialog
            v-model="dialog"
             width="auto"
            >
            <template v-slot:activator="{ props }">
                <v-btn
                 color="primary"
                 v-bind="props"
                 >
                    Open Text
                </v-btn>
            </template>

            <v-card>
                <v-card-text>
                 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                </v-card-text>
                <v-card-actions>
                    <v-btn color="primary" block @click="dialog = false">Close Text</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
      </div>
     </div>     
     <div class="onethree"><img class="migi" src="../assets/migi.jpg" alt=""></div>
     <div class="onefour"> <v-btn size="x-large" color="primary"> ---- vote---- </v-btn></div>




     <div class="oneone"><img class="hidari" src="../assets/hidari.jpg" alt=""></div>
     <div class="onetwo">
        Player 2
      <div class="text-center">
        <v-dialog
            v-model="dialog"
             width="auto"
            >
            <template v-slot:activator="{ props }">
                <v-btn
                 color="primary"
                 v-bind="props"
                 >
                    Open Text
                </v-btn>
            </template>

            <v-card>
                <v-card-text>
                 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                </v-card-text>
                <v-card-actions>
                    <v-btn color="primary" block @click="dialog = false">Close Text</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
      </div>
     </div>     
     <div class="onethree"><img class="migi" src="../assets/migi.jpg" alt=""></div>
     <div class="onefour"> <v-btn size="x-large" color="primary"> ---- vote---- </v-btn></div>


     <div class="oneone"><img class="hidari" src="../assets/hidari.jpg" alt=""></div>
     <div class="onetwo">
        Player 3
      <div class="text-center">
        <v-dialog
            v-model="dialog"
             width="auto"
            >
            <template v-slot:activator="{ props }">
                <v-btn
                 color="primary"
                 v-bind="props"
                 >
                    Open Text
                </v-btn>
            </template>

            <v-card>
                <v-card-text>
                 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                </v-card-text>
                <v-card-actions>
                    <v-btn color="primary" block @click="dialog = false">Close Text</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
      </div>
     </div>     
     <div class="onethree"><img class="migi" src="../assets/migi.jpg" alt=""></div>
     <div class="onefour"> <v-btn size="x-large" color="primary"> ---- vote---- </v-btn></div>


     <div class="oneone"><img class="hidari" src="../assets/hidari.jpg" alt=""></div>
     <div class="onetwo">
        Player 4
      <div class="text-center">
        <v-dialog
            v-model="dialog"
             width="auto"
            >
            <template v-slot:activator="{ props }">
                <v-btn
                 color="primary"
                 v-bind="props"
                 >
                    Open Text
                </v-btn>
            </template>

            <v-card>
                <v-card-text>
                 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                </v-card-text>
                <v-card-actions>
                    <v-btn color="primary" block @click="dialog = false">Close Text</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
      </div>
     </div>     
     <div class="onethree"><img class="migi" src="../assets/migi.jpg" alt=""></div>
     <div class="onefour"> <v-btn size="x-large" color="primary"> ---- vote---- </v-btn></div>


     <div class="oneone"><img class="hidari" src="../assets/hidari.jpg" alt=""></div>
     <div class="onetwo">
        Player 5
      <div class="text-center">
        <v-dialog
            v-model="dialog"
             width="auto"
            >
            <template v-slot:activator="{ props }">
                <v-btn
                 color="primary"
                 v-bind="props"
                 >
                    Open Text
                </v-btn>
            </template>

            <v-card>
                <v-card-text>
                 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                </v-card-text>
                <v-card-actions>
                    <v-btn color="primary" block @click="dialog = false">Close Text</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
      </div>
     </div>     
     <div class="onethree"><img class="migi" src="../assets/migi.jpg" alt=""></div>
     <div class="onefour"> <v-btn size="x-large" color="primary"> ---- vote---- </v-btn></div>


    


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
  margin: 30px;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-rows: 200px;
  
   }

.onetwo{
    table-layout: fixed;
    font-size: 30px;
    text-align: center;
    padding: 30px;

}


.onefour{
    margin-top: 50px;
    padding: 30px;
    text-align: center;
    
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