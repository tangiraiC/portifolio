<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import config from '../config'

const papers = ref([])
const loading = ref(true)
const API_URL = config.PUBLICATIONS

onMounted(async () => {
    try {
        const response = await axios.get(API_URL)
        papers.value = response.data.results
    } catch (error) {
        console.error('Error fetching research papers:', error)
    } finally {
        loading.value = false
    }
})
</script>

<template>
  <section id="publications" class="py-24 relative overflow-hidden">
    <!-- Background elements -->
    <div class="absolute top-0 right-0 w-[500px] h-[500px] bg-purple-900/10 rounded-full blur-[100px] -z-10"></div>

    <div class="mx-auto max-w-7xl px-6 lg:px-8">
      <div class="mx-auto max-w-2xl text-center mb-16">
        <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl bg-clip-text text-transparent bg-gradient-to-r from-purple-400 to-pink-600">
          Technical Writing & Publications
        </h2>
        <p class="mt-4 text-lg leading-8 text-gray-400">
          Research papers and technical publications.
        </p>
      </div>

      <div class="space-y-6">
        <div v-for="paper in papers" :key="paper.id" 
             class="group relative bg-cosmic-card/50 backdrop-blur-sm border border-white/5 rounded-xl p-8 hover:bg-white/5 hover:border-purple-500/30 transition-all duration-300">
          
          <div class="flex flex-col md:flex-row gap-6 justify-between items-start">
            <div class="flex-1">
              <div class="flex items-center gap-3 mb-3">
                <span class="inline-flex items-center rounded-md bg-purple-400/10 px-2 py-1 text-xs font-medium text-purple-400 ring-1 ring-inset ring-purple-400/20">
                    Publication
                </span>
                <time :datetime="paper.published_at" class="text-sm text-gray-500 font-mono-code">
                    {{ new Date(paper.published_at).toLocaleDateString(undefined, { year: 'numeric', month: 'long' }) }}
                </time>
              </div>
              
              <h3 class="text-xl font-bold text-white group-hover:text-purple-300 transition-colors mb-3">
                {{ paper.title }}
              </h3>
              
              <p class="text-gray-400 text-sm italic mb-4 border-l-2 border-purple-500/30 pl-4">
                {{ paper.citation }}
              </p>
              
              <p class="text-gray-300 leading-relaxed mb-6">
                {{ paper.abstract }}
              </p>
            </div>

            <div class="flex flex-col gap-3 min-w-[140px]">
              <a v-if="paper.pdf" :href="paper.pdf" target="_blank" 
                 class="flex items-center justify-center gap-2 rounded-lg bg-white/5 px-4 py-2.5 text-sm font-semibold text-white shadow-sm ring-1 ring-inset ring-white/10 hover:bg-white/10 transition-all">
                <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                </svg>
                PDF
              </a>
              <a v-if="paper.link" :href="paper.link" target="_blank"
                 class="flex items-center justify-center gap-2 rounded-lg bg-purple-600 px-4 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-purple-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-purple-600 transition-all">
                 <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                </svg>
                Read Online
              </a>
            </div>
          </div>
        </div>
        
        <div v-if="!loading && papers.length === 0" class="text-center py-12">
            <p class="text-gray-500 italic">Lincoln has not published anything yet</p>
        </div>
      </div>
    </div>
  </section>
</template>
