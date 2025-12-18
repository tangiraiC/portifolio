<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import config from '../config'

const posts = ref([])
const loading = ref(true)
const API_URL = config.BLOG

onMounted(async () => {
    try {
        const response = await axios.get(API_URL)
        posts.value = response.data.results
    } catch (error) {
        console.error('Error fetching blog posts:', error)
    } finally {
        loading.value = false
    }
})
</script>

<template>
  <div class="space-y-4">
    <div v-for="post in posts" :key="post.id" class="group flex flex-col sm:flex-row sm:items-baseline sm:gap-8 hover:bg-white/5 p-4 rounded-lg transition-colors border-b border-white/5 last:border-0 border-l border-transparent hover:border-l-purple-500">
      
      <div class="sm:w-32 flex-shrink-0 mb-2 sm:mb-0">
         <time :dateTime="post.published_at" class="font-mono-code text-sm text-gray-500">{{ new Date(post.published_at).toLocaleDateString(undefined, { month: 'short', day: 'numeric' }) }}</time>
      </div>
      
      <div class="flex-1">
          <h3 class="text-xl font-semibold text-white group-hover:text-purple-400 transition-colors">
              <a :href="`#blog-${post.id}`">{{ post.title }}</a>
          </h3>
      </div>

      <div class="hidden sm:block">
          <span v-for="tag in post.tags_csv.split(',').slice(0,1)" :key="tag" class="text-xs font-mono-code text-gray-400 border border-gray-700 px-2 py-1 rounded">
              {{ tag.trim() }}
          </span>
      </div>
    </div>
    
    <div v-if="loading" class="text-gray-500">Loading articles...</div>
    <div v-if="!loading && posts.length === 0" class="text-gray-500 italic">Lincoln has not published anything yet</div>
  </div>
</template>
