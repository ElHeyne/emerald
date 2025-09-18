<script setup>
import { defineProps } from 'vue'
import { useRoute } from 'vue-router'

defineProps({
  server: {
    type: Object,
    default: null,
  },
})

const isActiveServer = (data) => {
  const route = useRoute()
  return route.path.includes(data)
}
</script>
<template>
  <RouterLink :to="`/servers/${server.id}`">
    <section
      class="max-w-sm p-3 border rounded-lg mb-3 duration-200 ease-in-out"
      :class="[
        isActiveServer(server.id) ? 'bg-green-900 border-green-500' : 'hover:bg-em-gray-light bg-em-gray-darker bd-em-gray-light',
      ]"
    >
      <div class="flex items-center">
        <i
          class="pi pi-circle-fill mr-2.5 text-sm"
          :class="{
            'state-exited': server.status === 'exited',
            'state-running': server.status === 'running',
            'state-paused': server.status === 'paused',
          }"
        ></i>
        <span class="overflow-hidden text-sm"> {{ server.name }} </span>
      </div>
    </section>
  </RouterLink>
</template>
