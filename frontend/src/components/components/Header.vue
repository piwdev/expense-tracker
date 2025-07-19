<template>
    <header class="header">
        <div class="header-content">
            <h3>Expense Tracker</h3>
            <nav class="nav">
                <router-link to="/" class="nav-link">Home</router-link>
                <router-link to="/expenses" class="nav-link">Expenses</router-link>
                <router-link to="/categories" class="nav-link">Categories</router-link>
                <router-link to="/reports" class="nav-link">Reports</router-link>
            </nav>
        </div>
    </header>
</template>

<style scoped>
.header {
    background-color: #2c3e50;
    border-bottom: 1px solid #379bff;
    color: white;
    padding: 1rem 0;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.header-content {
    padding: 0 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo {
    font-size: 1.5rem;
    font-weight: bold;
    color: white;
    text-decoration: none;
}

.nav {
    margin-left: 2rem;
    display: flex;
    gap: 2rem;
}

.nav-link {
    color: #ecf0f1;
    text-decoration: none;
    padding: 0.5rem 1rem;
    border-radius: 0.25rem;
    transition: background-color 0.2s;
}

.nav-link:hover {
    background-color: #34495e;
}

.nav-link.router-link-active {
    background-color: #3498db;
    color: white;
}
</style>