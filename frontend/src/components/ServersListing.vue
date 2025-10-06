<script setup>
import { onMounted, computed, reactive, watch } from 'vue'
import PulseLoader from 'vue-spinner/src/PulseLoader.vue'
import ServersListingCard from './ServersListingCard.vue'
import { useContainerStore } from '@/stores/containerStore'

const containerStore = useContainerStore()

const state = reactive({
  containers: [],
  isLoading: true,
})

onMounted(async () => {
  onMounted(async () => {
    const data = containerStore.list
    if (data.length >= 0) {
      state.containers = containerStore.list
      state.isLoading = false
    }
  })

  watch(
    () => containerStore.list,
    (newList) => {
      const data = newList
      if (data.length >= 0) {
        state.containers = newList
        state.isLoading = false
      }
    },
    { inmediate: true }
  )
})

const noServers = computed(() => state.containers.length === 0)
const notFound = computed(() => state.containers.detail === 'Not Found')
</script>

<template>
  <section class="max-h-full">
    <h1 class="text-2xl font-bold mb-2.5">Minecraft Servers</h1>

    <!-- Loader -->
    <div v-if="state.isLoading" class="text-center text-gray-500 py-6">
      <PulseLoader />
    </div>

    <span v-if="noServers && !state.isLoading">No Servers</span>
    <span v-if="notFound && !state.isLoading">Python Api Error: Fetch URL Not Found</span>
    <ul
      v-if="!noServers && !notFound && !state.isLoading"
      class="overflow-scroll overflow-x-hidden pr-1.5 [&::-webkit-scrollbar]:w-2 [&::-webkit-scrollbar-track]:rounded-full [&::-webkit-scrollbar-thumb]:rounded-full [&::-webkit-scrollbar-thumb]:bg-em-gray"
      style="height: calc(100% - 32px)"
    >
      <ServersListingCard
        v-for="container in state.containers"
        :key="container.id"
        :server="container"
      />
    </ul>
  </section>
</template>
