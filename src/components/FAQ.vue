<template>
    <div id="partenaire"></div>
    <section id="partenaire-div" class="sectionSize items-start pt-8 md:pt-36 bg-black text-white">
    <div>
      <h2 class="secondaryTitle bg-highlight3 p-10 mb-0 bg-center bg-100%">
        Partenaire
      </h2>
    </div>
    
    <FAQItem v-for="faq_item in faq_item_array" :faq_item="faq_item"></FAQItem>
  </section>
</template>

<script setup>
import FAQItem from './shared/FAQItem.vue';

defineProps({
  faq_item_array : [
    {
      question: String,
      response: String
    }
  ]
})
</script>