<template>
    <div toggleElement class="cursor-pointer w-full py-4">
      <div class="flex justify-between items-center">
        <div question class="font-montserrat font-medium mr-auto">
          {{ faq_item.question }}
        </div>

        <div class="flex justify-center flex-row">
          <div class="bg-white rounded-md">
            <img class="p-2" :src="faq_item.logo_url" :alt="'Logo de ' + faq_item.question " style="height: 70px; width: auto"/>
          </div>
          <img src='/assets/logos/CaretRight.svg' alt="" class="transform transition-transform" />
        </div>
      </div>
      <div answer class="font-montserrat text-md font-extralight pb-8 hidden mt-4">
        {{  faq_item.response }}
    </div>
    </div>
    <hr class="w-full bg-white" />
</template>

<script setup>
defineProps({
    faq_item : {
        question: String,
        response: String,
        logo_url: String
    }
})

</script>