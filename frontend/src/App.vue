<script setup>
import NavBar from './components/NavBar.vue'
import Hero from './components/Hero.vue'
import TechStack from './components/TechStack.vue'
import AboutSection from './components/AboutSection.vue'
import ProjectGrid from './components/ProjectGrid.vue'
import Publications from './components/Publications.vue'
import ProofArea from './components/ProofArea.vue'
import ContactSection from './components/ContactSection.vue'
import Footer from './components/Footer.vue'
</script>

<template>
  <div class="bg-cosmic-bg min-h-screen text-white font-sans antialiased text-gray-300">
    <NavBar />
    <main class="pt-20 lg:pt-0">
      <Hero />
      <TechStack />
      <AboutSection />
      <ProjectGrid />
      <Publications />
      <ProofArea />
      <ContactSection />
    </main>
    <Footer />
  </div>
</template>

<style>
/* Global scrollbar styling */
::-webkit-scrollbar {
  width: 10px;
}
::-webkit-scrollbar-track {
  background: #0a0a16;
}
::-webkit-scrollbar-thumb {
  background: #2d2d44;
  border-radius: 5px;
}
::-webkit-scrollbar-thumb:hover {
  background: #4a4a6e;
}

html {
  scroll-behavior: smooth;
  scroll-padding-top: 80px; /* Offset for sticky nav */
}
</style>
