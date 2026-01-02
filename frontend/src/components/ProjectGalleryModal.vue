<script setup>
import { ref, computed } from 'vue'
import { XMarkIcon, ChevronLeftIcon, ChevronRightIcon } from '@heroicons/vue/24/outline'

const props = defineProps({
  project: {
    type: Object, 
    required: true
  },
  isOpen: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['close'])

const currentImageIndex = ref(0) // 0 is cover image, 1+ are gallery images

// Combine cover image and gallery images into a single list
const allImages = computed(() => {
    const images = []
    if (props.project.cover_image) {
        images.push({
            image: props.project.cover_image,
            caption: 'Cover Image',
            isCover: true
        })
    }
    
    if (props.project.images && props.project.images.length > 0) {
        // Sort by order if available, otherwise just append
        const gallery = [...props.project.images].sort((a,b) => a.order - b.order)
        images.push(...gallery)
    }
    
    return images
})

const currentImage = computed(() => {
    if (allImages.value.length === 0) return null
    return allImages.value[currentImageIndex.value]
})

const nextImage = () => {
    if (currentImageIndex.value < allImages.value.length - 1) {
        currentImageIndex.value++
    } else {
        currentImageIndex.value = 0 // Loop
    }
}

const prevImage = () => {
    if (currentImageIndex.value > 0) {
        currentImageIndex.value--
    } else {
        currentImageIndex.value = allImages.value.length - 1 // Loop
    }
}

const selectImage = (index) => {
    currentImageIndex.value = index
}
</script>

<template>
  <div v-if="isOpen" class="fixed inset-0 z-50 flex items-center justify-center p-4 sm:p-6" role="dialog" aria-modal="true">
    <!-- Backdrop -->
    <div class="fixed inset-0 bg-black/90 backdrop-blur-sm transition-opacity" @click="$emit('close')"></div>

    <!-- Modal Panel -->
    <div class="relative w-full max-w-6xl max-h-[90vh] bg-gray-900 rounded-2xl shadow-2xl flex flex-col overflow-hidden border border-white/10">
      
      <!-- Close Button -->
      <button 
        @click="$emit('close')"
        class="absolute top-4 right-4 z-10 p-2 bg-black/50 hover:bg-black/70 rounded-full text-white transition-colors"
      >
        <XMarkIcon class="w-6 h-6" />
      </button>

      <div class="flex flex-col lg:flex-row h-full overflow-hidden">
          
          <!-- Image Section (Large) -->
          <div class="flex-1 bg-black relative flex items-center justify-center min-h-[40vh] lg:h-full group">
              <div v-if="currentImage" class="relative w-full h-full flex items-center justify-center">
                  <img :src="currentImage.image" :alt="currentImage.caption || props.project.title" class="max-w-full max-h-[80vh] object-contain" />
                  
                  <!-- Navigation Arrows (only if > 1 image) -->
                  <div v-if="allImages.length > 1">
                      <button @click.stop="prevImage" class="absolute left-4 top-1/2 -translate-y-1/2 p-3 bg-black/50 hover:bg-primary-600/80 rounded-full text-white transition-all opacity-0 group-hover:opacity-100">
                          <ChevronLeftIcon class="w-6 h-6" />
                      </button>
                      <button @click.stop="nextImage" class="absolute right-4 top-1/2 -translate-y-1/2 p-3 bg-black/50 hover:bg-primary-600/80 rounded-full text-white transition-all opacity-0 group-hover:opacity-100">
                          <ChevronRightIcon class="w-6 h-6" />
                      </button>
                  </div>
                  
                  <!-- Caption -->
                  <div v-if="currentImage.caption" class="absolute bottom-4 left-0 right-0 text-center px-4">
                      <span class="inline-block bg-black/60 px-3 py-1 rounded text-sm text-gray-200 backdrop-blur-sm">
                          {{ currentImage.caption }}
                      </span>
                  </div>
              </div>
              <div v-else class="text-gray-500">No images available</div>
          </div>

          <!-- Info & Thumbnails Section -->
          <div class="w-full lg:w-96 bg-gray-900 border-t lg:border-t-0 lg:border-l border-white/10 flex flex-col">
              <!-- Scrollable Thumbnails -->
              <div class="p-4 border-b border-white/5 bg-gray-800/50">
                   <h3 class="text-xs font-bold uppercase text-gray-500 mb-3 tracking-wider">Gallery</h3>
                   <div class="flex lg:grid lg:grid-cols-4 gap-2 overflow-x-auto lg:overflow-visible pb-2 lg:pb-0">
                       <button 
                         v-for="(img, idx) in allImages" 
                         :key="idx"
                         @click="selectImage(idx)"
                         class="relative w-16 h-16 flex-shrink-0 rounded-lg overflow-hidden border-2 transition-all hover:opacity-100"
                         :class="currentImageIndex === idx ? 'border-primary-500 opacity-100 ring-2 ring-primary-500/30' : 'border-transparent opacity-60 hover:border-white/30'"
                       >
                           <img :src="img.image" class="w-full h-full object-cover" />
                       </button>
                   </div>
              </div>

              <!-- Project Info -->
              <div class="p-6 overflow-y-auto flex-1">
                  <h2 class="text-2xl font-bold text-white mb-2">{{ props.project.title }}</h2>
                  <div class="flex flex-wrap gap-2 mb-4">
                      <span class="px-2 py-0.5 rounded text-xs bg-primary-900/40 text-primary-300 border border-primary-500/20">
                          {{ props.project.category_name }}
                      </span>
                      <span v-if="props.project.status" class="px-2 py-0.5 rounded text-xs bg-gray-700 text-gray-300 capitalize">
                          {{ props.project.status.replace('_', ' ') }}
                      </span>
                  </div>
                  
                  <p class="text-gray-300 mb-6 text-sm leading-relaxed whitespace-pre-line">
                      {{ props.project.description || props.project.abstract }}
                  </p>

                  <div class="space-y-4">
                       <div v-if="props.project.tech_stack_csv">
                           <h4 class="text-xs font-bold text-gray-500 uppercase tracking-wider mb-2">Tech Stack</h4>
                           <div class="flex flex-wrap gap-2">
                               <span v-for="tech in props.project.tech_stack_csv.split(',')" :key="tech" class="text-xs text-blue-300 bg-blue-900/20 px-2 py-1 rounded">
                                   {{ tech.trim() }}
                               </span>
                           </div>
                       </div>
                       
                       <div class="pt-6 border-t border-white/5 flex flex-col gap-3">
                           <a v-if="props.project.demo_url" :href="props.project.demo_url" target="_blank" class="w-full text-center bg-primary-600 hover:bg-primary-500 text-white font-bold py-3 rounded-lg transition">
                               Launch Live Demo
                           </a>
                           <a v-if="props.project.repo_url" :href="props.project.repo_url" target="_blank" class="w-full text-center bg-gray-700 hover:bg-gray-600 text-white font-medium py-3 rounded-lg transition">
                               View Source Code
                           </a>
                       </div>
                  </div>
              </div>
          </div>
      </div>
    </div>
  </div>
</template>
