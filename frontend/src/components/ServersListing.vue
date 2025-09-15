<script setup>
import {ref, onMounted} from 'vue' 

const containers = ref([])

onMounted(async () => {
    try {
        const res = await fetch('/pythonapi/containers?all=true')
        const data = await res.json()
        containers.value = data
    } catch (error) {
        console.error("Error fetching containers: ", error)
    }
})
</script>

<template>
  <section>
    <h1>Docker Containers</h1>
    <ul>
      <li v-for="c in containers" :key="c.id">
        <strong>{{ c.name }}</strong>  
        <br> ID: {{ c.id.substring(0,12) }}  
        <br> Status: {{ c.status }}  
        <br> Image: {{ c.image[0] || "No tag" }}
        <hr>
      </li>
    </ul>
  </section>
</template>