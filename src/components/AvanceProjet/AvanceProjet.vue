<script setup>
import Article from '../shared/Article/Article.vue';

defineProps({
  articleArray: [{
    label: String,
    description: String
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