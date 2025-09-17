<script setup>
import { defineProps, reactive, onMounted } from 'vue'
import PulseLoader from 'vue-spinner/src/PulseLoader.vue'

const state = reactive({
  container: {},
  isLoading: true,
})

const props = defineProps({
  containerId: null,
})

onMounted(async () => {
  try {
    const response = await fetch(`/pythonapi/container/${props.containerId}`)
    const data = await response.json()
    state.container = data
  } catch (error) {
    console.error('Error fetching container details: ', error)
  } finally {
    state.isLoading = false
  }
})
</script>

<template>
  <section v-if="state.isLoading"><PulseLoader /></section>
  <section v-if="!state.isLoading" class="flex">
    <div>
      <h1 class="text-2xl font-bold">{{ state.container.name }}</h1>
      <i class="text-xs">{{ state.container.short_id }}</i>
    </div>
    <div>
      <section
        class="rounded-full px-4 py-0.5 ml-5"
        :class="{
          'bg-state-exited': state.container.status === 'exited',
          'bg-state-running': state.container.status === 'running',
          'bg-state-paused': state.container.status === 'paused',
        }"
      >
        {{ state.container.status }}
      </section>
    </div>
  </section>
</template>
