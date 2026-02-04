<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import NavBar from '../components/NavBar.vue'

const posts = ref([])
const loading = ref(true)
import config from '../config'
const API_URL = config.API_URL

onMounted(async () => {
    try {
        const response = await axios.get(`${API_URL}/blog/`)
        posts.value = response.data.results || response.data
    } catch (error) {
        console.error('Error fetching blog posts:', error)
    } finally {
        loading.value = false
    }
})
</script>

<template>
  <div class="py-24 sm:py-32 bg-cosmic-bg min-h-screen">
    <NavBar />
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
      <div class="mx-auto max-w-2xl text-center mb-16">
        <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl bg-clip-text text-transparent bg-gradient-to-r from-teal-400 to-blue-500">
          Cosmic Insights
        </h2>
        <p class="mt-4 text-lg leading-8 text-gray-400">
          Thoughts on technology, analytics, and building the future.
        </p>
      </div>

      <div class="mx-auto mt-16 grid max-w-2xl grid-cols-1 gap-x-8 gap-y-20 lg:mx-0 lg:max-w-none lg:grid-cols-3">
        <article 
            v-for="post in posts" 
            :key="post.id" 
            class="flex flex-col items-start justify-between bg-cosmic-card/50 rounded-2xl overflow-hidden border border-white/5 hover:border-teal-500/30 transition-all duration-300 group"
        >
          <div class="relative w-full aspect-[16/9] overflow-hidden bg-gray-900">
            <img 
                v-if="post.hero_image" 
                :src="post.hero_image" 
                :alt="post.title" 
                class="absolute inset-0 h-full w-full object-cover transition-transform duration-500 group-hover:scale-110" 
            />
            <div 
                v-else 
                class="absolute inset-0 h-full w-full flex items-center justify-center bg-gray-800 text-gray-600 font-mono"
            >
                No Image
            </div>
          </div>
          
          <div class="p-8 w-full flex-1 flex flex-col">
            <div class="flex items-center gap-x-4 text-xs">
              <time :datetime="post.published_at" class="text-gray-500 font-mono-code">
                 {{ new Date(post.published_at || post.created_at).toLocaleDateString(undefined, { year: 'numeric', month: 'short', day: 'numeric' }) }}
              </time>
              <span v-for="tag in (post.tags_csv || '').split(',').slice(0, 2)" :key="tag" class="relative z-10 rounded-full bg-teal-400/10 px-3 py-1.5 font-medium text-teal-400 font-mono-code hover:bg-teal-400/20">
                  {{ tag.trim() }}
              </span>
            </div>
            
            <div class="group relative mt-4 flex-1">
              <h3 class="text-lg font-semibold leading-6 text-white group-hover:text-teal-300 transition-colors">
                <router-link :to="`/blog/${post.slug}`">
                  <span class="absolute inset-0"></span>
                  {{ post.title }}
                </router-link>
              </h3>
              <p class="mt-5 line-clamp-3 text-sm leading-6 text-gray-400">
                  {{ post.body ? post.body.substring(0, 150) + '...' : '' }}
              </p>
            </div>
            
            <div class="mt-8 flex items-center justify-between gap-x-4">
               <div class="text-sm leading-6">
                 <p class="font-semibold text-white">
                   {{ post.author || 'Lincoln' }}
                 </p>
               </div>
               
               <router-link :to="`/blog/${post.slug}`" class="relative z-10 rounded-full bg-white/10 px-4 py-2 text-sm font-semibold text-white shadow-sm hover:bg-white/20 transition-colors">
                   Read Article
               </router-link>
             </div>
          </div>
        </article>
      </div>

      <div v-if="!loading && posts.length === 0" class="text-center py-20">
          <p class="text-gray-500 italic text-xl">No posts published correctly... yet.</p>
          <p class="text-gray-600 mt-2">Check back soon for updates!</p>
      </div>
    </div>
  </div>
</template>
