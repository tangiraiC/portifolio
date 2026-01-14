<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRoute } from 'vue-router'

const route = useRoute()
const password = ref('')
const confirmPassword = ref('')
const message = ref('')
const error = ref('')
const loading = ref(false)

import config from '../config'

const API_URL = config.API_URL


const submit = async () => {
    if (password.value !== confirmPassword.value) {
        error.value = "Passwords do not match"
        return
    }

    loading.value = true
    message.value = ''
    error.value = ''
    
    try {
        await axios.post(`${API_URL}/password-reset/confirm/`, {
            uid: route.params.uid,
            token: route.params.token,
            password: password.value
        })
        message.value = 'Password reset successful! You can now login.'
    } catch (err) {
        error.value = 'Invalid or expired token. Please try again.'
    } finally {
        loading.value = false
    }
}
</script>

<template>
  <div class="min-h-screen flex items-center justify-center bg-cosmic-bg text-white relative overflow-hidden">
     <!-- Background Decor -->
    <div class="absolute top-0 left-0 w-full h-full overflow-hidden z-0 pointer-events-none">
       <div class="absolute top-[-10%] right-[-10%] w-[40%] h-[40%] bg-primary-500/20 blur-[120px] rounded-full"></div>
       <div class="absolute bottom-[-10%] left-[-10%] w-[40%] h-[40%] bg-purple-500/20 blur-[120px] rounded-full"></div>
    </div>

    <div class="bg-gray-800/50 backdrop-blur-xl p-8 rounded-2xl shadow-2xl w-96 border border-white/10 relative z-10">
      <h1 class="text-2xl font-bold mb-2 text-center text-transparent bg-clip-text bg-gradient-to-r from-primary-400 to-purple-400">Set New Password</h1>
      <p class="text-gray-400 text-center mb-8 text-sm">Enter your new password below</p>
      
      <form @submit.prevent="submit" class="space-y-4">
        <div>
          <label class="block mb-1 text-sm text-gray-300">New Password</label>
          <input v-model="password" type="password" class="w-full p-3 rounded-lg bg-gray-900/50 border border-gray-700 focus:border-primary-500 outline-none transition text-white placeholder-gray-500" placeholder="••••••••" required />
        </div>
        <div>
          <label class="block mb-1 text-sm text-gray-300">Confirm Password</label>
          <input v-model="confirmPassword" type="password" class="w-full p-3 rounded-lg bg-gray-900/50 border border-gray-700 focus:border-primary-500 outline-none transition text-white placeholder-gray-500" placeholder="••••••••" required />
        </div>
        
        <div v-if="message" class="text-green-400 text-sm text-center bg-green-900/20 p-2 rounded">
            {{ message }}
            <div class="mt-2">
                <router-link to="/login" class="text-white underline font-bold">Log In Now</router-link>
            </div>
        </div>
        <div v-if="error" class="text-red-400 text-sm text-center bg-red-900/20 p-2 rounded">{{ error }}</div>
        
        <button v-if="!message" type="submit" :disabled="loading" class="w-full bg-gradient-to-r from-primary-600 to-purple-600 hover:from-primary-500 hover:to-purple-500 text-white font-bold py-3 px-4 rounded-lg transition shadow-lg shadow-primary-500/20 disabled:opacity-50">
          {{ loading ? 'Resetting...' : 'Reset Password' }}
        </button>
      </form>
      
      <div v-if="!message" class="mt-6 text-center text-sm text-gray-400">
        <router-link to="/login" class="text-primary-400 hover:text-primary-300 transition">Back to Login</router-link>
      </div>
    </div>
  </div>
</template>
