<script setup>
import { ref } from 'vue'
import axios from 'axios'

const form = ref({
  name: '',
  email: '',
  subject: '',
  message: ''
})

const loading = ref(false)
const success = ref(false)
const error = ref(null)

import config from '../config'



const API_URL = config.CONTACT

const submitForm = async () => {
    loading.value = true
    error.value = null
    success.value = false
    
    try {
        await axios.post(API_URL, form.value)
        success.value = true
        form.value = { name: '', email: '', subject: '', message: '' }
    } catch (err) {
        console.error(err)
        error.value = 'Failed to send message. Please try again later.'
    } finally {
        loading.value = false
    }
}
</script>

<template>
  <div id="contact" class="py-24 bg-black/40">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
      <div class="mx-auto max-w-2xl lg:text-center mb-16">
        <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl bg-clip-text text-transparent bg-gradient-to-r from-purple-400 to-pink-600">
            Get In Touch
        </h2>
        <p class="mt-4 text-lg leading-8 text-gray-400">
            Have a project in mind or just want to chat about AI? Drop me a message.
        </p>
      </div>
      
      <div class="mx-auto max-w-xl bg-cosmic-card p-8 rounded-2xl border border-white/5 shadow-2xl">
          <form @submit.prevent="submitForm" class="space-y-6">
              <div>
                  <label for="name" class="block text-sm font-semibold leading-6 text-white">Name</label>
                  <div class="mt-2.5">
                      <input type="text" v-model="form.name" name="name" id="name" required class="block w-full rounded-md border-0 bg-white/5 px-3.5 py-2 text-white shadow-sm ring-1 ring-inset ring-white/10 focus:ring-2 focus:ring-inset focus:ring-blue-500 sm:text-sm sm:leading-6">
                  </div>
              </div>
              
              <div>
                  <label for="email" class="block text-sm font-semibold leading-6 text-white">Email</label>
                  <div class="mt-2.5">
                      <input type="email" v-model="form.email" name="email" id="email" required class="block w-full rounded-md border-0 bg-white/5 px-3.5 py-2 text-white shadow-sm ring-1 ring-inset ring-white/10 focus:ring-2 focus:ring-inset focus:ring-blue-500 sm:text-sm sm:leading-6">
                  </div>
              </div>

              <div>
                  <label for="subject" class="block text-sm font-semibold leading-6 text-white">Subject</label>
                  <div class="mt-2.5">
                      <input type="text" v-model="form.subject" name="subject" id="subject" class="block w-full rounded-md border-0 bg-white/5 px-3.5 py-2 text-white shadow-sm ring-1 ring-inset ring-white/10 focus:ring-2 focus:ring-inset focus:ring-blue-500 sm:text-sm sm:leading-6">
                  </div>
              </div>
              
              <div>
                  <label for="message" class="block text-sm font-semibold leading-6 text-white">Message</label>
                  <div class="mt-2.5">
                      <textarea v-model="form.message" name="message" id="message" rows="4" required class="block w-full rounded-md border-0 bg-white/5 px-3.5 py-2 text-white shadow-sm ring-1 ring-inset ring-white/10 focus:ring-2 focus:ring-inset focus:ring-blue-500 sm:text-sm sm:leading-6"></textarea>
                  </div>
              </div>
              
              <div>
                  <button type="submit" :disabled="loading" class="btn-primary w-full disabled:opacity-50 disabled:cursor-not-allowed">
                      {{ loading ? 'Sending...' : 'Send Message' }}
                  </button>
              </div>
              
              <div v-if="success" class="p-4 bg-green-900/50 text-green-200 rounded text-center border border-green-500/50">
                  Message sent successfully! I'll get back to you soon.
              </div>
              <div v-if="error" class="p-4 bg-red-900/50 text-red-200 rounded text-center border border-red-500/50">
                  {{ error }}
              </div>
          </form>
      </div>

      <!-- Social Links in Contact Section too -->
      <div class="flex justify-center gap-12 mt-16">
           <a href="https://github.com/tangiraiC" target="_blank" class="flex flex-col items-center gap-3 group">
               <div class="p-4 bg-white/5 rounded-full group-hover:bg-white/10 transition-colors border border-white/5 group-hover:border-white/20">
                   <span class="text-3xl">🐙</span>
               </div>
               <span class="text-gray-400 group-hover:text-white transition-colors">GitHub</span>
           </a>
           <a href="https://www.linkedin.com/in/tangirai/" target="_blank" class="flex flex-col items-center gap-3 group">
               <div class="p-4 bg-white/5 rounded-full group-hover:bg-white/10 transition-colors border border-white/5 group-hover:border-white/20">
                   <span class="text-3xl">💼</span>
               </div>
               <span class="text-gray-400 group-hover:text-white transition-colors">LinkedIn</span>
           </a>
      </div>

    </div>
  </div>
</template>
