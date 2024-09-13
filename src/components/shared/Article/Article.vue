<script setup>
defineProps({
    blog : {
        label : String,
        description: String
    }
})
</script>

<template>
    <div class="flex items-start font-montserrat my-6 mr-10">
        <img src='/assets/logos/Heart.svg' alt='' class="h-7 mr-4" />
        <div>
            <h3 class="font-semibold text-2xl">{{ blog.label}}</h3>
            <p>
                {{ blog.description }}
            </p>
        </div>
    </div>
</template>
