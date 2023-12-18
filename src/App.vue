<template>
    <!-- Your template content -->
  </template>
  
  <script>
  import ProfileComponent from './Profile.vue'; 
  
  export default {
    data() {
      return {
        response_data: '',
      };
    },
    async mounted() {
      if (window.location.pathname === '/app/' || window.location.pathname === '/') {
        this.$router.push('/api/profile/');
      }
  
      const response = await fetch('http://localhost:8000/api/test.json');
      this.response_data = await response.json();
    },
    // other options and methods
  };
  
  // Define your routes here, outside the export default
  const routes = [
    // ... other routes
    { path: '/api/profile/', component: ProfileComponent },
  ];
  
  // If you're using Vue Router, the routes need to be part of the router instance
  // For example:
  // const router = new VueRouter({ routes });
  // new Vue({ router }).$mount('#app');
  
  </script>
  