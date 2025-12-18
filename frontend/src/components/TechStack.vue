<template>
  <div class="w-full bg-cosmic-card py-6 border-y border-white/5 overflow-hidden">
    <div class="relative w-full flex overflow-x-hidden">
      <div class="animate-marquee whitespace-nowrap flex items-center gap-8 sm:gap-16 px-4 sm:px-8">
        <span class="text-base sm:text-xl font-bold text-gray-400 font-mono-code items-center flex gap-2"><span class="text-2xl sm:text-3xl">🐍</span> Python</span>
        <span class="text-base sm:text-xl font-bold text-gray-400 font-mono-code items-center flex gap-2"><span class="text-2xl sm:text-3xl">⚛️</span> React</span>
        <span class="text-base sm:text-xl font-bold text-gray-400 font-mono-code items-center flex gap-2"><span class="text-2xl sm:text-3xl">☁️</span> AWS</span>
        <span class="text-base sm:text-xl font-bold text-gray-400 font-mono-code items-center flex gap-2"><span class="text-2xl sm:text-3xl">🐳</span> Docker</span>
        <span class="text-base sm:text-xl font-bold text-gray-400 font-mono-code items-center flex gap-2"><span class="text-2xl sm:text-3xl">🔥</span> PyTorch</span>
        <span class="text-base sm:text-xl font-bold text-gray-400 font-mono-code items-center flex gap-2"><span class="text-2xl sm:text-3xl">🚀</span> FastAPI</span>
         <!-- Duplicate for smooth loop -->
        <span class="text-base sm:text-xl font-bold text-gray-400 font-mono-code items-center flex gap-2"><span class="text-2xl sm:text-3xl">🐍</span> Python</span>
        <span class="text-base sm:text-xl font-bold text-gray-400 font-mono-code items-center flex gap-2"><span class="text-2xl sm:text-3xl">⚛️</span> React</span>
        <span class="text-base sm:text-xl font-bold text-gray-400 font-mono-code items-center flex gap-2"><span class="text-2xl sm:text-3xl">☁️</span> AWS</span>
        <span class="text-base sm:text-xl font-bold text-gray-400 font-mono-code items-center flex gap-2"><span class="text-2xl sm:text-3xl">🐳</span> Docker</span>
        <span class="text-base sm:text-xl font-bold text-gray-400 font-mono-code items-center flex gap-2"><span class="text-2xl sm:text-3xl">🔥</span> PyTorch</span>
        <span class="text-base sm:text-xl font-bold text-gray-400 font-mono-code items-center flex gap-2"><span class="text-2xl sm:text-3xl">🚀</span> FastAPI</span>
        <!-- Triplicate for wide screens -->
        <span class="text-base sm:text-xl font-bold text-gray-400 font-mono-code items-center flex gap-2"><span class="text-2xl sm:text-3xl">🐍</span> Python</span>
        <span class="text-base sm:text-xl font-bold text-gray-400 font-mono-code items-center flex gap-2"><span class="text-2xl sm:text-3xl">⚛️</span> React</span>
        <span class="text-base sm:text-xl font-bold text-gray-400 font-mono-code items-center flex gap-2"><span class="text-2xl sm:text-3xl">☁️</span> AWS</span>
        <span class="text-base sm:text-xl font-bold text-gray-400 font-mono-code items-center flex gap-2"><span class="text-2xl sm:text-3xl">🐳</span> Docker</span>
        <span class="text-base sm:text-xl font-bold text-gray-400 font-mono-code items-center flex gap-2"><span class="text-2xl sm:text-3xl">🔥</span> PyTorch</span>
        <span class="text-base sm:text-xl font-bold text-gray-400 font-mono-code items-center flex gap-2"><span class="text-2xl sm:text-3xl">🚀</span> FastAPI</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.animate-marquee {
  animation: marquee 25s linear infinite;
}

@keyframes marquee {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}
</style>
