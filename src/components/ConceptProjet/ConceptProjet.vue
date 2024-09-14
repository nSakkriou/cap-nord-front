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

// Fonction pour alterner les classes
const getTopClass = () => {
  odd = !odd;
  return odd ? "mb:top-24" : "mb:top-12";
};
</script>

<template>
  <section class="bg-black text-white sectionSize">
    <div>
      <h2 class="text-white secondaryTitle bg-underline2 bg-100%">Comprendre mon projet</h2>
    </div>

    <div class="text-black flex w-full flex-col md:flex-row pb-7">
      <!-- Utiliser la fonction pour assigner dynamiquement la classe -->
      <Card 
        v-for="(card, index) in cardArray" 
        :key="index" 
        :card="card" 
        :class="getTopClass()"
      />
    </div>
  </section>
</template>
