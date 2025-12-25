<script setup>
import { ref, watch, onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const activeTab = ref('experience')
const items = ref([])
const showModal = ref(false)
const editingItem = ref(null)
const formData = ref({})

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api'
const token = localStorage.getItem('token')

const headers = {
  Authorization: `Token ${token}`,
  'Content-Type': 'multipart/form-data' // Important for file uploads
}

// Configuration for each resource type
const resourceConfig = {
  projects: {
    endpoint: 'projects',
    title: 'Projects',
    fields: [
      { key: 'title', label: 'Title', type: 'text' },
      { key: 'primary_category', label: 'Category ID', type: 'number' }, // MVP: Just ID for now
      { key: 'status', label: 'Status (in_progress, completed)', type: 'text' },
      { key: 'abstract', label: 'Abstract', type: 'textarea' },
      { key: 'tech_stack_csv', label: 'Tech Stack (CSV)', type: 'text' },
      { key: 'repo_url', label: 'GitHub URL', type: 'url' },
      { key: 'demo_url', label: 'Demo URL', type: 'url' },
      { key: 'cover_image', label: 'Cover Image', type: 'file' }
    ]
  },
  publications: {
     endpoint: 'research', // Mapped to ResearchPaperViewSet
     title: 'Publications',
     fields: [
       { key: 'title', label: 'Title', type: 'text' },
       { key: 'published_at', label: 'Date', type: 'date' },
       { key: 'citation', label: 'Citation', type: 'textarea' },
       { key: 'abstract', label: 'Abstract', type: 'textarea' },
       { key: 'link', label: 'Live Link', type: 'url' },
       { key: 'pdf', label: 'PDF File', type: 'file' }
     ]
  },
  experience: {
    endpoint: 'experience',
    title: 'Experience',
    fields: [
      { key: 'company', label: 'Company', type: 'text' },
      { key: 'role', label: 'Role', type: 'text' },
      { key: 'start_date', label: 'Start Date', type: 'date' },
      { key: 'end_date', label: 'End Date', type: 'date' },
      { key: 'description', label: 'Description (Markdown)', type: 'textarea' }
    ]
  },
  education: {
    endpoint: 'education',
    title: 'Education',
    fields: [
      { key: 'institution', label: 'Institution', type: 'text' },
      { key: 'degree', label: 'Degree', type: 'text' },
      { key: 'start_date', label: 'Start Date', type: 'date' },
      { key: 'end_date', label: 'End Date', type: 'date' },
      { key: 'description', label: 'Description', type: 'textarea' }
    ]
  },
  skills: {
    endpoint: 'skills',
    title: 'Skills',
    fields: [
      { key: 'name', label: 'Skill Name', type: 'text' },
      { key: 'proficiency', label: 'Proficiency (1-100)', type: 'number' },
      { key: 'category', label: 'Category', type: 'text' }
    ]
  },
  settings: {
    endpoint: 'site-settings',
    title: 'Site Settings',
    isSingleton: true,
    fields: [
      { key: 'about_me', label: 'About Me', type: 'textarea' },
      { key: 'resume_link', label: 'Resume Link', type: 'url' },
      { key: 'contact_email', label: 'Contact Email', type: 'email' },
      { key: 'github_url', label: 'GitHub URL', type: 'url' },
      { key: 'linkedin_url', label: 'LinkedIn URL', type: 'url' }
    ]
  }
}

const currentConfig = computed(() => resourceConfig[activeTab.value])

const fetchItems = async () => {
  try {
    const response = await axios.get(`${API_URL}/${currentConfig.value.endpoint}/`)
    items.value = response.data.results || response.data
  } catch (err) {
    if (err.response && err.response.status === 401) {
      logout()
    }
  }
}

const deleteItem = async (id) => {
  if (!confirm('Are you sure?')) return
  try {
    const token = localStorage.getItem('token')
    await axios.delete(`${API_URL}/${currentConfig.value.endpoint}/${id}/`, { 
        headers: { Authorization: `Token ${token}` }  // Only need Auth for delete
    })
    fetchItems()
  } catch (err) {
    alert('Failed to delete')
  }
}

const handleFileUpload = (event, key) => {
    formData.value[key] = event.target.files[0]
}

const saveItem = async () => {
  try {
    const url = editingItem.value 
      ? `${API_URL}/${currentConfig.value.endpoint}/${editingItem.value.id}/`
      : `${API_URL}/${currentConfig.value.endpoint}/`
    
    const method = editingItem.value ? 'put' : 'post'
    
    // Construct FormData for file uploads
    const data = new FormData()
    for (const key in formData.value) {
        if (formData.value[key] !== null && formData.value[key] !== undefined) {
             data.append(key, formData.value[key])
        }
    }

    const token = localStorage.getItem('token')
    await axios[method](url, data, { 
        headers: { 
            Authorization: `Token ${token}`,
            'Content-Type': 'multipart/form-data'
        } 
    })
    showModal.value = false
    fetchItems()
  } catch (err) {
    alert('Failed to save')
    console.error(err)
  }
}


const openModal = (item = null) => {
  editingItem.value = item
  formData.value = item ? { ...item } : {}
  showModal.value = true
}

const logout = () => {
  localStorage.removeItem('token')
  router.push('/login')
}

watch(activeTab, fetchItems)
onMounted(fetchItems)
</script>

<template>
  <div class="min-h-screen bg-cosmic-bg text-white flex">
    <!-- Sidebar -->
    <aside class="w-64 bg-gray-900 border-r border-gray-800 p-6 flex flex-col">
      <h1 class="text-2xl font-bold text-primary-400 mb-8">Portfolio Admin</h1>
      
      <nav class="flex-1 space-y-2">
        <button 
          v-for="(config, key) in resourceConfig" 
          :key="key"
          @click="activeTab = key"
          class="w-full text-left px-4 py-2 rounded transition capitalize"
          :class="activeTab === key ? 'bg-primary-600 text-white' : 'text-gray-400 hover:bg-gray-800'"
        >
          {{ config.title }}
        </button>
      </nav>


      <button @click="logout" class="mt-auto text-red-400 hover:text-red-300 flex items-center gap-2">
        <span>Logout</span>
      </button>
    </aside>

    <!-- Main Content -->
    <main class="flex-1 p-8 overflow-y-auto">
      <div class="flex justify-between items-center mb-8">
        <h2 class="text-3xl font-bold capitalize">{{ currentConfig.title }} Management</h2>
        <button 
          v-if="!currentConfig.isSingleton"
          @click="openModal()" 
          class="bg-green-600 hover:bg-green-700 text-white px-4 py-2 rounded"
        >
          + Add New
        </button>
      </div>
      
      <!-- List View -->
      <div class="bg-gray-800 rounded-lg border border-gray-700 overflow-hidden">
        <table class="w-full text-left">
          <thead class="bg-gray-900 text-gray-400">
            <tr>
              <th v-for="field in currentConfig.fields.slice(0, 3)" :key="field.key" class="p-4">{{ field.label }}</th>
              <th class="p-4 text-right">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in items" :key="item.id" class="border-t border-gray-700 hover:bg-gray-750">
              <td v-for="field in currentConfig.fields.slice(0, 3)" :key="field.key" class="p-4">
                {{ item[field.key] }}
              </td>
              <td class="p-4 text-right space-x-2">
                <button @click="openModal(item)" class="text-blue-400 hover:text-blue-300">Edit</button>
                <button @click="deleteItem(item.id)" class="text-red-400 hover:text-red-300">Delete</button>
              </td>
            </tr>
            <tr v-if="items.length === 0" class="border-t border-gray-700">
              <td colspan="4" class="p-8 text-center text-gray-500">No items found.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </main>

    <!-- Modal -->
    <div v-if="showModal" class="fixed inset-0 bg-black/80 flex items-center justify-center p-4 z-50">
      <div class="bg-gray-800 rounded-lg w-full max-w-lg p-6 max-h-[90vh] overflow-y-auto">
        <h3 class="text-2xl font-bold mb-6">{{ editingItem ? 'Edit' : 'Add' }} {{ currentConfig.title }}</h3>
        
        <form @submit.prevent="saveItem" class="space-y-4">
          <div v-for="field in currentConfig.fields" :key="field.key">
            <label class="block mb-1 text-sm text-gray-400">{{ field.label }}</label>
            <textarea 
              v-if="field.type === 'textarea'" 
              v-model="formData[field.key]"
              class="w-full p-2 rounded bg-gray-700 border border-gray-600 focus:border-primary-500 outline-none h-32"
            ></textarea>
            <input 
              v-else-if="field.type === 'file'"
              @change="(e) => handleFileUpload(e, field.key)"
              type="file"
              class="w-full p-2 rounded bg-gray-700 border border-gray-600 focus:border-primary-500 outline-none text-gray-300"
            />
            <input 
              v-else 
              v-model="formData[field.key]" 
              :type="field.type"
              class="w-full p-2 rounded bg-gray-700 border border-gray-600 focus:border-primary-500 outline-none"
            />

          </div>

          <div class="flex justify-end gap-4 mt-8">
            <button type="button" @click="showModal = false" class="text-gray-400 hover:text-white">Cancel</button>
            <button type="submit" class="bg-primary-600 hover:bg-primary-700 text-white px-6 py-2 rounded">Save</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

