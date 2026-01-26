<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import NavBar from '../components/NavBar.vue'

import config from '../config'

const resumeUrl = ref(null)
const loading = ref(true)
const error = ref(null)
const API_URL = config.API_URL


onMounted(async () => {
    loading.value = true
    try {
        // 1. Try to fetch from Resume model (prioritize primary)
        try {
            const resumeRes = await axios.get(`${API_URL}/resume/?ordering=-is_primary`)
            if (resumeRes.data.results && resumeRes.data.results.length > 0) {
                resumeUrl.value = resumeRes.data.results[0].pdf
                loading.value = false
                return
            }
        } catch (e) {
            console.warn("Could not fetch from Resume model", e)
        }

        // 2. Fallback to SiteSettings
        try {
            const settingsRes = await axios.get(`${API_URL}/site-settings/`)
            const settings = Array.isArray(settingsRes.data.results) ? settingsRes.data.results[0] : settingsRes.data[0]
            if (settings) {
                resumeUrl.value = settings.resume_file || settings.resume_link
            }
        } catch (e) {
             console.warn("Could not fetch from Site Settings", e)
        }

        if (!resumeUrl.value) {
            error.value = "No resume found. Please upload one in the admin panel."
        }

    } catch (err) {
        error.value = "Failed to load resume connection."
        console.error(err)
    } finally {
        loading.value = false
    }
})
    const forceDownload = async (url) => {
        try {
            const response = await axios.get(url, { responseType: 'blob' })
            const blob = new Blob([response.data], { type: 'application/pdf' })
            const link = document.createElement('a')
            link.href = URL.createObjectURL(blob)
            link.download = 'Lincoln_Chanakira_Resume.pdf'
            document.body.appendChild(link)
            link.click()
            document.body.removeChild(link)
            URL.revokeObjectURL(link.href)
        } catch (e) {
            console.error("Download failed", e)
            window.open(url, '_blank')
        }
    }
</script>

<template>
    <div class="min-h-screen bg-cosmic-bg text-white">
        <NavBar />
        
        <div class="pt-24 px-6 max-w-7xl mx-auto h-[calc(100vh-100px)] flex flex-col">
            <div class="flex justify-between items-center mb-6">
                <h1 class="text-3xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-purple-600">
                    My Resume
                </h1>
                <a v-if="resumeUrl" :href="resumeUrl" @click.prevent="forceDownload(resumeUrl)" class="btn-primary flex items-center gap-2 cursor-pointer">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M3 16.5v2.25A2.25 2.25 0 0 0 5.25 21h13.5A2.25 2.25 0 0 0 21 18.75V16.5M16.5 12 12 16.5m0 0L7.5 12m4.5 4.5V3" />
                    </svg>
                    Download PDF
                </a>
            </div>

            <div v-if="loading" class="flex-1 flex items-center justify-center">
                <div class="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500"></div>
            </div>

            <div v-else-if="error" class="flex-1 flex items-center justify-center flex-col text-center">
                 <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-16 h-16 text-gray-500 mb-4">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 0 0-3.375-3.375h-1.5A1.125 1.125 0 0 1 13.5 7.125v-1.5a3.375 3.375 0 0 0-3.375-3.375H8.25m2.25 0H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 0 0-9-9Z" />
                </svg>
                <p class="text-xl text-gray-400">{{ error }}</p>
                <router-link to="/#contact" class="mt-4 text-blue-400 hover:text-blue-300">Contact me directly &rarr;</router-link>
            </div>

            <div v-else class="flex-1 bg-white/5 rounded-xl border border-white/10 overflow-hidden shadow-2xl">
                <iframe :src="resumeUrl" class="w-full h-full" type="application/pdf">
                    <p class="p-8 text-center">
                        It appears your browser doesn't support PDF viewing. 
                        <a :href="resumeUrl" class="text-blue-400 underline">Download the resume here</a>.
                    </p>
                </iframe>
            </div>
            
            <div class="h-8"></div> <!-- Spacer -->
        </div>
    </div>
</template>
