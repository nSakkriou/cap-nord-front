<template>
    <div toggleElement class="cursor-pointer w-full py-4">
      <div class="flex justify-between items-center">
        <div question class="font-montserrat font-medium mr-auto">
          {{ faq_item.question }}
        </div>
        <img src='/assets/logos/CaretRight.svg' alt="" class="transform transition-transform" />
      </div>
      <div answer class="font-montserrat text-sm font-extralight pb-8 hidden">
        {{  faq_item.response }}
    </div>
    </div>
    <hr class="w-full bg-white" />
</template>

<script setup>
defineProps({
    faq_item : {
        question: String,
        response: String
    }
})

</script>