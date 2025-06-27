<template>
  <div class="admin-home-view">
    <h2 class="dashboard-header">Admin Dashboard</h2>
    <p> Overview of the PennyWise system and key statistics.</p>
    <br>

    <div class="info-cards-grid">
      <div class="info-card">
        <h3>Total Users</h3>
        <p>{{ totalUsers }}</p>
      </div>
      <div class="info-card">
        <h3>Active Schools</h3>
        <p>{{ activeSchools }}</p>
      </div>
      <div class="info-card">
        <h3>Total Active Children</h3>
        <p>{{ totalActiveChildren }}</p>
      </div>
      <div class="info-card">
        <h3>Completed Goals (School-wide)</h3>
        <p>{{ completedGoalsSchoolWide }}</p>
      </div>
    </div>

    <div class="content-card">
      <h3 class="text-xl font-semibold mb-4">User Role Distribution</h3>
      <div class="chart-placeholder">
        [Chart: Pie chart showing distribution of Child, Parent, Teacher, Admin users]
         <img src="https://wac-cdn.atlassian.com/dam/jcr:978f9f05-19ee-47d5-a9a9-a768a601a61b/pie-chart-example-1.png?cdnVersion=2806" alt="Monthly Spending Trends Chart" width="1000" height="300">
     
      </div>
    </div>

    <div class="content-card">
      <h3 class="text-xl font-semibold mb-4">Platform Activity Trends</h3>
      <div class="chart-placeholder">
        [Chart: Line chart showing daily/weekly/monthly active users or login trends]
       <img src="https://sta.laits.utexas.edu/wp-content/uploads/files/charts.png" alt="Monthly Spending Trends Chart" width="1000" height="300">
     
      </div>
    </div>

    <div class="content-card">
      <h3 class="text-xl font-semibold mb-4">Recent System Events</h3>
      <ul class="list-none p-0 m-0">
        <li v-for="event in recentSystemEvents" :key="event.id" 
            class="flex justify-between items-center py-3 border-b border-gray-200 last:border-b-0">
          <div class="flex items-center gap-3">
            <span class="text-gray-700 font-medium">{{ event.description }}</span>
          </div>
          <span class="text-sm text-gray-500">{{ event.date }}</span>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AdminHomeView',
  data() {
    return {
      totalUsers: 150,
      activeSchools: 10, 
      totalActiveChildren: 1000, 
      completedGoalsSchoolWide: 500,
      recentSystemEvents: [
        {
          id: 1,
          description: 'New school "Vidya mandir" registered',
          date: '2024-06-25'
        },
        {
          id: 2,
          description: 'Teacher Sneha created 3 new activities',
          date: '2024-06-24'
        },
        {
          id: 3,
          description: 'Parent #3456 updated child\'s allowance settings',
          date: '2024-06-23'
        }
      ]
    };
  }
};
</script>

<style scoped>
/* Scoped styles specific to AdminHomeView if needed */
.chart-placeholder {
  height: 250px;
  background: #f3f4f6;
  border-radius: 0.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #6b7280;
  font-style: italic;
  margin-bottom: 1rem;
}
</style>
