<script setup>
defineProps({
    blog : {
        label : String,
        description: String,
        date: String
    }
})
</script>

<template>
    <div class="flex items-start font-montserrat my-6 mr-10">
        <i class="fa-solid fa-map h-7 mr-4"></i>
        <div>
            <h3 class="font-semibold text-2xl">{{ blog.label}}</h3>
            <p class="pb-2" style="color: rgb(156 163 175);">{{ blog.date }}</p>
            
            <p>
                {{ blog.description }}
            </p>
        </div>
    </div>
</template>
