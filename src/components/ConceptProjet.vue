<script setup>
import Card from '../shared/Card/Card.vue';

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
  </section>
</template>
