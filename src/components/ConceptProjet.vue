<script setup>
import Card from './shared/Card.vue';

// Les props pour le tableau de cartes
defineProps({
  cardArray: [
    {
      label: String
    }
  ]
});

// Variable pour suivre l'ordre pair/impair
let odd = false;

</script>

<template>
<section class="bg-black text-white sectionSize">
  <div>
    <h2 class="text-white secondaryTitle bg-underline2 bg-100%">
      Comprendre mon projet
    </h2>
  </div>

  <div class="text-black w-full items-center flex flex-col md:flex-row justify-between pb-7">
      <!-- Utiliser la fonction pour assigner dynamiquement la classe -->
      <Card 
        v-for="(card, index) in cardArray" 
        :key="index" 
        :card="card" 
      />
    </div>

    <h2 class="text-white secondaryTitle bg-underline2 bg-100%">
      Le concept
    </h2>

    <div>
      Lorem, ipsum dolor sit amet consectetur adipisicing elit. Cum vel officia quibusdam distinctio itaque iste non, quod eos. Adipisci dignissimos quaerat nobis nisi aliquam magnam illum cum ad quibusdam quas.
    </div>
  </section>
</template>
