// import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

const app = createApp(App)


// const cors = require('cors');
// const corsOptions = {
//   exposedHeaders: 'token',
// };

// app.use(cors(corsOptions));
app.use(ElementPlus, { size: 'small', zIndex: 3000 })
app.use(router)

app.mount('#app')

