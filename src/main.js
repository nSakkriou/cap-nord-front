import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import Nav from './components/Nav.vue'
import Hero from './components/Hero.vue'

const app = createApp(App)

app.component("Nav", Nav)
    .component("Hero", Hero)

app.mount('#app')
