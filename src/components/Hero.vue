<template>
  <section
    class="pt-24 md:mt-0 pb-24 flex flex-col justify-center text-center md:text-left md:flex-row md:justify-between md:items-center lg:px-48 md:px-12 px-4 bg-secondary">
    <div class="md:flex-1 md:mr-10">
      <h1 class="font-pt-serif text-5xl font-bold mb-7">
        PROJET
        <span class="bg-underline1 bg-left-bottom bg-no-repeat pb-2 bg-100%">
          Cap Nord
        </span>
      </h1>
      <p class="font-pt-serif font-normal mb-7">
        Le projet est de relier Amsterdam au Cap Nord en vélo ...
      </p>

      <div v-if="isTheo">
        Que pour toi théo : <a href="https://nathansakkriou.com/cap-nord">Lien pour le dashboard</a>
      </div>
      
      <!-- 
      <div class="font-montserrat">
        <button class="bg-black px-6 py-4 rounded-lg border-2 border-black border-solid text-white mr-2 mb-2">
          Call to action
        </button>
        <button class="px-6 py-4 border-2 border-black border-solid rounded-lg">
          Secondary action
        </button>
      </div>
      -->
      
    </div>
    <div class="flex justify-around md:block mt-8 md:mt-0 md:flex-1">
      
      <div class="relative">
        <img src='/assets/Highlight1.svg' alt="" class="absolute -top-16 -left-10" />
      </div>
      
      <img src='/assets/cap_nord/logo.png' alt="Macbook" />
      
      <div class="relative">
        <img src='/assets/Highlight2.svg' alt="" class="absolute -bottom-10 -right-1" />
      </div>
    </div>
    </section>
</template>

<script setup>

import {ref} from "vue";

let currentURL = document.location.href
let isTheo = ref(false)

if(currentURL.indexOf("whois=theo") !== -1) {
  isTheo.value = true
}


</script>