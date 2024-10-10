<script setup>
defineProps({
  card : {
    label: String,
    link : String
  }
})
</script>

<template>
    <a :href="card.link" class="w-full h-auto flex justify-center items-center ">
      <div class="hvr-float text-center w-full flex flex-col mx-auto shadow-2xl gap-4 bg-secondary rounded-2xl py-5 my-8">
        <h3 class="font-pt-serif font-normal text-2xl my-8 mx-4">{{ card.label }}</h3>
      </div>
    </a>
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
  -webkit-transform: translateY(-50px);
  transform: translateY(-50px);
}

</style>