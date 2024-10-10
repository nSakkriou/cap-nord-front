

<template>
    <div style="background-color: whitesmoke;" class="article-container w-full mb-4 max-w-6xl mx-auto p-6 bg-white rounded-lg shadow-lg">
        <div class="flex items-start mb-6">
            <div class="w-full">
                <h3 class="font-semibold text-3xl text-gray-800">{{ blog.title }}</h3>
                <p class="text-sm text-gray-400">{{ blog.date }}</p>

                <!-- Display either a truncated version or the full content -->
              <div :id="idEditorjs"></div>
              <button @click="toggleContent" class="ml-2 text-blue-600 hover:underline">
                Voir plus
              </button>
              <!--
                <p class="mt-4 text-gray-700" v-if="!showFullContent">
                        {{ blog.content.substring(0, 200) }}...
                        <span>
                            <button @click="toggleContent" class="ml-2 text-blue-600 hover:underline">
                                Voir plus
                            </button>
                        </span>
                  </p>
                  <div v-else>
                      {{ blog.content }}
                      <p><button @click="toggleContent" class="ml-2 text-blue-600 hover:underline">
                              Voir moins
                          </button>
                       </p>
                  </div>
                  -->

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

<script setup>
import { ref } from 'vue';
import EditorJS from "@editorjs/editorjs";
import Header from "@editorjs/header";
import Paragraph from "@editorjs/paragraph";
import List from "@editorjs/list";
import ImageTool from "@editorjs/image";
import Quote from "@editorjs/quote";
import CodeTool from "@editorjs/code";
import Table from "@editorjs/table";
import Embed from "@editorjs/embed";
import Delimiter from "@editorjs/delimiter";

const props = defineProps({
  blog: {
    id: String,
    title: String,
    content: String,
    date: String,
    imageURL: [String],
  },
});

const idEditorjs = props.blog.id + '-editorjs'

const editor = new EditorJS({
  holder : idEditorjs,
  data: JSON.parse(props.blog.content),
  readOnly: true,

  tools: {
    /**
     * Bloc de titre.
     */
    header: {
      class:
      Header,
      inlineToolbar:
          ['link'], // Ajout d'une barre d'outils en ligne (ex. lien)
      config:
          {
            placeholder: 'Entrez un titre',
            levels:
                [1, 2, 3, 4], // Niveaux de titre disponibles
            defaultLevel:
                1
          }
    },

    /**
     * Bloc de paragraphe.
     */
    paragraph: {
      class:
      Paragraph,
      inlineToolbar:
          true // Ajout de la barre d'outils en ligne
    },

    /**
     * Bloc de liste ordonnée et non ordonnée.
     */
    list: {
      class:
      List,
      inlineToolbar:
          true,
      config:
          {
            defaultStyle: 'unordered' // Liste non ordonnée par défaut
          }
    },

    /**
     * Bloc d'image.
     */
    image: {
      class:
      ImageTool,
      config:
          {
            endpoints: {
              byFile: '/uploadFile', // Point d'upload du fichier
              byUrl:
                  '/fetchUrl', // Point d'upload par URL
            }
            ,
            caption: true, // Activer les légendes sous les images
            placeholder:
                'Téléchargez ou collez une URL d\'image'
          }
    },

    /**
     * Bloc de citation.
     */
    quote: {
      class:
      Quote,
      inlineToolbar:
          true,
      config:
          {
            quotePlaceholder: 'Tapez la citation',
            captionPlaceholder:
                'Auteur'
          }
    },

    /**
     * Bloc de code pour les extraits de code.
     */
    code: {
      class:
      CodeTool,
    },

    /**
     * Bloc de tableau.
     */
    table: {
      class:
      Table,
      inlineToolbar:
          true,
      config:
          {
            rows: 2, // Nombre initial de lignes
            cols:
                3, // Nombre initial de colonnes
          }
    },

    /**
     * Bloc d'intégration vidéo.
     */
    embed: {
      class:
      Embed,
      config:
          {
            services: {
              youtube: true,
              coub: true,
              vimeo: true,
            }
          }
    },
    delimiter: Delimiter,
  }
})

let showFullContent = false;

const toggleContent = () => {
  showFullContent = !showFullContent;

  if(showFullContent) {
    console.log(props.blog.content)
    editor.data = props.blog.content
  }
  else {
    console.log(props.blog.content.substring(0, 200))
    editor.data = props.blog.content.substring(0, 200)
  }
};
</script>

<style scoped>
.carousel {
    scrollbar-width: none;
    /* Hide scrollbar in Firefox */
}

.carousel::-webkit-scrollbar {
    display: none;
    /* Hide scrollbar in Chrome, Safari, Opera */
}

.ce-block__content {
  margin: unset;
}
</style>
