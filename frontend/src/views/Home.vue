<script setup>
import NavBar from '../components/NavBar.vue'
import Hero from '../components/Hero.vue'
import TechStack from '../components/TechStack.vue'
import AboutSection from '../components/AboutSection.vue'
import ProjectGrid from '../components/ProjectGrid.vue'
import Publications from '../components/Publications.vue'
import BlogFeed from '../components/BlogFeed.vue'
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
      <section id="writing" aria-labelledby="writing-heading" class="mx-auto max-w-7xl px-6 lg:px-8 py-24">
        <div class="flex items-center justify-between gap-4 mb-8">
          <h2 id="writing-heading" class="text-3xl font-bold">Latest writing</h2>
          <router-link to="/blog" class="text-link underline">All articles <span>↗</span></router-link>
        </div>
        <BlogFeed />
      </section>
      <ProofArea />
      <ContactSection />
    </main>
    <Footer />
  </div>
</template>
