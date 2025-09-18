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

const isActiveBullet = (buttonState) => {
  if (state.isLoading) return false
  const containerStatus = state.container.status
  return containerStatus === buttonState
}
</script>

<template>
  <section v-if="state.isLoading"><PulseLoader /></section>
  <div v-if="!state.isLoading">
    <section class="flex">
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

    <section>
      <div class="h-10 max-w-lg bg-em-gray-darker border bd-em-gray-darker rounded-lg">
        <div class="grid h-full max-w-lg grid-cols-5 mx-auto">
          <button
            class="inline-flex flex-col items-center justify-center px-5 rounded-s-lg hover:bg-green-500"
            :class="[isActiveBullet('running') ? 'text-green-500 hover:text-white' : 'text-white']"
          >
            <a class="pi pi-play"></a>
          </button>
          <button
            class="inline-flex flex-col items-center justify-center px-5 hover:bg-em-gray-light"
            :class="[isActiveBullet('exited') ? 'text-red-500' : 'text-white']"
          >
            <a class="pi pi-stop"></a>
          </button>
          <button
            class="inline-flex flex-col items-center justify-center px-5 hover:bg-em-gray-light"
            :class="[isActiveBullet('paused') ? 'text-yellow-500' : 'text-white']"
          >
            <a class="pi pi-refresh"></a>
          </button>
          <button
            class="inline-flex flex-col items-center justify-center px-5 hover:bg-em-gray-light"
          >
            <a class="pi pi-pencil"></a>
          </button>
          <button
            class="inline-flex flex-col items-center justify-center px-5 rounded-e-lg bg-em-red hover:bg-em-red-dark"
          >
            <a class="pi pi-trash"></a>
          </button>
        </div>
      </div>
    </section>
  </div>
</template>
