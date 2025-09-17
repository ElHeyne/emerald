<script setup>
import SimpleStats from '../components/SimpleStats.vue'
</script>

<template>
  <section class="grid grid-cols-2 gap-4">
    <div class="col-span-1">
      <SimpleStats />
    </div>
    <div class="p-4 bg-em-gray-soft shadow rounded-xl">Terminal</div>
    <div class="p-4 bg-em-gray-soft rounded-xl col-span-2">Logs</div>
    <div class="p-4 bg-em-gray-soft rounded-xl col-span-2">Performance</div>
  </section>
</template>
