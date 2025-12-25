<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'
import { marked } from 'marked' // We need to install this if not present, checking package.json next

const route = useRoute()
const post = ref(null)
const loading = ref(true)
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api'

// Simple markdown parser fallback if marked isn't installed
const parseMarkdown = (text) => {
    if (!text) return ''
    // Basic replacements for paragraphs and headers to allow readability
    // Ideally we use a library like 'marked'
    return text
        .replace(/^# (.*$)/gim, '<h1 class="text-3xl font-bold mb-4 text-white">$1</h1>')
        .replace(/^## (.*$)/gim, '<h2 class="text-2xl font-bold mb-3 mt-6 text-teal-400">$1</h2>')
        .replace(/^### (.*$)/gim, '<h3 class="text-xl font-bold mb-2 mt-4 text-white">$1</h3>')
        .replace(/\*\*(.*)\*\*/gim, '<b>$1</b>')
        .replace(/\n/gim, '<br />')
}

onMounted(async () => {
    try {
        // Fetch by slug through list filtering or direct endpoint if supported
        // MVP: Fetch list and find. Ideal: /api/blog/slug/
        const response = await axios.get(`${API_URL}/blog/?search=${route.params.slug}`)
        // DRF SearchFilter might match multiple, finding exact slug match
        if (response.data.results && response.data.results.length > 0) {
            post.value = response.data.results.find(p => p.slug === route.params.slug) || response.data.results[0]
        }
    } catch (error) {
        console.error('Error fetching post:', error)
    } finally {
        loading.value = false
    }
})
</script>

<template>
  <div class="py-24 sm:py-32 bg-cosmic-bg min-h-screen">
    <div class="mx-auto max-w-3xl px-6 lg:px-8">
      
      <div v-if="loading" class="text-center py-20 text-gray-400">Loading Article...</div>

      <article v-else-if="post" class="prose prose-invert prose-lg mx-auto">
        <div class="mb-10 text-center">
            <div class="flex items-center justify-center gap-4 text-sm text-gray-500 font-mono-code mb-4">
                 <time :datetime="post.published_at">
                    {{ new Date(post.published_at || post.created_at).toLocaleDateString(undefined, { year: 'numeric', month: 'long', day: 'numeric' }) }}
                 </time>
                 <span>•</span>
                 <span>{{ post.author || 'Lincoln' }}</span>
            </div>
            <h1 class="text-4xl font-bold tracking-tight text-white mb-6 leading-tight">
                {{ post.title }}
            </h1>
            <div class="flex justify-center gap-2">
                 <span v-for="tag in (post.tags_csv || '').split(',')" :key="tag" class="rounded-full bg-teal-400/10 px-3 py-1 text-sm font-medium text-teal-400 ring-1 ring-inset ring-teal-400/20 font-mono-code">
                    {{ tag.trim() }}
                 </span>
            </div>
        </div>

        <div v-if="post.hero_image" class="mb-10 rounded-2xl overflow-hidden shadow-2xl border border-white/10">
            <img :src="post.hero_image" :alt="post.title" class="w-full object-cover" />
        </div>

        <div class="text-gray-300 leading-relaxed space-y-6 bg-cosmic-card/30 p-8 rounded-2xl border border-white/5" v-html="parseMarkdown(post.body)"></div>
        
        <div class="mt-12 pt-8 border-t border-white/10 text-center">
             <router-link to="/blog" class="text-teal-400 hover:text-teal-300 font-semibold flex items-center justify-center gap-2">
                 ← Back to All Articles
             </router-link>
        </div>
      </article>

      <div v-else class="text-center py-20">
          <h1 class="text-4xl font-bold text-gray-700">404</h1>
          <p class="text-gray-500 mt-4">Article not found.</p>
          <router-link to="/blog" class="text-teal-400 mt-8 inline-block">Go Home</router-link>
      </div>
    </div>
  </div>
</template>
