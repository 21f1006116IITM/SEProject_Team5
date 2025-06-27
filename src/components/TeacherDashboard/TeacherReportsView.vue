<template>
  <div class="teacher-reports-view w-full">
    <h2 class="dashboard-header">Class Reports & Analytics</h2>

    <div class="info-cards-grid mb-6">
      <div class="info-card">
        <h3>Total Students</h3>
        <p>{{ totalStudents }}</p>
      </div>
      <div class="info-card">
        <h3>Average Class Score</h3>
        <p>{{ averageClassScore }}%</p>
      </div>
      <div class="info-card">
        <h3>Completion Rate</h3>
        <p>{{ completionRate }}%</p>
      </div>
    </div>

    <div class="content-card">
      <h3 class="text-xl font-semibold mb-4">Student Performance Overview</h3>
      <table class="w-full border-collapse">
        <thead>
          <tr class="bg-gray-50">
            <th class="border p-2 text-left">Student Name</th>
            <th class="border p-2 text-left">Class</th>
            <th class="border p-2 text-left">Score</th>
            <th class="border p-2 text-left">Goals Completed</th>
            <th class="border p-2 text-left">Status</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="student in studentPerformance" :key="student.id">
            <td class="border p-2">{{ student.name }}</td>
            <td class="border p-2">{{ student.class }}</td>
            <td class="border p-2">{{ student.score }}%</td>
            <td class="border p-2">{{ student.goalsCompleted }}</td>
            <td class="border p-2">
              <span :class="getStatusClass(student.score)">{{ getStatus(student.score) }}</span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="content-card">
      <h3 class="text-xl font-semibold mb-4">Activity Engagement</h3>
      <div class="chart-placeholder mb-4">
        <!-- [Chart: Student engagement across different activities] -->
        <img src="https://charts.livegap.com/2020/images/paper-en.png" alt="Engagement Chart" />
      </div>
      <div class="activity-stats-grid">
        <div v-for="activity in activityStats" :key="activity.id" class="activity-stat-card">
          <h4>{{ activity.name }}</h4>
          <div class="stat-details">
            <div class="stat-item">
              <span class="label">Participants:</span>
              <span class="value">{{ activity.participants }}</span>
            </div>
            <div class="stat-item">
              <span class="label">Completion Rate:</span>
              <span class="value">{{ activity.completionRate }}%</span>
            </div>
            <div class="stat-item">
              <span class="label">Average Score:</span>
              <span class="value">{{ activity.averageScore }}%</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="content-card">
      <h3 class="text-xl font-semibold mb-4">Financial Literacy Progress</h3>
      <div class="progress-grid">
        <div v-for="topic in topicProgress" :key="topic.id" class="topic-progress-card">
          <h4>{{ topic.name }}</h4>
          <div class="progress-bar">
            <div class="progress-fill" :style="{ width: topic.progress + '%' }"></div>
          </div>
          <p class="progress-text">{{ topic.progress }}% class average</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TeacherReportsView',
  data() {
    return {
      studentPerformance: [
        {
          id: 1,
          name: 'Spriha Mishra',
          class: '5th Grade',
          score: 95,
          goalsCompleted: 5
        },
        {
          id: 2,
          name: 'Kalkin Mishra',
          class: '5th Grade',
          score: 87,
          goalsCompleted: 3
        },
        {
          id: 3,
          name: 'Ram Pandey',
          class: '5th Grade',
          score: 92,
          goalsCompleted: 4
        },
        {
          id: 4,
          name: 'Lado Pandey',
          class: '5th Grade',
          score: 78,
          goalsCompleted: 2
        }
      ],
      activityStats: [
        {
          id: 1,
          name: 'Savings Challenge',
          participants: 28,
          completionRate: 85,
          averageScore: 88
        },
        {
          id: 2,
          name: 'Budgeting Quiz',
          participants: 30,
          completionRate: 92,
          averageScore: 85
        },
        {
          id: 3,
          name: 'Shopping Game',
          participants: 25,
          completionRate: 78,
          averageScore: 82
        }
      ],
      topicProgress: [
        {
          id: 1,
          name: 'Saving Money',
          progress: 88
        },
        {
          id: 2,
          name: 'Budgeting',
          progress: 75
        },
        {
          id: 3,
          name: 'Spending Wisely',
          progress: 82
        },
        {
          id: 4,
          name: 'Goal Setting',
          progress: 90
        }
      ]
    };
  },
  computed: {
    totalStudents() {
      return this.studentPerformance.length;
    },
    averageClassScore() {
      const total = this.studentPerformance.reduce((sum, student) => sum + student.score, 0);
      return Math.round(total / this.studentPerformance.length);
    },
    completionRate() {
      const totalGoals = this.studentPerformance.reduce((sum, student) => sum + student.goalsCompleted, 0);
      const maxPossibleGoals = this.studentPerformance.length * 5; // Assuming 5 goals per student
      return Math.round((totalGoals / maxPossibleGoals) * 100);
    }
  },
  methods: {
    getStatus(score) {
      if (score >= 90) return 'Excellent';
      if (score >= 80) return 'Good';
      if (score >= 70) return 'Satisfactory';
      return 'Needs Improvement';
    },
    getStatusClass(score) {
      if (score >= 90) return 'text-green-600 font-semibold';
      if (score >= 80) return 'text-blue-600 font-semibold';
      if (score >= 70) return 'text-yellow-600 font-semibold';
      return 'text-red-600 font-semibold';
    }
  }
};
</script>

<style scoped>
.activity-stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1rem;
}

.activity-stat-card {
  background: white;
  border-radius: 0.5rem;
  padding: 1rem;
  border: 1px solid #e5e7eb;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.stat-details {
  margin-top: 1rem;
}

.stat-item {
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.5rem;
}

.progress-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1rem;
}

.topic-progress-card {
  background: white;
  border-radius: 0.5rem;
  padding: 1rem;
  border: 1px solid #e5e7eb;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.progress-bar {
  width: 100%;
  height: 0.5rem;
  background: #e5e7eb;
  border-radius: 0.25rem;
  margin: 0.5rem 0;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background: #7c3aed;
  transition: width 0.3s ease;
}

.progress-text {
  font-size: 0.875rem;
  color: #6b7280;
  margin: 0;
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