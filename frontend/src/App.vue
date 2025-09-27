<script setup>
import { RouterView } from 'vue-router'
import { provide, readonly, ref, onUnmounted } from 'vue'

const webSocketUpdate = ref(null)

const ws = new WebSocket('ws://localhost:8000/ws')

ws.onmessage = (event) => {
  webSocketUpdate.value = JSON.parse(event.data)
  console.log('Web Socket', webSocketUpdate.value)
}

onUnmounted(() => {
  ws.close()
})

provide('update', readonly(webSocketUpdate))
</script>

<template>
  <RouterView />
</template>
