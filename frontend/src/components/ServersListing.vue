<script setup>
import { onMounted, computed, reactive } from 'vue'
import PulseLoader from 'vue-spinner/src/PulseLoader.vue'
import ServersListingCard from './ServersListingCard.vue'

const state = reactive({
  containers: [],
  isLoading: true,
})

onMounted(async () => {
  try {
    const res = await fetch('/pythonapi/containers?all=true')
    const data = await res.json()
    state.containers = data
    if (data.detail === "Not Found") {
      throw new Error ('Pythonapi, Containers not found.') /* TODO Show specific error message on the web if the error is due and api not found */
    }
  } catch (error) {
    console.error('Error fetching containers: ', error)
  } finally {
    state.isLoading = false
  }
})

const noServers = computed(() => state.containers.length === 0)
const notFound = computed(() => state.containers.detail === "Not Found")
</script>

<template>
  <section>
    <h1 class="text-2xl font-bold mb-2.5">Minecraft Servers</h1>

    <!-- Loader -->
    <div v-if="state.isLoading" class="text-center text-gray-500 py-6">
      <PulseLoader />
    </div>

    <span v-if="noServers && !state.isLoading">No Servers</span>
    <span v-if="notFound && !state.isLoading">Python Api Error: Fetch URL Not Found</span>
    <ul v-if="(!noServers && !notFound) && !state.isLoading">
      <ServersListingCard
        v-for="container in state.containers"
        :key="container.id"
        :server="container"
      />
    </ul>
  </section>
</template>
