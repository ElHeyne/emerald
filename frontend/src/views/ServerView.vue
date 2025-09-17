<script setup>
import { onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'

import ServerInfo from '../components/ServerInfo.vue'

const route = useRoute()
let serverId = route.params.serverId

const fetchServer = async (id) => {
  // Fetch server data based on the id
}

onMounted(() => {
  fetchServer(serverId)
})

watch(
  () => route.params.serverId,
  (newId) => {
    serverId = newId
    fetchServer(newId)
  },
)
</script>

<template>
  <section>
    <ServerInfo :containerId="route.params.serverId" />
  </section>
</template>
