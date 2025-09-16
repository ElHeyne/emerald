<script setup>
import ServersListing from '../components/ServersListing.vue'
</script>

<template>
  <div class="grid grid-cols-4 gap-6 p-6">
    <aside class="col-span-1 flex flex-col space-y-4">
      <ServersListing />
    </aside>

    <!-- Main Content -->
    <main class="col-span-3 grid grid-rows-[auto,1fr] gap-4 self-start">
      <!-- Top Bar -->
      <header class="flex items-center justify-between">
        <!-- filters, search -->
      </header>

      <!-- Dashboard Panels -->
      <section class="grid grid-cols-2 gap-4">
        <div class="p-4 bg-white shadow rounded-xl">Containers</div>
        <div class="p-4 bg-white shadow rounded-xl">Stats</div>
        <div class="p-4 bg-white shadow rounded-xl col-span-2">Logs</div>
      </section>
    </main>
  </div>
</template>
