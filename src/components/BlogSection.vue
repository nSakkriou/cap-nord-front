<script setup>
import Article from './shared/Post.vue';
import { ref, computed, watch } from 'vue';

const props = defineProps(['articleArray']); // On passe simplement la prop

const maxShowArticle = 1
const currentPage = ref(0);

// Utilisation de computed pour rendre le calcul réactif
const maxPages = computed(() => Math.ceil(props.articleArray.length / maxShowArticle));

// Fonction pour changer de page
function switchPage(event) {
  let btn = event.target;
  const btnId = parseInt(btn.dataset.pageId)
  currentPage.value = btnId;
  window.location.href = "#blog"
}

const showArticle = computed(() => props.articleArray.slice(currentPage.value * maxShowArticle, maxShowArticle + (currentPage.value * maxShowArticle)))
</script>


<template>
  <section class="sectionSize bg-secondary" id="blog">
    <div>
      <h2 class="secondaryTitle bg-underline3 bg-100%">Blog</h2>
    </div>
    <div class="flex flex-col">
      <p v-if="articleArray.length === 0">Je n'ai pas encore fait de post mais reviens vite afin de suivre mes aventures</p>
      <Article v-for="article in showArticle" :blog="article"></Article>
    </div>

    <div v-if="maxPages > 1">
      <button v-for="i in maxPages" :class="{'bg-white' : true, 'p-2' : true, 'mr-2' : true, 'text-red' : currentPage === i-1}" :data-page-id="i-1" @click="switchPage">{{i}}</button>
    </div>

  </section>
</template>