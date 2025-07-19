<template>
  <div class="reports">
    <h2>Reports</h2>
    <div class="reports-grid">
      <div class="report-card">
        <h3>Monthly Overview</h3>
        <div class="stat">
          <span class="label">Total Expenses:</span>
          <span class="value">${{ totalExpenses }}</span>
        </div>
        <div class="stat">
          <span class="label">Average per Day:</span>
          <span class="value">${{ averagePerDay }}</span>
        </div>
      </div>
      
      <div class="report-card">
        <h3>Top Categories</h3>
        <div class="category-list">
          <div class="category-item" v-for="category in topCategories" :key="category.name">
            <span class="category-name">{{ category.name }}</span>
            <span class="category-amount">${{ category.amount }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const totalExpenses = ref(0)
const averagePerDay = ref(0)

const topCategories = ref([
  { name: 'Food', amount: 0 },
  { name: 'Transport', amount: 0 },
  { name: 'Entertainment', amount: 0 },
  { name: 'Utilities', amount: 0 },
  { name: 'Other', amount: 0 }
])
</script>

<style scoped>
.reports {
  padding: 2rem;
}

.reports-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin-top: 2rem;
}

.report-card {
  padding: 1.5rem;
  border: 1px solid #ddd;
  border-radius: 0.5rem;
  background-color: white;
}

.report-card h3 {
  margin: 0 0 1.5rem 0;
  color: #333;
  border-bottom: 2px solid #007bff;
  padding-bottom: 0.5rem;
}

.stat {
  display: flex;
  justify-content: space-between;
  margin-bottom: 1rem;
  padding: 0.5rem 0;
}

.label {
  font-weight: 500;
  color: #666;
}

.value {
  font-weight: bold;
  color: #333;
}

.category-list {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.category-item {
  display: flex;
  justify-content: space-between;
  padding: 0.5rem 0;
  border-bottom: 1px solid #eee;
}

.category-name {
  color: #666;
}

.category-amount {
  font-weight: bold;
  color: #333;
}
</style> 