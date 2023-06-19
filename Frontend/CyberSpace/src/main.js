 import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'

import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

const app = createApp(App)

axios.defaults.baseURL = ''
app.use(ElementPlus, { size: 'small', zIndex: 3000 })
app.use(router)

app.mount('#app')

