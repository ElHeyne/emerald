<script setup>
import Navbar from '../components/Navbar.vue'
</script>

<template>
  <Navbar />
  <!-- TODO add login logic to show navbar or login screen -->

  <router-view />
  <!-- v-if="$root.loggedIn -->
</template>
