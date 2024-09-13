<script setup>
defineProps({
  card : {
    label: String
  }
})
</script>

<template>
  <div class='hvr-float text-center flex-1 flex flex-col mx-6 shadow-2xl relative bg-secondary rounded-2xl py-5 px-8 my-8'>
    <h3 class="font-pt-serif font-normal text-2xl my-8">
      {{ card.label }}
    </h3>
    
    <!-- <div class="font-montserrat font-bold text-2xl mb-4">
          $25
          <span class="font-normal text-base"> / month</span>
        </div>

        <div class="flex">
          <img src='/assets/logos/CheckedBox.svg' alt="" class="mr-1" />
          <p>Benefit #1</p>
        </div>
        <div class="flex">
          <img src='/assets/logos/CheckedBox.svg' alt="" class="mr-1" />
          <p>Benefit #2</p>
        </div>
        <div class="flex">
          <img src='/assets/logos/CheckedBox.svg' alt="" class="mr-1" />
          <p>Benefit #3</p>
        </div>

        <button class=" border-2 border-solid border-black rounded-xl text-lg py-3 mt-4">
          Choose plan
        </button> -->
  </div>
</template>

<style scoped>
/* Float */
.hvr-float {
  display: inline-block;
  vertical-align: middle;
  -webkit-transform: perspective(1px) translateZ(0);
  transform: perspective(1px) translateZ(0);
  box-shadow: 0 0 1px rgba(0, 0, 0, 0);
  -webkit-transition-duration: 0.3s;
  transition-duration: 0.3s;
  -webkit-transition-property: transform;
  transition-property: transform;
  -webkit-transition-timing-function: ease-out;
  transition-timing-function: ease-out;
}
.hvr-float:hover, .hvr-float:focus, .hvr-float:active {
  -webkit-transform: translateY(-8px);
  transform: translateY(-8px);
}

</style>