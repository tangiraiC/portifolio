<script setup>
</script>

<template>
  <router-view />
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
