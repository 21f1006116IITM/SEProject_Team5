<template>
  <div class="dashboard-layout">
    <!-- Sidebar Navigation -->
    <aside class="sidebar">
      <nav class="sidebar-nav">
        <button
          class="nav-item"
          :class="{ 'active': currentDashboardView === 'home' }"
          @click="changeDashboardView('home')"
        >
          <img :src="require('@/assets/home-page.png')" alt="home" class="child-logo-images" />
          Dashboard
        </button>
        <button
          class="nav-item"
          :class="{ 'active': currentDashboardView === 'classroom' }"
          @click="changeDashboardView('classroom')"
        >
          <img :src="require('@/assets/classroom.png')" alt="classroom" class="child-logo-images" />
          Classroom
        </button>
        <button
          class="nav-item"
          :class="{ 'active': currentDashboardView === 'students' }"
          @click="changeDashboardView('students')"
        >
          <img :src="require('@/assets/students.png')" alt="students" class="child-logo-images" />
          Students
        </button>
        <button
          class="nav-item"
          :class="{ 'active': currentDashboardView === 'activities' }"
          @click="changeDashboardView('activities')"
        >
          <img :src="require('@/assets/activities.png')" alt="activities" class="child-logo-images" />
          Activities
        </button>
        <button
          class="nav-item"
          :class="{ 'active': currentDashboardView === 'reports' }"
          @click="changeDashboardView('reports')"
        >
          <img :src="require('@/assets/report.png')" alt="reports" class="child-logo-images" />
          Reports
        </button>
        <button class="logout-button" @click="$emit('navigate', 'landing')">
          <img :src="require('@/assets/logout.png')" alt="logout" class="child-logo-images" />
          Logout
        </button>
      </nav>
    </aside>

    <!-- Main Content Area -->
    <div class="dashboard-content">
      <template v-if="currentDashboardView === 'home'">
        <TeacherHomeView />
      </template>
      <template v-else-if="currentDashboardView === 'classroom'">
        <ClassroomView />
      </template>
      <template v-else-if="currentDashboardView === 'students'">
        <StudentsView />
      </template>
      <template v-else-if="currentDashboardView === 'activities'">
        <ActivitiesView />
      </template>
      <template v-else-if="currentDashboardView === 'reports'">
        <TeacherReportsView />
      </template>
    </div>
  </div>
</template>

<script>
import TeacherHomeView from './TeacherDashboard/TeacherHomeView.vue';
import ClassroomView from './TeacherDashboard/ClassroomView.vue';
import StudentsView from './TeacherDashboard/StudentsView.vue';
import ActivitiesView from './TeacherDashboard/ActivitiesView.vue';
import TeacherReportsView from './TeacherDashboard/TeacherReportsView.vue';

export default {
  name: 'TeacherDashboard',
  components: {
    TeacherHomeView,
    ClassroomView,
    StudentsView,
    ActivitiesView,
    TeacherReportsView
  },
  emits: ['navigate'],
  data() {
    return {
      currentDashboardView: 'home'
    };
  },
  methods: {
    changeDashboardView(view) {
      this.currentDashboardView = view;
    }
  }
};
</script>

<style scoped>
/* No specific scoped styles needed here, as global styles handle the look. */
</style>
