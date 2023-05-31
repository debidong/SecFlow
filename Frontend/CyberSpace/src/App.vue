<script>
import Login from './components/Login.vue'
import UserList from './components/UserList.vue'

export default {
  components: {
    Login,
    UserList
  }
}
</script>

<template>
  <main>
    <router-view :key="$route.path" />
  </main>
</template>

<style>
  #cyberspace {
    color: aqua;
  }
  /* h1 {
    
  }
  p {
    font-family:
  } */
</style>
