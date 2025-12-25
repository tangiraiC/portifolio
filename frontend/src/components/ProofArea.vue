<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const certifications = ref([])
const loading = ref(true)
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api'

onMounted(async () => {
    try {
        const response = await axios.get(`${API_URL}/certifications/`)
        certifications.value = response.data.results || response.data
    } catch (error) {
        console.error('Error fetching certifications:', error)
    } finally {
        loading.value = false
    }
})
</script>

<template>
  <div id="proof-area" class="py-24 relative overflow-hidden">
    <!-- Background element -->
    <div class="absolute inset-0 bg-cosmic-bg pointer-events-none -z-10"></div>

    <div class="mx-auto max-w-7xl px-6 lg:px-8">
      <div class="mx-auto max-w-2xl text-center mb-16">
        <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl bg-clip-text text-transparent bg-gradient-to-r from-teal-400 to-blue-500">
          Certifications & Proof
        </h2>
        <p class="mt-4 text-lg leading-8 text-gray-400">
          Continuous learning and verified skills.
        </p>
      </div>

      <div class="mx-auto mt-16 grid max-w-2xl grid-cols-1 gap-x-8 gap-y-12 lg:mx-0 lg:max-w-none lg:grid-cols-3">
        <div v-for="cert in certifications" :key="cert.id" class="flex flex-col items-center text-center group">
           <div class="relative w-full aspect-[4/3] bg-gray-800 rounded-xl overflow-hidden mb-6 border border-white/5 hover:border-teal-500/30 transition-all">
               <img v-if="cert.image" :src="cert.image" :alt="cert.name" class="absolute inset-0 h-full w-full object-contain p-4 transition-transform duration-500 group-hover:scale-105" />
               <div v-else class="absolute inset-0 flex items-center justify-center text-gray-600 font-mono text-sm">No Image</div>
           </div>
           
           <h3 class="text-lg font-bold text-white group-hover:text-teal-400 transition-colors">
               <a v-if="cert.credential_url" :href="cert.credential_url" target="_blank">{{ cert.name }}</a>
               <span v-else>{{ cert.name }}</span>
           </h3>
           <p class="text-sm text-gray-400 mt-1">{{ cert.issuing_organization }}</p>
           <time class="text-xs text-gray-500 mt-2 font-mono-code">{{ new Date(cert.issue_date).getFullYear() }}</time>
        </div>
      </div>
      
      <div v-if="!loading && certifications.length === 0" class="text-center py-12 text-gray-500 italic">
          No certifications uploaded yet.
      </div>
    </div>
  </div>
</template>
