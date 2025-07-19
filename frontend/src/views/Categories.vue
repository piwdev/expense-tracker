<template>
  <div class="categories">
    <h2>Categories</h2>
    <div class="categories-grid">
      <div class="category-card" v-for="category in categories" :key="category.id">
        <h3>{{ category.name }}</h3>
        <p>Total: ${{ category.total }}</p>
        <p>Count: {{ category.count }}</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const categories = ref([
  { id: 1, name: 'Food', total: 0, count: 0 },
  { id: 2, name: 'Transport', total: 0, count: 0 },
  { id: 3, name: 'Entertainment', total: 0, count: 0 },
  { id: 4, name: 'Utilities', total: 0, count: 0 },
  { id: 5, name: 'Other', total: 0, count: 0 }
])
</script>

<style scoped>
.categories {
  padding: 2rem;
}

.categories-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin-top: 2rem;
}

.category-card {
  padding: 1.5rem;
  border: 1px solid #ddd;
  border-radius: 0.5rem;
  background-color: #f8f9fa;
}

.category-card h3 {
  margin: 0 0 1rem 0;
  color: #333;
}

.category-card p {
  margin: 0.5rem 0;
  color: #666;
}
</style> 