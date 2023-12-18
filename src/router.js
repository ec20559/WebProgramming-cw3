import Vue from 'vue';
import VueRouter from 'vue-router';
import ProfileComponent from './Profile.vue';

Vue.use(VueRouter);

const routes = [
  // ... other routes
  { path: '/api/profile/', component: ProfileComponent },
];

export default new VueRouter({ routes });
