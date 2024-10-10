<template>
  <!--<Nav :navArray='navArray'></Nav>-->
  <Hero></Hero>
  <ConceptProjetSection :cardArray='cardArray'></ConceptProjetSection>
  <BlogSection :articleArray="articleArray"></BlogSection>
  <MapSection></MapSection>
  <PartenaireSection :faq_item_array="faq_item_array"></PartenaireSection>
  <Footer></Footer>
</template>

<script setup>
import Footer from './components/Footer.vue';
import Hero from "./components/Hero.vue";
import MapSection from './components/MapSection.vue';
import { getAllBlog } from "./service/blog"
import { ref } from "vue"
import ConceptProjetSection from "./components/ConceptProjetSection.vue";
import BlogSection from "./components/BlogSection.vue";
import PartenaireSection from "./components/PartenaireSection.vue";

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
