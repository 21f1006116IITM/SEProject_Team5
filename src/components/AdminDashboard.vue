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
          :class="{ 'active': currentDashboardView === 'users' }"
          @click="changeDashboardView('users')"
        >
          <img :src="require('@/assets/users.png')" alt="users" class="child-logo-images" />
          Users
        </button>
        <button
          class="nav-item"
          :class="{ 'active': currentDashboardView === 'schools' }"
          @click="changeDashboardView('schools')"
        >
          <img :src="require('@/assets/school.png')" alt="schools" class="child-logo-images" />
          Schools
        </button>
        <button
          class="nav-item"
          :class="{ 'active': currentDashboardView === 'reports' }"
          @click="changeDashboardView('reports')"
        >
          <img :src="require('@/assets/report.png')" alt="reports" class="child-logo-images" />
          Reports
        </button>
        <button
          class="nav-item"
          :class="{ 'active': currentDashboardView === 'settings' }"
          @click="changeDashboardView('settings')"
        >
          <img :src="require('@/assets/settings.png')" alt="settings" class="child-logo-images" />
          Settings
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
        <AdminHomeView />
      </template>
      <template v-else-if="currentDashboardView === 'users'">
        <UserManagementView />
      </template>
      <template v-else-if="currentDashboardView === 'schools'">
        <SchoolManagementView />
      </template>
      <template v-else-if="currentDashboardView === 'reports'">
        <AdminReportsView />
      </template>
      <template v-else-if="currentDashboardView === 'settings'">
        <SystemSettingsView />
      </template>
    </div>
  </div>
</template>

<script>
import AdminHomeView from './AdminDashboard/AdminHomeView.vue';
import UserManagementView from './AdminDashboard/UserManagementView.vue';
import SchoolManagementView from './AdminDashboard/SchoolManagementView.vue';
import AdminReportsView from './AdminDashboard/AdminReportsView.vue';
import SystemSettingsView from './AdminDashboard/SystemSettingsView.vue';

export default {
  name: 'AdminDashboard',
  components: {
    AdminHomeView,
    UserManagementView,
    SchoolManagementView,
    AdminReportsView,
    SystemSettingsView
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
