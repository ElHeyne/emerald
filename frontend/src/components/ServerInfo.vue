<script setup>
import { defineProps, reactive, onMounted, inject, watch } from 'vue'
import PulseLoader from 'vue-spinner/src/PulseLoader.vue'
import { useContainerStore } from '@/stores/containerStore'

const containerStore = useContainerStore()

const state = reactive({
  container: {},
  isLoading: true,
})

const props = defineProps({
  containerId: null,
})

onMounted(async () => {
  const idFound = containerStore.list.findIndex(c => c.id === props.containerId)
  if (idFound >= 0) {
    state.container = containerStore.list[idFound]
    state.isLoading = false
  }
})

watch(
  () => containerStore.list,
  (newList) => {
    const idFound = newList.findIndex(c => c.id === props.containerId)
    if (idFound >= 0) {
      state.container = newList[idFound]
      state.isLoading = false
    }
  },
  { inmediate: true }
)

const isActiveBullet = (buttonState) => {
  if (state.isLoading) return false
  const containerStatus = state.container.status
  return containerStatus === buttonState
}

const startServer = async () => {
  try {
    const idFound = containerStore.list.findIndex(c => c.id === props.containerId)
    if (idFound >= 0) {
      containerStore.list[idFound].status = "starting"
    }
    const response = await fetch(`/pythonapi/container/${props.containerId}/start`, {
      method: 'POST',
    })
    const data = await response.json()
    console.log("DEBUG: ", data)
  } catch (error) {
    console.error('Error starting server: ', error)
  }
}

const stopServer = async () => {
  try {
    const idFound = containerStore.list.findIndex(c => c.id === props.containerId)
    if (idFound >= 0) {
      containerStore.list[idFound].status = "exiting"
    }
    const response = await fetch(`/pythonapi/container/${props.containerId}/stop`, {
      method: 'POST',
    })
    const data = await response.json()
    console.log("DEBUG: ", data)
  } catch (errir) {
    console.error('Error stopping server: ', error)
  }
}

const restartServer = async () => {
  try {
    const idFound = containerStore.list.findIndex(c => c.id === props.containerId)
    if (idFound >= 0) {
      containerStore.list[idFound].status = "exiting"
    }
    const response = await fetch(`/pythonapi/container/${props.containerId}/restart`, {
      method: 'POST',
    })
    const data = await response.json()
    console.log("DEBUG: ", data)
  } catch (error) {
    console.error('Error restarting server: ', error)
  }
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
            'bg-state-exiting': state.container.status === 'exiting',
            'bg-state-starting': state.container.status === 'starting',
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
            @click="startServer"
            class="inline-flex flex-col items-center justify-center px-5 rounded-s-lg"
            :class="[
              isActiveBullet('starting') ? '!text-gray-700' : '', 
              isActiveBullet('exiting') ? '!text-gray-700' : '', 
              isActiveBullet('running') ? 'text-green-500' : '', 
              isActiveBullet('running') || isActiveBullet('starting') || isActiveBullet('exiting')
                ? ''
                : 'text-white hover:bg-green-500']"
          >
            <a class="pi pi-play"></a>
          </button>
          <button
            @click="stopServer"
            class="inline-flex flex-col items-center justify-center px-5"
            :class="[
              isActiveBullet('starting') ? '!text-gray-700' : '', 
              isActiveBullet('exiting') ? '!text-gray-700' : '', 
              isActiveBullet('exited') ? 'text-red-500' : '', 
              isActiveBullet('exited') || isActiveBullet('starting') || isActiveBullet('exiting')
                ? ''
                : 'text-white hover:bg-em-gray-light']"
          >
            <a class="pi pi-stop"></a>
          </button>
          <button
            @click="restartServer"
            class="inline-flex flex-col items-center justify-center px-5"
            :class="[
              isActiveBullet('starting') ? '!text-gray-700' : '', 
              isActiveBullet('exiting') ? '!text-gray-700' : '', 
              isActiveBullet('paused') ? 'text-yellow-500' : '',
              isActiveBullet('starting') || isActiveBullet('exiting')
                ? ''
                : 'text-white hover:bg-em-gray-light']"
          >
            <a class="pi pi-refresh"></a>
          </button>
          <button
            class="inline-flex flex-col items-center justify-center px-5"
            :class="[
              isActiveBullet('starting') ? '!text-gray-700' : '', 
              isActiveBullet('exiting') ? '!text-gray-700' : '',
              isActiveBullet('starting') || isActiveBullet('exiting')
                ? ''
                : 'text-white hover:bg-em-gray-light']"
          >
            <a class="pi pi-pencil"></a>
          </button>
          <button
            class="inline-flex flex-col items-center justify-center px-5 rounded-e-lg"
            :class="[
              isActiveBullet('starting') ? '!text-gray-700' : '', 
              isActiveBullet('exiting') ? '!text-gray-700' : '', 
              isActiveBullet('starting') || isActiveBullet('exiting')
                ? ''
                : 'bg-em-red hover:bg-em-red-dark']"
          >
            <a class="pi pi-trash"></a>
          </button>
        </div>
      </div>
    </section>
  </div>
</template>
