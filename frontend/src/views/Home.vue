<script setup>
import NavBar from '../components/NavBar.vue'
import Hero from '../components/Hero.vue'
import TechStack from '../components/TechStack.vue'
import AboutSection from '../components/AboutSection.vue'
import ProjectGrid from '../components/ProjectGrid.vue'
import Publications from '../components/Publications.vue'
import ProofArea from '../components/ProofArea.vue'
import ContactSection from '../components/ContactSection.vue'
import Footer from '../components/Footer.vue'
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
