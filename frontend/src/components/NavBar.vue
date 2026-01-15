<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const navigation = ref([
  { name: 'Projects', href: '/#projects' },
  { name: 'Certifications', href: '/#proof-area' },
  { name: 'Publications', href: '/#publications' },
  { name: 'Resume', href: '/resume' },
  { name: 'Blog', href: '/blog' },
])

const mobileMenuOpen = ref(false)
// Logic for dynamic resume fetching removed as we now have a dedicated page
</script>

<template>
  <header class="fixed inset-x-0 top-0 z-50 bg-cosmic-bg/90 backdrop-blur-md border-b border-white/5">
    <nav class="flex items-center justify-between p-6 lg:px-8" aria-label="Global">
      <div class="flex lg:flex-1">
        <a href="#" class="-m-1.5 p-1.5 text-2xl font-bold tracking-tight text-white">
          Lincoln
        </a>
      </div>
      <div class="flex lg:hidden">
        <button type="button" @click="mobileMenuOpen = true" class="-m-2.5 inline-flex items-center justify-center rounded-md p-2.5 text-gray-400">
          <span class="sr-only">Open main menu</span>
          <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
            <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
          </svg>
        </button>
      </div>
      <div class="hidden lg:flex lg:gap-x-12">
        <a v-for="item in navigation" :key="item.name" :href="item.href" :target="item.target || '_self'" class="text-sm font-semibold leading-6 text-gray-300 hover:text-white transition-colors">
          {{ item.name }}
        </a>
      </div>
      <div class="hidden lg:flex lg:flex-1 lg:justify-end">
        <a href="/#contact" class="btn-primary text-sm">
            Contact
        </a>
      </div>
    </nav>
    <!-- Mobile menu -->
    <Teleport to="body">
      <div class="lg:hidden" v-if="mobileMenuOpen">
        <!-- Backdrop (optional since panel is full screen, but good for safety) -->
        <div class="fixed inset-0 z-[998] bg-black/80 backdrop-blur-sm" @click="mobileMenuOpen = false" />
        
        <!-- Panel -->
        <div class="fixed inset-0 z-[999] w-full bg-black px-6 py-6 shadow-2xl flex flex-col items-center justify-center">
          <div class="absolute top-6 right-6">
            <button type="button" @click="mobileMenuOpen = false" class="-m-2.5 rounded-md p-2.5 text-gray-400 hover:text-white">
              <span class="sr-only">Close menu</span>
              <svg class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" aria-hidden="true">
                <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
          
          <div class="flex items-center justify-center mb-12">
            <a href="#" class="-m-1.5 p-1.5 text-3xl font-bold text-white">
              Lincoln
            </a>
          </div>
          
          <div class="flex flex-col space-y-8 text-center w-full max-w-sm">
              <a v-for="item in navigation" :key="item.name" :href="item.href" :target="item.target || '_self'" @click="mobileMenuOpen = false" class="text-2xl font-bold leading-7 text-white hover:text-blue-400 transition-colors block py-2 border-b border-gray-800">
                {{ item.name }}
              </a>
              <div class="pt-8">
                  <a href="#contact" @click="mobileMenuOpen = false" class="btn-primary inline-block text-xl px-10 py-4 w-full text-center shadow-lg shadow-blue-900/20">Contact Me</a>
              </div>
          </div>
        </div>
      </div>
    </Teleport>
  </header>
</template>
