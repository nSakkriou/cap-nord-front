<script setup>
import Article from './shared/Article.vue';

defineProps({
  articleArray: [{
    id: String,
    title: String,
    content: String,
    date: String,
    imageURL: [
      String
    ]
  }]
}
)
</script>


<template>
  <section class="sectionSize bg-secondary" id="blog">
    <div>
      <h2 class="secondaryTitle bg-underline3 bg-100%">Blog</h2>
    </div>
    <div class="flex flex-col">
      <p v-if="articleArray.length === 0">Je n'ai pas encore fait de post mais reviens vite afin de suivre mes aventures</p>
      <Article v-for="article in articleArray" :blog="article"></Article>
    </div>
  </section>
</template>