<template>
  <Nav :navArray='navArray'></Nav>
  <Hero></Hero>
  <ConceptProjet :cardArray='cardArray'></ConceptProjet>
  <AvanceProjet :articleArray="articleArray"></AvanceProjet>
  <FAQ></FAQ>
  <Footer></Footer>
</template>

<script setup>
import Footer from './components/Footer/Footer.vue';
import Nav from './components/Nav/Nav.vue';
import Hero from "./components/Hero/Hero.vue";
import FAQ from "./components/FAQ/FAQ.vue";
import ConceptProjet from "./components/ConceptProjet/ConceptProjet.vue";
import AvanceProjet from "./components/AvanceProjet/AvanceProjet.vue"


const navArray = [
  {
    label : "Mon projets",
    url: "/projects"
  },
  {
    label: "Avancée du projet",
    url : "/avancee"
  }
]

const cardArray = [{
    label: "Concept du projet"
  },
  {
    label : "Carte GPX"
  },
  {
    label : "Les partenaires"
  }
]

const articleArray = [
{
  label : "Premier jour", 
  description : "lorem feergregregregregrereregerg"
},
{
  label : "Deuxième jour", 
  description : "lorem feergregregregregrereregerg"
}
]

</script>
