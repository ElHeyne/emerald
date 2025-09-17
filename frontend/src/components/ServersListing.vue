<script setup>
import { onMounted, computed, reactive } from 'vue'
import PulseLoader from 'vue-spinner/src/PulseLoader.vue'

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
      <span v-if="noServers && isLoading">No Servers</span>
      <li v-for="c in state.containers" :key="c.id">
        <RouterLink to="/servers">
          <section
            class="max-w-sm p-4 border bd-em-gray-light hover:bg-em-gray-light rounded-lg bg-em-gray-darker mb-3 duration-300 ease-in-out"
          >
            <div class="flex items-center">
              <i
                class="pi pi-circle-fill mr-2.5"
                :class="{
                  'state-exited': c.status === 'exited',
                  'state-running': c.status === 'running',
                  'state-paused': c.status === 'paused',
                }"
              ></i>
              <span class="overflow-hidden"> {{ c.name }} </span>
            </div>
          </section>
        </RouterLink>
      </li>
    </ul>
  </section>
</template>
