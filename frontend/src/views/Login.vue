<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const username = ref('')
const password = ref('')
const error = ref('')
const router = useRouter()

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api'

const login = async () => {
  try {
    const response = await axios.post(`${API_URL}/login/`, {
      username: username.value,
      password: password.value
    })
    localStorage.setItem('token', response.data.token)
    router.push('/admin')
  } catch (err) {
    error.value = 'Invalid credentials'
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
      <h1 class="text-3xl font-bold mb-2 text-center text-transparent bg-clip-text bg-gradient-to-r from-primary-400 to-purple-400">Welcome Back</h1>
      <p class="text-gray-400 text-center mb-8 text-sm">Access your command center</p>
      
      <form @submit.prevent="login" class="space-y-4">
        <div>
          <label class="block mb-1 text-sm text-gray-300">Username</label>
          <input v-model="username" type="text" class="w-full p-3 rounded-lg bg-gray-900/50 border border-gray-700 focus:border-primary-500 outline-none transition text-white placeholder-gray-500" placeholder="admin" required />
        </div>
        <div>
          <label class="block mb-1 text-sm text-gray-300">Password</label>
          <input v-model="password" type="password" class="w-full p-3 rounded-lg bg-gray-900/50 border border-gray-700 focus:border-primary-500 outline-none transition text-white placeholder-gray-500" placeholder="••••••••" required />
          <div class="text-right mt-1">
            <router-link to="/forgot-password" class="text-xs text-primary-400 hover:text-primary-300 transition">Forgot Password?</router-link>
          </div>
        </div>
        <div v-if="error" class="text-red-400 text-sm text-center bg-red-900/20 p-2 rounded">{{ error }}</div>
        <button type="submit" class="w-full bg-gradient-to-r from-primary-600 to-purple-600 hover:from-primary-500 hover:to-purple-500 text-white font-bold py-3 px-4 rounded-lg transition shadow-lg shadow-primary-500/20">
          Login
        </button>
      </form>
      
      <div class="mt-6 text-center text-sm text-gray-400">
        Need an account? 
        <router-link to="/register" class="text-primary-400 hover:text-primary-300 transition">Register</router-link>
      </div>
    </div>
  </div>
</template>
