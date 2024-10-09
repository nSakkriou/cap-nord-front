<template>
  <!--<Nav :navArray='navArray'></Nav>-->
  <Hero></Hero>
  <ConceptProjet :cardArray='cardArray'></ConceptProjet>
  <AvanceProjet :articleArray="articleArray"></AvanceProjet>
  <MapSection></MapSection>
  <FAQ :faq_item_array="faq_item_array"></FAQ>
  <Footer></Footer>
</template>

<script setup>
import Footer from './components/Footer.vue';
import Nav from './components/Nav.vue';
import Hero from "./components/Hero.vue";
import FAQ from "./components/PartenaireSection.vue";
import ConceptProjet from "./components/ConceptProjetSection.vue";
import AvanceProjet from "./components/BlogSection.vue"
import MapSection from './components/MapSection.vue';
import { getAllBlog } from "./service/blog"
import { ref } from "vue"

const navArray = [
  {
    label : "Le concept",
    url: "#concept"
  },
  {
    label: "Mon Blog",
    url : "#blog"
  },
  {
    label : "Mon avancée",
    url: "#map-section"
  },
  {
    label: "Mes partenaires",
    url : "#partenaire"
  }
]

const cardArray = [
  {
    label : "Mon blog",
    link : "#blog"
  },
  {
    label : "Mon avancée",
    link : "#map-section"
  },
  {
    label : "Mes partenaires",
    link : "#partenaire"
  }
]

let articleArray = ref([
])

getAllBlog().then(res => {
  let data = res.data
  data = data.reverse()
  articleArray.value = data
})

const faq_item_array = [
  {
    question : "Partenaire 1",
    response : "Info partenaire 1",
    logo_url : ""
  },
  {
    question : "Partenaire 2",
    response : "Info partenaire 2",
    logo_url : ""
  }
]

</script>
