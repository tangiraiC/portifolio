<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

import config from '../config'

const resumes = ref([])
const certifications = ref([])
const API_URL_RESUME = config.RESUME
const API_URL_CERTS = config.CERTIFICATIONS

onMounted(async () => {
    try {
        const [resResponse, certResponse] = await Promise.all([
            axios.get(API_URL_RESUME),
            axios.get(API_URL_CERTS)
        ])
        resumes.value = resResponse.data.results
        certifications.value = certResponse.data.results
    } catch (error) {
        console.error('Error fetching data:', error)
    }
})
    const forceDownload = async (url, filename) => {
        try {
            const response = await axios.get(url, { responseType: 'blob' })
            const blob = new Blob([response.data], { type: 'application/pdf' })
            const link = document.createElement('a')
            link.href = URL.createObjectURL(blob)
            link.download = filename || 'Lincoln_Chanakira_Resume.pdf'
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
  <div class="py-24 sm:py-32 bg-black/20">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
      
      <!-- Resume Section -->
      <div id="resume" class="mx-auto max-w-2xl text-center mb-16">
        <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl bg-clip-text text-transparent bg-gradient-to-r from-purple-400 to-pink-600">
          Resume
        </h2>
        <p class="mt-4 text-lg leading-8 text-gray-400">
          Professional experience and qualifications.
        </p>
        <div class="mt-8 flex justify-center">
             <div v-for="resume in resumes" :key="resume.id" class="m-2">
                <a :href="resume.pdf" @click.prevent="forceDownload(resume.pdf, `Lincoln_Chanakira_${resume.version || 'Resume'}.pdf`)" class="flex items-center gap-2 rounded-full bg-white/10 px-6 py-3 text-sm font-semibold text-white shadow-sm hover:bg-white/20 transition-all border border-white/10 cursor-pointer">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
                    Download {{ resume.version || 'Resume' }}
                </a>
             </div>
             <div v-if="resumes.length === 0" class="text-gray-400">Lincoln has not published anything yet</div>
        </div>
      </div>

      <!-- Certifications Section -->
      <div id="certifications" class="mx-auto max-w-7xl mt-24">
          <div class="mx-auto max-w-2xl text-center mb-12">
            <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl bg-clip-text text-transparent bg-gradient-to-r from-purple-400 to-pink-600">
                Certifications
            </h2>
          </div>
         <div class="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-3">
            <div v-for="cert in certifications" :key="cert.id" class="flex items-center gap-4 bg-cosmic-card p-4 rounded-xl border border-white/5 hover:border-cosmic-accent/30 transition-all">
                <div class="h-16 w-16 flex-shrink-0 bg-white/5 rounded-lg flex items-center justify-center overflow-hidden">
                    <img v-if="cert.image" :src="cert.image" :alt="cert.name" class="h-full w-full object-cover" />
                    <span v-else class="text-2xl">📜</span>
                </div>
                <div>
                    <h3 class="text-base font-semibold leading-7 tracking-tight text-white">{{ cert.name }}</h3>
                    <p class="text-sm font-semibold leading-6 text-cosmic-accent">{{ cert.issuing_organization }}</p>
                    <p class="text-xs text-gray-400">Issued: {{ cert.issue_date }}</p>
                </div>
            </div>
         </div>
      </div>

    </div>
  </div>
</template>
