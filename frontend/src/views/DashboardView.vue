<script setup>
import ServersListing from '../components/ServersListing.vue'
</script>
<template>
  <main class="grid grid-cols-8 gap-8 p-6">
    <aside class="col-span-2 flex flex-col">
      <ServersListing />
    </aside>
    <section class="col-span-6 flex flex-col">
      <router-view :key="$route.fullPath" />
    </section>
  </main>
</template>
