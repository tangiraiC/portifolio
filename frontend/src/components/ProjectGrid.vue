<script setup>
import { ref, onMounted, computed } from 'vue'
import axios from 'axios'

const projects = ref([])
const loading = ref(true)
const selectedFilter = ref('All')

const filters = ['All', 'Web Development', 'Business and Data Analytics', 'AI and Machine Learning', 'Hackathons']

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api'

onMounted(async () => {
    try {
        const response = await axios.get(`${API_URL}/projects/`)
        projects.value = response.data.results || response.data
    } catch (error) {
        console.error('Error fetching projects:', error)
    } finally {
        loading.value = false
    }
})

const filteredProjects = computed(() => {
    if (selectedFilter.value === 'All') return projects.value
    
    // Simple frontend filtering based on category name
    // Assuming backend returns category_name in serializer
    return projects.value.filter(p => p.category_name === selectedFilter.value)
})
</script>

<template>
  <div id="projects" class="py-24 sm:py-32 scroll-mt-20">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
      <div class="mx-auto max-w-2xl text-center mb-16">
        <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl bg-clip-text text-transparent bg-gradient-to-r from-purple-400 to-pink-600">
          Selected Work
        </h2>
        <p class="mt-4 text-lg leading-8 text-gray-400">
          A showcase of my recent technical projects.
        </p>
      </div>

      <!-- Filter Tabs -->
      <div class="flex justify-center mt-8 gap-4 flex-wrap">
          <button 
            v-for="filter in filters" 
            :key="filter"
            @click="selectedFilter = filter"
            class="px-4 py-2 rounded-full text-sm font-medium transition-all"
            :class="selectedFilter === filter ? 'bg-white text-black' : 'bg-white/5 text-gray-400 hover:bg-white/10'"
          >
            {{ filter }}
          </button>
      </div>

      <div class="mx-auto mt-16 grid max-w-2xl grid-cols-1 gap-x-8 gap-y-20 lg:mx-0 lg:max-w-none lg:grid-cols-2">
        <article v-for="project in filteredProjects" :key="project.id" class="flex flex-col items-start justify-between bg-cosmic-card rounded-xl overflow-hidden border border-white/5 hover:border-cosmic-accent/30 transition-all duration-300">
          
          <!-- Image Container (16:9) -->
          <div class="relative w-full aspect-video bg-gray-800 overflow-hidden group">
             <!-- Check if cover_image exists -->
             <img v-if="project.cover_image" :src="project.cover_image" :alt="project.title" class="absolute inset-0 h-full w-full object-cover transition-transform duration-500 group-hover:scale-105" />
             <div v-else class="absolute inset-0 h-full w-full bg-gray-900 flex items-center justify-center text-gray-600 font-mono">
                 No Image
             </div>
             
             <!-- Badge Overlay -->
             <div class="absolute top-4 right-4 bg-green-500/90 text-black text-xs font-bold px-2 py-1 rounded uppercase tracking-wide" v-if="project.demo_url">
                 Live Deployment
             </div>
          </div>

          <div class="p-8 w-full">
            <h3 class="text-xl font-bold text-white group-hover:text-blue-400 transition-colors">
              {{ project.title }}
            </h3>
            
            <p class="mt-4 text-base leading-7 text-gray-400 line-clamp-3">
                {{ project.abstract }}
            </p>
            
            <div class="mt-6 flex flex-wrap gap-3">
              <span v-for="tag in (project.tech_stack_csv || '').split(',')" :key="tag" class="text-xs font-mono-code text-blue-300 bg-blue-900/30 px-3 py-1 rounded border border-blue-500/20">
                  {{ tag.trim() }}
              </span>
            </div>

            <div class="w-full h-px bg-white/10 my-6"></div>

            <div class="flex gap-4">
                <a v-if="project.repo_url" :href="project.repo_url" target="_blank" class="flex-1 text-center btn-secondary text-sm py-2 rounded bg-gray-700 hover:bg-gray-600 transition">
                   GitHub
                </a>
                <a v-if="project.demo_url" :href="project.demo_url" target="_blank" class="flex-1 text-center btn-primary text-sm py-2 rounded bg-primary-600 hover:bg-primary-500 transition text-white">
                   Try Live Demo
                </a>
            </div>
          </div>
        </article>
      </div>
        <div v-if="!loading && filteredProjects.length === 0" class="text-center text-gray-500 italic mt-10">No projects found for this category.</div>
        <div v-if="loading" class="text-center text-gray-400 mt-10 font-mono-code">Loading projects...</div>
    </div>
  </div>
</template>
