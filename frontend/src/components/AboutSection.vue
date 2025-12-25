<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const aboutText = ref('')
const loading = ref(true)
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api'

onMounted(async () => {
    try {
        const response = await axios.get(`${API_URL}/site-settings/`)
        // SiteSettings might return a list or single object depending on viewset
        const settings = Array.isArray(response.data.results) ? response.data.results[0] : response.data[0]
        
        if (settings) {
            aboutText.value = settings.about_me
        }
    } catch (error) {
        console.error('Error fetching site settings:', error)
    } finally {
        loading.value = false
    }
})
</script>

<template>
  <div id="about" class="py-24 bg-black/20">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
      <div class="mx-auto max-w-2xl lg:max-w-none">
        <div class="mx-auto max-w-2xl text-center mb-16">
            <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl bg-clip-text text-transparent bg-gradient-to-r from-purple-400 to-pink-600">
                About Me
            </h2>
        </div>
        
        <div class="font-sans text-lg text-gray-400 leading-relaxed max-w-3xl mx-auto whitespace-pre-line">
           <div v-if="loading" class="text-center">Loading...</div>
           <div v-else-if="aboutText">{{ aboutText }}</div>
           <div v-else>
               <!-- Fallback static content if no API data -->
               <p>
                   I’m <span class="text-white font-bold">Lincoln T Chanakira</span>, a passionate Full Stack Developer and Data Scientist...
                   (Please update your bio in the Admin Dashboard)
               </p>
           </div>
        </div>
      </div>
    </div>
  </div>
</template>
