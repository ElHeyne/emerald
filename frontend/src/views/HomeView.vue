<script setup>
import ServersListing from '../components/ServersListing.vue'
import SimpleStats from '../components/SimpleStats.vue'
</script>

<template>
  <main class="grid grid-cols-4 gap-6 p-6">
    <aside class="max-w-64 col-span-1 flex flex-col space-y-4">
      <ServersListing />
    </aside>

    <section class="col-span-3 grid grid-rows-[auto,1fr] gap-4 self-start">
      <section class="grid grid-cols-2 gap-4">
        <SimpleStats />
        <div class="p-4 bg-white shadow rounded-xl">Content</div>
        <div class="p-4 bg-white shadow rounded-xl col-span-2">Logs</div>
      </section>
    </section>
  </main>
</template>
