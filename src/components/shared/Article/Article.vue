<script setup>
defineProps({
    blog : {
        id: String,
        title: String,
        content: String,
        date: String,
        imageURL: [
        String
        ]
    }
})
</script>

<template>
    <div class="flex items-start font-montserrat my-6 mr-10">
        <i class="fa-solid fa-map h-7 mr-4"></i>
        <div>
            <h3 class="font-semibold text-2xl">{{ blog.title}}</h3>
            <p class="pb-2" style="color: rgb(156 163 175);">{{ blog.date }}</p>
            
            <p>
                {{ blog.content }}
            </p>
            
            <div class="flex flex-row flex-wrap">
                <img v-for="image in blog.imageURL" :src="image" alt="" class="max-h-94">
            </div>
        </div>
    </div>
</template>
