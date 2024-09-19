<template>
    <Nav :navArray='navArray'></Nav>
  <Hero></Hero>
  <ConceptProjet :cardArray='cardArray'></ConceptProjet>
  <AvanceProjet :articleArray="articleArray"></AvanceProjet>
  <MapSection></MapSection>
  <FAQ :faq_item_array="faq_item_array"></FAQ>
  <Footer></Footer>
</template>

<script setup>
import Footer from './components/Footer/Footer.vue';
import Nav from './components/Nav/Nav.vue';
import Hero from "./components/Hero/Hero.vue";
import FAQ from "./components/FAQ/FAQ.vue";
import ConceptProjet from "./components/ConceptProjet/ConceptProjet.vue";
import AvanceProjet from "./components/AvanceProjet/AvanceProjet.vue"
import MapSection from './components/Map/MapSection.vue';
import { getAllBlog } from "./service/blog/blog"
import { ref } from "vue"

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
    label: "Concept du projet",
    link : ""
  },
  {
    label : "Carte GPX",
    link : "#map-section"
  },
  {
    label : "Les partenaires",
    link : ""
  }
]

let articleArray = ref([
])

getAllBlog().then(res => {
  let data = res.data
  console.log(data)
  articleArray.value = data
})

const faq_item_array = [
  {
    question : "Question 1",
    response : "Réponse 1"
  },
  {
    question : "Question 2",
    response : "Réponse 2"
  }
]

</script>
