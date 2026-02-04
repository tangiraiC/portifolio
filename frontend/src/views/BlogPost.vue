<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'
import NavBar from '../components/NavBar.vue'
import config from '../config'

const route = useRoute()
const post = ref(null)
const loading = ref(true)
const newComment = ref('')
const submittingComment = ref(false)
const API_URL = config.API_URL

// Authentication state
const token = localStorage.getItem('token')
const isAuthenticated = !!token

const parseMarkdown = (text) => {
    if (!text) return ''
    return text
        .replace(/^# (.*$)/gim, '<h1 class="text-3xl font-bold mb-4 text-white">$1</h1>')
        .replace(/^## (.*$)/gim, '<h2 class="text-2xl font-bold mb-3 mt-6 text-teal-400">$1</h2>')
        .replace(/^### (.*$)/gim, '<h3 class="text-xl font-bold mb-2 mt-4 text-white">$1</h3>')
        .replace(/\*\*(.*)\*\*/gim, '<b>$1</b>')
        .replace(/\n/gim, '<br />')
}

const fetchPost = async () => {
    try {
        const headers = token ? { Authorization: `Token ${token}` } : {}
        const response = await axios.get(`${API_URL}/blog/?search=${route.params.slug}`, { headers })
        
        if (response.data.results && response.data.results.length > 0) {
            // Find exact match
            post.value = response.data.results.find(p => p.slug === route.params.slug) || response.data.results[0]
        }
    } catch (error) {
        console.error('Error fetching post:', error)
    } finally {
        loading.value = false
    }
}

const handleLike = async () => {
    if (!isAuthenticated) {
        alert("Please login to like posts.")
        return
    }
    try {
        const response = await axios.post(`${API_URL}/blog/${post.value.id}/like/`, {}, {
            headers: { Authorization: `Token ${token}` }
        })
        if (response.data.status === 'liked') {
            post.value.is_liked = true
            post.value.likes_count++
        } else {
            post.value.is_liked = false
            post.value.likes_count--
        }
    } catch (error) {
        console.error("Error liking post:", error)
    }
}

const submitComment = async () => {
    if (!newComment.value.trim()) return
    submittingComment.value = true
    try {
        const response = await axios.post(`${API_URL}/blog/${post.value.id}/comment/`, {
            content: newComment.value
        }, {
            headers: { Authorization: `Token ${token}` }
        })
        // Add new comment to list (optimistic or from response)
        if (!post.value.comments) post.value.comments = []
        post.value.comments.push(response.data)
        newComment.value = ''
    } catch (error) {
        console.error("Error commenting:", error)
        alert("Failed to post comment.")
    } finally {
        submittingComment.value = false
    }
}

const shareLinkedIn = () => {
    const url = encodeURIComponent(window.location.href)
    window.open(`https://www.linkedin.com/sharing/share-offsite/?url=${url}`, '_blank')
}

const shareFacebook = () => {
    const url = encodeURIComponent(window.location.href)
    window.open(`https://www.facebook.com/sharer/sharer.php?u=${url}`, '_blank')
}

onMounted(fetchPost)
</script>

<template>
  <div class="py-24 sm:py-32 bg-cosmic-bg min-h-screen">
    <NavBar />
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

        <!-- Interactions Section -->
        <div class="mt-12 pt-8 border-t border-white/10">
            <div class="flex flex-wrap items-center justify-between gap-6 mb-8">
                <!-- Share Buttons -->
                <div class="flex items-center gap-4">
                    <span class="text-gray-400 text-sm font-semibold uppercase tracking-wider">Share:</span>
                    <button @click="shareLinkedIn" class="px-4 py-2 bg-[#0077b5] hover:bg-[#006396] text-white rounded-md text-sm font-medium transition-colors flex items-center gap-2">
                        LinkedIn
                    </button>
                    <button @click="shareFacebook" class="px-4 py-2 bg-[#1877f2] hover:bg-[#166fe5] text-white rounded-md text-sm font-medium transition-colors flex items-center gap-2">
                        Facebook
                    </button>
                </div>

                <!-- Like Button -->
                <button 
                    @click="handleLike" 
                    class="flex items-center gap-2 px-4 py-2 rounded-full border transition-all duration-300"
                    :class="post.is_liked ? 'bg-red-500/10 border-red-500 text-red-500 hover:bg-red-500/20' : 'bg-white/5 border-white/10 text-gray-400 hover:border-red-500/50 hover:text-red-400'"
                >
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-5 h-5" :class="post.is_liked ? 'animate-pulse' : ''">
                        <path d="M11.645 20.91l-.007-.003-.022-.012a15.247 15.247 0 01-.383-.218 25.18 25.18 0 01-4.244-3.17C4.688 15.36 2.25 12.174 2.25 8.25 2.25 5.322 4.714 3 7.688 3A5.5 5.5 0 0112 5.052 5.5 5.5 0 0116.313 3c2.973 0 5.437 2.322 5.437 5.25 0 3.925-2.438 7.111-4.739 9.256a25.175 25.175 0 01-4.244 3.17 15.247 15.247 0 01-.383.219l-.022.012-.007.004-.003.001a.752.752 0 01-.704 0l-.003-.001z" />
                    </svg>
                    <span class="font-mono-code">{{ post.likes_count || 0 }} Likes</span>
                </button>
            </div>

            <!-- Comments Section -->
            <div class="bg-gray-900/50 rounded-xl p-6 border border-white/5">
                <h3 class="text-xl font-bold text-white mb-6">Comments ({{ post.comments ? post.comments.length : 0 }})</h3>
                
                <!-- Comment List -->
                <div class="space-y-6 mb-8">
                    <div v-for="comment in post.comments" :key="comment.id" class="flex gap-4 p-4 rounded-lg bg-gray-800/50">
                        <div class="flex-1">
                            <div class="flex items-center justify-between mb-2">
                                <span class="font-bold text-teal-400">{{ comment.author_name }}</span>
                                <span class="text-xs text-gray-500 font-mono-code">{{ new Date(comment.created_at).toLocaleDateString() }}</span>
                            </div>
                            <p class="text-gray-300">{{ comment.content }}</p>
                        </div>
                    </div>
                     <div v-if="(!post.comments || post.comments.length === 0)" class="text-gray-500 italic text-sm">
                        No comments yet. Be the first to share your thoughts!
                    </div>
                </div>

                <!-- Comment Form -->
                <div v-if="isAuthenticated">
                    <textarea 
                        v-model="newComment" 
                        class="w-full bg-gray-900 border border-gray-700 rounded-lg p-3 text-white focus:border-teal-500 focus:ring-1 focus:ring-teal-500 outline-none transition"
                        rows="3"
                        placeholder="Add a comment..."
                    ></textarea>
                    <div class="flex justify-end mt-2">
                        <button 
                            @click="submitComment" 
                            :disabled="submittingComment || !newComment.trim()"
                            class="px-4 py-2 bg-teal-600 hover:bg-teal-500 text-white rounded-md text-sm font-semibold disabled:opacity-50 disabled:cursor-not-allowed transition"
                        >
                            {{ submittingComment ? 'Posting...' : 'Post Comment' }}
                        </button>
                    </div>
                </div>
                <div v-else class="text-center p-4 bg-gray-800/50 rounded-lg border border-gray-700">
                    <p class="text-gray-400 mb-2">Please log in to join the discussion.</p>
                    <router-link to="/login" class="text-teal-400 hover:text-teal-300 font-semibold text-sm">Login here</router-link>
                </div>
            </div>
        </div>
        
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
