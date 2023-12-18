import { createApp } from 'vue'
import Vue from 'vue';
import App from './App.vue';
import router from './router'; // Import router

import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";


new Vue({
    router, // Use the router
    render: h => h(App)
  }).$mount('#app');

createApp(App).mount('#app')
