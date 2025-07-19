<template>
  <div class="home">
    <h2>Welcome to Expense Tracker</h2>
    <p>Manage your expenses and track your spending habits.</p>
    <div class="quick-actions">
      <router-link to="/expenses" class="btn">Add Expense</router-link>
      <router-link to="/reports" class="btn">View Reports</router-link>
    </div>
  </div>
</template>

<script setup lang="ts">
// Home component logic here
</script>

<style scoped>
.home {
  padding: 2rem;
  text-align: center;
}

.quick-actions {
  margin-top: 2rem;
  display: flex;
  gap: 1rem;
  justify-content: center;
}

.btn {
  padding: 0.75rem 1.5rem;
  background-color: #007bff;
  color: white;
  text-decoration: none;
  border-radius: 0.375rem;
  transition: background-color 0.2s;
}

.btn:hover {
  background-color: #0056b3;
}
</style> 