<script setup>
import { onMounted, computed, reactive } from 'vue'
import PulseLoader from 'vue-spinner/src/PulseLoader.vue'
import ServersListingCard from './ServersListingCard.vue'

const state = reactive({
  containers: [],
  isLoading: true,
})

const noServers = computed(() => state.containers.length === 0)

onMounted(async () => {
  try {
    const res = await fetch('/pythonapi/containers?all=true')
    const data = await res.json()
    state.containers = data
  } catch (error) {
    console.error('Error fetching containers: ', error)
  } finally {
    state.isLoading = false
  }
})
</script>

<template>
  <section>
    <h1 class="text-2xl font-bold mb-2.5">Minecraft Servers</h1>

    <!-- Loader -->
    <div v-if="state.isLoading" class="text-center text-gray-500 py-6">
      <PulseLoader />
    </div>

    <ul>
      <span v-if="noServers && state.isLoading">No Servers</span>
      <ServersListingCard
        v-for="container in state.containers"
        :key="container.id"
        :server="container"
      />
    </ul>
  </section>
</template>
