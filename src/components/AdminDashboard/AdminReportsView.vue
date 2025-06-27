<template>
  <div class="admin-reports-view w-full">
    <h2 class="dashboard-header">System-wide Reports</h2>

    <div class="info-cards-grid mb-6">
      <div class="info-card">
        <h3>Total Goals Achieved</h3>
        <p>{{ totalGoalsAchieved }}</p>
      </div>
      <div class="info-card">
        <h3>Total Money Saved (All Children)</h3>
        <p>₹{{ totalMoneySaved }}</p>
      </div>
      <div class="info-card">
        <h3>Average Student Engagement</h3>
        <p>{{ averageStudentEngagement }}%</p>
      </div>
    </div>

    <div class="content-card">
      <h3 class="text-xl font-semibold mb-4">Financial Literacy Progress by School</h3>
      <div class="chart-placeholder">
        [Chart: Bar chart showing average financial literacy score per school]
        
      </div>
    </div>

    <div class="content-card">
      <h3 class="text-xl font-semibold mb-4">Top 5 Performing Schools (Goals Achieved)</h3>
      <table class="w-full border-collapse">
        <thead>
          <tr class="bg-gray-50">
            <th class="border p-2 text-left">Rank</th>
            <th class="border p-2 text-left">School Name</th>
            <th class="border p-2 text-left">Goals Achieved</th>
            <th class="border p-2 text-left">Avg. Savings per Child</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(school, index) in topSchools" :key="school.id">
            <td class="border p-2">{{ index + 1 }}</td>
            <td class="border p-2">{{ school.name }}</td>
            <td class="border p-2">{{ school.goalsAchieved }}</td>
            <td class="border p-2">₹{{ school.avgSavingsPerChild }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="content-card">
      <h3 class="text-xl font-semibold mb-4">User Growth Trends</h3>
      <div class="chart-placeholder">
        [Chart: Line chart showing new user registrations over time, broken down by role]
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AdminReportsView',
  data() {
    return {
      totalGoalsAchieved: 5000,
      totalMoneySaved: 1500000, // Example: 15 Lakhs
      averageStudentEngagement: 85, // Example percentage
      topSchools: [
        { id: 1, name: 'Sarasvati Vidya Mandir', goalsAchieved: 1200, avgSavingsPerChild: 1500 },
        { id: 2, name: 'Junior Highschool', goalsAchieved: 950, avgSavingsPerChild: 1200 },
        { id: 3, name: 'City Montessori', goalsAchieved: 800, avgSavingsPerChild: 1800 },
        { id: 4, name: 'Sunrise Academy', goalsAchieved: 700, avgSavingsPerChild: 1100 },
        { id: 5, name: 'Shanti Niketan', goalsAchieved: 650, avgSavingsPerChild: 1000 }
      ]
    };
  }
};
</script>

<style scoped>
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
