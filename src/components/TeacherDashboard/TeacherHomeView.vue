<template>
  <div class="teacher-home-view">
    <h2 class="dashboard-header">Teacher Dashboard</h2>
    <p class="text-gray-600 mb-6">Manage your classroom financial literacy program.</p>

    <div class="info-cards-grid">
      <div class="info-card">
        <h3>Total Students</h3>
        <p>{{ students.length }}</p>
      </div>
      <div class="info-card">
        <h3>Active Challenges</h3>
        <p>{{ activeChallenges }}</p>
      </div>
      <div class="info-card">
        <h3>Completion Rate</h3>
        <p>{{ completionRate }}%</p>
      </div>
    </div>

    <div class="content-card">
      <h3 class="text-xl font-semibold mb-4">Class Progress Overview</h3>
      <div class="chart-placeholder">
        <!-- [Placeholder: Student Progress Chart] -->
        <img src="https://www.iseesystems.com/resources/help/v3/Content/Resources/images/placeholders06.png" alt="Class Progress Chart" width="1000" height="300" class="hidden">
      </div>
    </div>

    <div class="content-card">
      <h3 class="text-xl font-semibold mb-4">Top Performers</h3>
      <div class="students-grid">
        <div v-for="student in topStudents" :key="student.id" class="student-card">
          <h4>{{ student.name }}</h4>
          <div class="student-stats">
            <span class="stat-item">Goals: {{ student.completedGoals }}</span>
            <span class="stat-item">Score: {{ student.score }}</span>
          </div>
        </div>
      </div>
    </div>

    <div class="content-card">
      <h3 class="text-xl font-semibold mb-4">Recent Class Activities</h3>
      <ul class="list-none p-0 m-0">
        <li v-for="activity in recentActivities" :key="activity.id" 
            class="flex justify-between items-center py-3 border-b border-gray-200 last:border-b-0">
          <div class="flex items-center gap-3">
            <span class="text-gray-700 font-medium">{{ activity.description }}</span>
          </div>
          <span class="text-sm text-gray-500">{{ activity.date }}</span>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TeacherHomeView',
  data() {
    return {
      students: [
        { id: 1, name: 'Spriha Mishra', completedGoals: 5, score: 95 },
        { id: 2, name: 'Kalkin Mishra', completedGoals: 3, score: 87 },
        { id: 3, name: 'Ram Pandey', completedGoals: 4, score: 92 },
      ],
      activeChallenges: 3,
      recentActivities: [
        {
          id: 1,
          description: 'New savings challenge assigned to class',
          date: '2024-06-25'
        },
        {
          id: 2,
          description: 'Spriha completed budgeting exercise',
          date: '2024-06-24'
        }
      ]
    };
  },
  computed: {
    topStudents() {
      return this.students.slice().sort((a, b) => b.score - a.score).slice(0, 3);
    },
    completionRate() {
      if (this.students.length === 0) return 0;
      const totalGoals = this.students.reduce((sum, student) => sum + student.completedGoals, 0);
      const maxPossibleGoals = this.students.length * 5; // Assuming 5 goals per student
      return Math.round((totalGoals / maxPossibleGoals) * 100);
    }
  }
};
</script>

<style scoped>
.students-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1rem;
}

.student-card {
  background: white;
  border-radius: 0.5rem;
  padding: 1rem;
  border: 1px solid #e5e7eb;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.student-stats {
  display: flex;
  gap: 1rem;
  margin-top: 0.5rem;
}

.stat-item {
  font-size: 0.875rem;
  color: #6b7280;
}
</style>
