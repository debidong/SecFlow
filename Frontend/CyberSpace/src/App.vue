<script>
import Login from './components/Login.vue';
import UserList from './components/UserList.vue';
import Register from './components/Register.vue';
import Chat from './components/Chat.vue';

export default {
  components: {
    Login,
    UserList,
    Register,
    Chat
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
