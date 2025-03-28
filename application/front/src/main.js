import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import VueGoodTablePlugin from 'vue-good-table-next'
import 'vue-good-table-next/dist/vue-good-table-next.css'

const app = createApp(App)
// app.config.globalProperties.$axios = axios;
app.use(VueGoodTablePlugin)
app.mount('#app')