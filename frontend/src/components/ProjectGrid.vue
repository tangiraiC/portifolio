<script setup>
import { ref, onMounted, computed } from 'vue'
import axios from 'axios'
import ProjectGalleryModal from './ProjectGalleryModal.vue'

const projects = ref([])
const loading = ref(true)
const selectedFilter = ref('All')

const filters = ['All', 'Web Development', 'Business & Data Analytics', 'AI & Machine Learning', 'Hackathons']

import config from '../config'

const API_URL = config.API_URL


const error = ref(null)

onMounted(async () => {
    try {
        // Debug logging
        console.log(`Attempting to fetch projects from: ${API_URL}/projects/`)
        
        const response = await axios.get(`${API_URL}/projects/`)
        projects.value = response.data.results || response.data
        
        if (projects.value.length === 0) {
            console.warn("API returned 0 projects.")
        }
    } catch (err) {
        console.error('Error fetching projects:', err)
        error.value = `Failed to load projects. URL: ${API_URL}/projects/. Error: ${err.message}`
        if (err.response) {
            error.value += ` (Status: ${err.response.status})`
        }
    } finally {
        loading.value = false
    }
})


const filteredProjects = computed(() => {
    if (selectedFilter.value === 'All') return projects.value
    
    // Simple frontend filtering based on category name
    // Assuming backend returns category_name in serializer
    // Assuming backend returns category_name in serializer
    return projects.value.filter(p => p.category_name === selectedFilter.value)
})

const selectedProject = ref(null)
const isModalOpen = ref(false)

const openProject = (project) => {
    selectedProject.value = project
    isModalOpen.value = true
}
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

      <div class="mx-auto mt-16 grid grid-cols-1 gap-x-8 gap-y-20 sm:grid-cols-2 lg:grid-cols-3">
        <article 
            v-for="project in filteredProjects" 
            :key="project.id" 
            @click="openProject(project)"
            class="flex flex-col items-start justify-between bg-cosmic-card rounded-xl overflow-hidden border border-white/5 hover:border-cosmic-accent/30 transition-all duration-300 cursor-pointer group hover:-translate-y-1 hover:shadow-2xl hover:shadow-purple-900/20"
        >
          
          <!-- Image Container (16:9) -->
          <div class="relative w-full aspect-video bg-gray-800 overflow-hidden">
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
                <button v-else disabled class="flex-1 text-center text-sm py-2 rounded bg-gray-800 text-gray-500 cursor-not-allowed border border-white/5">
                   No Live Demo
                </button>
            </div>
          </div>
        </article>
      </div>
    <div v-if="error" class="mx-auto max-w-2xl mt-8 p-4 bg-red-900/50 border border-red-500 rounded text-red-200 text-center">
        <p class="font-bold">System Error</p>
        <p class="text-sm font-mono mt-2">{{ error }}</p>
        <p class="text-xs mt-2">Please verify your VITE_API_URL setting.</p>
    </div>

    <div v-if="loading" class="text-center text-gray-400 mt-10 font-mono-code">
        Loading projects from {{ API_URL }}...
    </div>
    
    <div v-if="!loading && !error && filteredProjects.length === 0" class="text-center text-gray-500 italic mt-10">No projects found for this category ({{ selectedFilter }}).</div>
    </div>

    <!-- Gallery Modal -->
    <ProjectGalleryModal 
        v-if="selectedProject" 
        :project="selectedProject" 
        :isOpen="isModalOpen" 
        @close="isModalOpen = false" 
    />
  </div>
</template>
