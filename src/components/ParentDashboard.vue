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
          :class="{ 'active': currentDashboardView === 'children' }"
          @click="changeDashboardView('children')"
        >
          <img :src="require('@/assets/children.png')" alt="children" class="child-logo-images" />
          My Children
        </button>
        <button
          class="nav-item"
          :class="{ 'active': currentDashboardView === 'allowances' }"
          @click="changeDashboardView('allowances')"
        >
          <img :src="require('@/assets/allowances.png')" alt="allowances" class="child-logo-images" />
          Allowances
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
          :class="{ 'active': currentDashboardView === 'messages' }"
          @click="changeDashboardView('messages')"
        >
          <img :src="require('@/assets/message.png')" alt="messages" class="child-logo-images" />
          Messages
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
        <ParentHomeView />
      </template>
      <template v-else-if="currentDashboardView === 'children'">
        <ChildrenManagementView />
      </template>
      <template v-else-if="currentDashboardView === 'allowances'">
        <AllowancesView />
      </template>
      <template v-else-if="currentDashboardView === 'reports'">
        <ParentReportsView />
      </template>
      <template v-else-if="currentDashboardView === 'messages'">
        <ParentMessagesView />
      </template>
    </div>
  </div>
</template>

<script>
import ParentHomeView from './ParentDashboard/ParentHomeView.vue';
import ChildrenManagementView from './ParentDashboard/ChildrenManagementView.vue';
import AllowancesView from './ParentDashboard/AllowancesView.vue';
import ParentReportsView from './ParentDashboard/ParentReportsView.vue';
import ParentMessagesView from './ParentDashboard/ParentMessagesView.vue';

export default {
  name: 'ParentDashboard',
  components: {
    ParentHomeView,
    ChildrenManagementView,
    AllowancesView,
    ParentReportsView,
    ParentMessagesView
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
