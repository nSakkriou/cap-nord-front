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
<section id="concept" class="bg-black text-white sectionSize">
  <div>
    <h2 class="text-center text-white secondaryTitle bg-underline2 bg-100%">
      Comprendre mon projet
    </h2>
  </div>

  <div class="text-black w-full md:gap-5 gap-0 items-center flex flex-col md:flex-row justify-between pb-7">
      <!-- Utiliser la fonction pour assigner dynamiquement la classe -->
      <Card 
        v-for="(card, index) in cardArray" 
        :key="index" 
        :card="card" 
      />
    </div>

    <h2 class="text-center text-white secondaryTitle bg-underline2 bg-100%">
      Le concept
    </h2>

    <div class="text-center">
      <p>Ce projet est un projet pédagogique destiné aux classes de primaire visant à proposer une ouverture culturelle vers l’étranger concrète, par le biais d’un voyage en vélo, en sensibilisant à différentes thématiques telles que la mobilité verte, l’ouverture vers autrui et la richesse culturelle du monde.</p>
      <p>Le voyage à vélo comme outil de sensibilisation à l’ouverture vers l’étranger et aux mobilités vertes </p>
    </div>
  </section>
</template>
