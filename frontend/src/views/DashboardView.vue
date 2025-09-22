<script setup>
import ServersListing from '../components/ServersListing.vue'
</script>
<template>
  <main class="flex gap-8 w-fit">
    <aside
      class="p-6 col-span-2 flex flex-col w-sm bg-em-gray-darker border-r border-green-500"
      style="height: calc(100dvh - 81px)"
    >
      <!-- Add a preference in the settings to get a version w no background and no border, just as the original -->
      <ServersListing />
    </aside>
    <section class="p-6 col-span-6 flex flex-col">
      <router-view :key="$route.fullPath" />
    </section>
  </main>
</template>
