<template>
  <div class="parent-home-view">
    <h2 class="dashboard-header">Parent Dashboard</h2>
    <p class="text-gray-600 mb-6">Monitor and guide your children's financial journey.</p>

    <div class="info-cards-grid">
      <div class="info-card">
        <h3>Total Children</h3>
        <p>{{ children.length }}</p>
      </div>
      <div class="info-card">
        <h3>Total Allowances</h3>
        <p>₹{{ totalAllowances }}</p>
      </div>
      <div class="info-card">
        <h3>Active Goals</h3>
        <p>{{ activeGoals }}</p>
      </div>
    </div>

    <div class="content-card">
      <h3 class="text-xl font-semibold mb-4">Children Overview</h3>
      <div class="children-overview-grid">
        <div v-for="child in children" :key="child.id" class="child-card">
          <div class="child-info">
            <h4>{{ child.name }}</h4>
            <p class="text-sm text-gray-500">{{ child.class }}</p>
          </div>
          <div class="child-stats">
            <div class="stat">
              <span class="label">Balance:</span>
              <span class="value text-green-600">₹{{ child.balance }}</span>
            </div>
            <div class="stat">
              <span class="label">Goals:</span>
              <span class="value">{{ child.activeGoals }}</span>
            </div>
          </div>
          <button class="btn-view-details" @click="viewChildDetails(child.id)">
            View Details
          </button>
        </div>
      </div>
    </div>

    <div class="content-card">
      <h3 class="text-xl font-semibold mb-4">Recent Activities</h3>
      <ul class="list-none p-0 m-0">
        <li v-for="activity in recentActivities" :key="activity.id" 
            class="flex justify-between items-center py-3 border-b border-gray-200 last:border-b-0">
          <div class="flex items-center gap-3">
            <span class="text-gray-700 font-medium">{{ activity.description }}</span>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-sm text-gray-500">{{ activity.date }}</span>
            <span :class="activity.type === 'allowance' ? 'text-green-600' : 'text-red-600'" 
                  class="font-semibold">{{ activity.amount }}</span>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ParentHomeView',
  data() {
    return {
      children: [
        {
          id: 1,
          name: 'Spriha Mishra',
          class: '5th Grade',
          balance: 1200,
          activeGoals: 3
        },
        {
          id: 2,
          name: 'Kalkin Mishra',
          class: '3rd Grade',
          balance: 800,
          activeGoals: 2
        }
      ],
      recentActivities: [
        {
          id: 1,
          description: 'Spriha received weekly allowance',
          amount: '+₹500',
          date: '2024-06-25',
          type: 'allowance'
        },
        {
          id: 2,
          description: 'Kalkin spent on toy car',
          amount: '-₹200',
          date: '2024-06-24',
          type: 'spend'
        }
      ]
    };
  },
  computed: {
    totalAllowances() {
      return this.children.reduce((sum, child) => sum + child.balance, 0);
    },
    activeGoals() {
      return this.children.reduce((sum, child) => sum + child.activeGoals, 0);
    }
  },
  methods: {
    viewChildDetails(childId) {
      // Implementation for viewing child details
      console.log('Viewing details for child:', childId);
    }
  }
};
</script>

<style scoped>
.children-overview-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1rem;
}

.child-card {
  background: white;
  border-radius: 0.5rem;
  padding: 1rem;
  border: 1px solid #e5e7eb;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.child-info h4 {
  font-weight: 600;
  margin-bottom: 0.25rem;
}

.child-stats {
  margin: 1rem 0;
}

.stat {
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.5rem;
}

.btn-view-details {
  background-color: #7c3aed;
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  border: none;
  cursor: pointer;
  font-weight: 500;
}
</style>
