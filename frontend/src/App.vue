<script setup lang="ts">
import Header from './components/components/Header.vue'
</script>

<template>
  <div class="app">
    <Header />
    <main class="main-content">
      <router-view />
    </main>
  </div>
</template>

<style scoped>
.app {
  min-height: 90vh;
  min-width: 90vw;
  display: flex;
  flex-direction: column;
}

.main-content {
  flex: 1;
  background-color: #f8f9fa;
}

</style>
