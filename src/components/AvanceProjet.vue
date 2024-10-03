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
  <section class="sectionSize bg-secondary">
    <div>
      <h2 class="secondaryTitle bg-underline3 bg-100%">Blog</h2>
    </div>
    <div class="flex flex-col">
      <Article v-for="article in articleArray" :blog="article"></Article>
    </div>
  </section>
</template>