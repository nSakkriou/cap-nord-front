import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  server: {
    port: 3000, // Modifie le port si nécessaire
    cors: {
      origin: '*',  // Autoriser toutes les origines
      methods: ['GET', 'POST'],  // Autoriser uniquement GET et POST
    }
  },
  plugins: [vue()],
});
