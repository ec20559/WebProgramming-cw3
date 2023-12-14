<template>
    <div class="container pt-3">
        <div class="h1 text-center border rounded bg-light p-2 mb-3">
            API Client
        </div>
        <div class="mb-3">
            <u>Response data</u>:             
        </div>
        <pre>{{ response_data }}</pre>
    </div>
  </template>
  
<script>
export default {
    data() {
        return {
            response_data: '',
        }
    },
    async mounted() {

        if (window.location.pathname === '/app/' || window.location.pathname === '/') {
        this.$router.push('/profile/');
    }

        const response = await fetch('http://localhost:8000/api/test.json')
        this.response_data = await response.json()
    }
}

const routes = [
  // ... other routes
  { path: '/profile/', component: ProfileComponent }
];




</script>
