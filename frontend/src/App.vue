<script setup>
import { RouterView } from 'vue-router'
import { onUnmounted, onMounted } from 'vue'
import { useContainerStore } from '@/stores/containerStore'

const containerStore = useContainerStore()
const ws = new WebSocket(URL='ws://localhost:8000/ws')

onMounted(async() => {
  const response = await fetch(`/pythonapi/containers`)
    const data = await response.json()
    const containers = data
    containerStore.setContainers(containers)
})

ws.onmessage = (event) => {
  if (event.status === "error"){
    console.log("I got an error!") /**TODO MANAGE ERRORS */
  } else {
    const msg = JSON.parse(event.data)
    console.log("DEBUB: ", msg) /**TODO KEEP ERROR MSG? */

    containerStore.updateContainerStatus(msg.id, msg.status)
  }
}

onUnmounted(() => {
  ws.close()
})
</script>

<template>
  <RouterView />
</template>
