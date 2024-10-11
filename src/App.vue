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
    label : "Journal de bord",
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
    question : "Bourse Ajir",
    response : "La Bourse Ajir, porté par la Ligue de l’Enseignement et le Département de la Manche, soutient des projets à l'initiative des jeunes de 11 à 25 ans qui ont une utilité sociale sur le territoire.",
    logo_url : "https://nathansakkriou.com/webContent/get/aafcae27-708b-4d14-b8be-2e5cdb077b76"
  },
  {
    question : "Pass Monde Initiative - La Région Normandie",
    response : " La Région Normandie a lancé le dispositif Pass Monde pour soutenir la mobilité internationale des jeunes normands. Ce programme vise à favoriser leur autonomie, l’ouverture au monde, et à élargir leurs perspectives personnelles et professionnelles à travers des projets de mobilité.",
    logo_url : "https://nathansakkriou.com/webContent/get/9a059de3-bca2-43aa-8ef1-14122d1bb6d1"
  }
]

</script>

<style>
.codex-editor__redactor {
  padding-bottom: 20px !important;
}
</style>
