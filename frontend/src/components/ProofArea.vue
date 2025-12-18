<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import config from '../config'
import BlogFeed from './BlogFeed.vue'

const certifications = ref([])
const API_URL_CERTS = config.CERTIFICATIONS

onMounted(async () => {
    try {
        const response = await axios.get(API_URL_CERTS)
        certifications.value = response.data.results
    } catch (error) {
        console.error('Error fetching certs:', error)
    }
})
</script>

<template>
  <div id="proof-area" class="py-24 bg-black/40">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
      
      <!-- Certifications Section -->
      <div class="mb-24">
         <div class="mx-auto max-w-2xl text-center mb-16">
            <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl bg-clip-text text-transparent bg-gradient-to-r from-purple-400 to-pink-600">
                Certifications & Education
            </h2>
             <p class="mt-4 text-lg leading-8 text-gray-400">
                Continuous learning and academic foundation.
            </p>
         </div>
         <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div v-for="cert in certifications" :key="cert.id" class="flex items-center gap-6 bg-white/5 p-6 rounded-lg border border-white/5 hover:border-white/20 transition-all">
                <div class="h-16 w-16 flex-shrink-0 bg-white rounded flex items-center justify-center p-2">
                    <img v-if="cert.image" :src="cert.image" :alt="cert.name" class="h-full w-full object-contain" />
                    <span v-else class="text-2xl text-black">🎓</span>
                </div>
                <div>
                    <h3 class="text-lg font-bold text-white leading-tight">{{ cert.name }}</h3>
                    <p class="text-sm text-gray-400 mt-1">{{ cert.issuing_organization }}</p>
                    <a v-if="cert.credential_url" :href="cert.credential_url" target="_blank" class="text-xs text-blue-400 mt-2 block hover:underline">Verify Credential ></a>
                </div>
            </div>
            <!-- Empty state filler -->
             <div v-if="certifications.length === 0" class="text-gray-500 italic p-4">Lincoln has not published anything yet</div>
         </div>
      </div>

      <!-- Blog / Writing Section -->
      <div id="blog-list" class="mx-auto max-w-2xl text-center mb-16">
          <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl bg-clip-text text-transparent bg-gradient-to-r from-purple-400 to-pink-600">
            Blog
          </h2>
           <p class="mt-4 text-lg leading-8 text-gray-400">
            Thoughts, tutorials, and insights.
          </p>
      </div>
      <div>
          <BlogFeed />
      </div>

    </div>
  </div>
</template>
