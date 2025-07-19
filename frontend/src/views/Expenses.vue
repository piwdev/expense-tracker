<template>
  <div class="expenses">
    <h2>Expenses</h2>
    <div class="expense-form">
      <h3>Add New Expense</h3>
      <form @submit.prevent="addExpense">
        <div class="form-group">
          <label for="description">Description:</label>
          <input type="text" id="description" v-model="newExpense.description" required>
        </div>
        <div class="form-group">
          <label for="amount">Amount:</label>
          <input type="number" id="amount" v-model="newExpense.amount" step="0.01" required>
        </div>
        <div class="form-group">
          <label for="category">Category:</label>
          <select id="category" v-model="newExpense.category" required>
            <option value="">Select Category</option>
            <option value="food">Food</option>
            <option value="transport">Transport</option>
            <option value="entertainment">Entertainment</option>
            <option value="utilities">Utilities</option>
            <option value="other">Other</option>
          </select>
        </div>
        <button type="submit" class="btn">Add Expense</button>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const newExpense = ref({
  description: '',
  amount: '',
  category: ''
})

const addExpense = () => {
  // TODO: Implement expense addition logic
  console.log('Adding expense:', newExpense.value)
  // Reset form
  newExpense.value = {
    description: '',
    amount: '',
    category: ''
  }
}
</script>

<style scoped>
.expenses {
  padding: 2rem;
}

.expense-form {
  max-width: 500px;
  margin: 0 auto;
  padding: 1.5rem;
  border: 1px solid #ddd;
  border-radius: 0.5rem;
}

.form-group {
  margin-bottom: 1rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
}

.form-group input,
.form-group select {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 0.25rem;
}

.btn {
  padding: 0.75rem 1.5rem;
  background-color: #28a745;
  color: white;
  border: none;
  border-radius: 0.375rem;
  cursor: pointer;
  transition: background-color 0.2s;
}

.btn:hover {
  background-color: #218838;
}
</style> 