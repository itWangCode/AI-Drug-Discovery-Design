// src/main.js
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import './assets/iconfont/iconfont.css'; // 引入图标样式

createApp(App).use(router).mount('#app');

