<script setup>
import { onMounted, reactive } from 'vue'
import PulseLoader from 'vue-spinner/src/PulseLoader.vue'

const state = reactive({
  data: [],
  isLoading: true,
})

onMounted(async () => {
  try {
    const res = await fetch('/pythonapi/containers/simple?all=true')
    const data = await res.json()
    state.data = data
  } catch (error) {
    console.error('Error fetching simple container data: ', error)
  } finally {
    state.isLoading = false
  }
})
</script>
<template>
  <section>
    <h1 class="text-2xl font-bold mb-2.5">Simple Stats</h1>

    <!-- Loader -->
    <div v-if="state.isLoading" class="text-center text-gray-500 py-6">
      <PulseLoader />
    </div>

    <section class="max-w-sm p-4 border bd-em-gray-light rounded-lg bg-em-gray-darker mb-3">
      <section class="grid grid-cols-3 gap-4 text-center">
        <div><b>Active</b></div>
        <div><b>Exited</b></div>
        <div><b>Inactive</b></div>

        <div>
          <b class="text-2xl state-running" v-if="state.data.running">{{ state.data.running }}</b>
          <b class="text-2xl state-running" v-if="!state.data.running">0</b>
        </div>
        <div>
          <b class="text-2xl state-exited" v-if="state.data.exited">{{ state.data.exited }}</b>
          <b class="text-2xl state-exited" v-if="!state.data.exited">0</b>
        </div>
        <div>
          <b class="text-2xl state-paused" v-if="state.data.paused">{{ state.data.paused }}</b>
          <b class="text-2xl state-paused" v-if="!state.data.paused">0</b>
        </div>
      </section>
    </section>
  </section>
</template>
