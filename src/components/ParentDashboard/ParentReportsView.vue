<template>
  <div class="parent-reports-view w-full">
    <h2 class="dashboard-header">Financial Reports</h2>

    <div class="info-cards-grid mb-6">
      <div class="info-card">
        <h3>Total Allowances Sent</h3>
        <p>₹{{ totalAllowancesSent }}</p>
      </div>
      <div class="info-card">
        <h3>Children's Total Savings</h3>
        <p>₹{{ totalChildrenSavings }}</p>
      </div>
      <div class="info-card">
        <h3>Average Monthly Spend</h3>
        <p>₹{{ averageMonthlySpend }}</p>
      </div>
    </div>

    <div class="content-card">
      <h3 class="text-xl font-semibold mb-4">Monthly Spending Trends</h3>
      <div class="chart-placeholder">
        <img src="https://sta.laits.utexas.edu/wp-content/uploads/files/charts.png" alt="Monthly Spending Trends Chart" width="1000" height="300">
      </div>
    </div>

    <div class="content-card">
      <h3 class="text-xl font-semibold mb-4">Children's Financial Goals Progress</h3>
      <div class="goals-progress-grid">
        <div v-for="child in childrenProgress" :key="child.id" class="child-progress-card">
          <h4>{{ child.name }}</h4>
          <div class="progress-stats">
            <div class="stat-item">
              <span class="label">Active Goals:</span>
              <span class="value">{{ child.activeGoals }}</span>
            </div>
            <div class="stat-item">
              <span class="label">Completed Goals:</span>
              <span class="value">{{ child.completedGoals }}</span>
            </div>
            <div class="stat-item">
              <span class="label">Total Saved:</span>
              <span class="value text-green-600">₹{{ child.totalSaved }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="content-card">
      <h3 class="text-xl font-semibold mb-4">Recent Transactions</h3>
      <table class="w-full border-collapse">
        <thead>
          <tr class="bg-gray-50">
            <th class="border p-2 text-left">Date</th>
            <th class="border p-2 text-left">Child</th>
            <th class="border p-2 text-left">Type</th>
            <th class="border p-2 text-left">Amount</th>
            <th class="border p-2 text-left">Description</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="transaction in recentTransactions" :key="transaction.id">
            <td class="border p-2">{{ transaction.date }}</td>
            <td class="border p-2">{{ transaction.childName }}</td>
            <td class="border p-2">{{ transaction.type }}</td>
            <td class="border p-2" :class="transaction.type === 'allowance' ? 'text-green-600' : 'text-red-600'">
              {{ transaction.type === 'allowance' ? '+' : '-' }}₹{{ transaction.amount }}
            </td>
            <td class="border p-2">{{ transaction.description }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ParentReportsView',
  data() {
    return {
      childrenProgress: [
        {
          id: 1,
          name: 'Spriha Mishra',
          activeGoals: 2,
          completedGoals: 5,
          totalSaved: 2500
        },
        {
          id: 2,
          name: 'Kalkin Mishra',
          activeGoals: 1,
          completedGoals: 3,
          totalSaved: 1800
        }
      ],
      recentTransactions: [
        {
          id: 1,
          date: '2024-06-25',
          childName: 'Spriha Mishra',
          type: 'allowance',
          amount: 500,
          description: 'Weekly allowance'
        },
        {
          id: 2,
          date: '2024-06-24',
          childName: 'Kalkin Mishra',
          type: 'spend',
          amount: 200,
          description: 'Toy purchase'
        }
      ]
    };
  },
  computed: {
    totalAllowancesSent() {
      return this.recentTransactions
        .filter(t => t.type === 'allowance')
        .reduce((sum, t) => sum + t.amount, 0);
    },
    totalChildrenSavings() {
      return this.childrenProgress.reduce((sum, child) => sum + child.totalSaved, 0);
    },
    averageMonthlySpend() {
      const totalSpends = this.recentTransactions
        .filter(t => t.type === 'spend')
        .reduce((sum, t) => sum + t.amount, 0);
      return Math.round(totalSpends / 1); // Assuming 1 month of data
    }
  }
};
</script>

<style scoped>
.goals-progress-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1rem;
}

.child-progress-card {
  background: white;
  border-radius: 0.5rem;
  padding: 1rem;
  border: 1px solid #e5e7eb;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.progress-stats {
  margin-top: 1rem;
}

.stat-item {
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.5rem;
}

.chart-placeholder {
  height: 200px;
  background: #f3f4f6;
  border-radius: 0.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #6b7280;
  font-style: italic;
}
</style>