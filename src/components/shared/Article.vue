<script setup>
import { ref } from 'vue';

const props = defineProps({
    blog: {
        id: String,
        title: String,
        content: String,
        date: String,
        imageURL: [String],
    },
});

const showFullContent = ref(false);

const toggleContent = () => {
    showFullContent.value = !showFullContent.value;
};
</script>

<template>
    <div style="background-color: whitesmoke;" class="article-container w-full mb-4 max-w-6xl mx-auto p-6 bg-white rounded-lg shadow-lg">
        <div class="flex items-start mb-6">
            <div class="w-full">
                <h3 class="font-semibold text-3xl text-gray-800">{{ blog.title }}</h3>
                <p class="text-sm text-gray-400">{{ blog.date }}</p>

                <!-- Display either a truncated version or the full content -->
                <p class="mt-4 text-gray-700">
                    <span v-if="!showFullContent">
                        {{ blog.content.substring(0, 200) }}...
                        <p>
                            <button @click="toggleContent" class="ml-2 text-blue-600 hover:underline">
                                Voir plus
                            </button>
                        </p>
                    </span>
                    <span v-else>
                        {{ blog.content }}
                        <p><button @click="toggleContent" class="ml-2 text-blue-600 hover:underline">
                                Voir moins
                            </button>
                        </p>
                    </span>
                </p>

                <!-- Responsive Image carousel -->
                <div class="carousel mt-6">
                    <div class="flex overflow-x-auto space-x-4 pb-2 scroll-smooth snap-x snap-mandatory">
                        <a v-for="(image, index) in blog.imageURL" :key="index" :href="image" target="_blank"
                            class="block min-w-[80%] md:min-w-[45%] lg:min-w-[30%] snap-center">
                            <img :src="image" alt="Image"
                                class="h-48 w-full object-cover rounded-lg shadow-md transition-transform duration-300 transform hover:scale-105" />
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.carousel {
    scrollbar-width: none;
    /* Hide scrollbar in Firefox */
}

.carousel::-webkit-scrollbar {
    display: none;
    /* Hide scrollbar in Chrome, Safari, Opera */
}
</style>
