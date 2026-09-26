<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import config from '../config'

const posts = ref([])
const loading = ref(true)
const errorMessage = ref('')
const API_URL = config.BLOG

const loadPosts = async () => {
    loading.value = true
    errorMessage.value = ''
    try {
        const response = await axios.get(API_URL)
        posts.value = response.data.results || response.data
    } catch (error) {
        errorMessage.value = 'Unable to load articles. Please try again.'
        console.error('Error fetching blog posts:', error)
    } finally {
        loading.value = false
    }
}

onMounted(loadPosts)
</script>

<template>
  <div class="space-y-4">
    <div v-for="post in posts" :key="post.id" class="group flex flex-col sm:flex-row sm:items-baseline sm:gap-8 hover:bg-white/5 p-4 rounded-lg transition-colors border-b border-white/5 last:border-0 border-l border-transparent hover:border-l-purple-500">
      
      <div class="sm:w-32 flex-shrink-0 mb-2 sm:mb-0">
         <time :dateTime="(post.published_at || post.created_at)" class="font-mono-code text-sm text-gray-500">{{ new Date(post.published_at || post.created_at).toLocaleDateString(undefined, { month: 'short', day: 'numeric' }) }}</time>
      </div>
      
      <div class="flex-1">
          <h3 class="text-xl font-semibold text-white group-hover:text-purple-400 transition-colors">
              <router-link :to="`/blog/${post.slug}`">{{ post.title }}</router-link>
          </h3>
      </div>

      <div class="hidden sm:block">
          <span v-for="tag in (post.tags_csv || '').split(',').filter(tag => tag.trim()).slice(0,1)" :key="tag" class="text-xs font-mono-code text-gray-400 border border-gray-700 px-2 py-1 rounded">
              {{ tag.trim() }}
          </span>
      </div>
    </div>
    
    <div v-if="loading" class="text-gray-500">Loading articles...</div>
    <div v-else-if="errorMessage" role="alert" class="text-gray-500">
      <p>{{ errorMessage }}</p>
      <button type="button" @click="loadPosts" class="mt-2 underline">Try again</button>
    </div>
    <div v-else-if="posts.length === 0" class="text-gray-500 italic">Lincoln has not published anything yet</div>
  </div>
</template>
