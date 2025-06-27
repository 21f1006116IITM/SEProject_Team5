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
          <!-- Icon for Home -->
        <img :src="require('@/assets/home-page.png')" alt="home" class="child-logo-images" />

          Home
        </button>
        <button
          class="nav-item"
          :class="{ 'active': currentDashboardView === 'goals' }"
          @click="changeDashboardView('goals')"
        >
          <!-- Icon for Goals (e.g., target or piggy bank) -->
            <img :src="require('@/assets/target.png')" alt="goals" class="child-logo-images" />

          Goals
        </button>
        <button
          class="nav-item"
          :class="{ 'active': currentDashboardView === 'spends' }"
          @click="changeDashboardView('spends')"
        >
          <!-- Icon for Spends (e.g., wallet or receipt) -->
           <img :src="require('@/assets/spending.png')" alt="spends" class="child-logo-images" />

          Spends
        </button>
        <button
          class="nav-item"
          :class="{ 'active': currentDashboardView === 'pocketMoney' }"
          @click="changeDashboardView('pocketMoney')"
        >
          <!-- Icon for Pocket Money (e.g., money bag) -->
          <img :src="require('@/assets/wallet.png')" alt="pocket money" class="child-logo-images" />
          Pocket Money
        </button>
        <button
          class="nav-item"
          :class="{ 'active': currentDashboardView === 'challenges' }"
          @click="changeDashboardView('challenges')"
        >
          <!-- Icon for Challenges (e.g., trophy or target) -->
          <img :src="require('@/assets/goal.png')" alt="challenges" class="child-logo-images" />
          Challenges
        </button>
        <button class="logout-button" @click="$emit('navigate', 'landing')">
        <!-- Icon for Logout -->
        <img :src="require('@/assets/logout.png')" alt="spends" class="child-logo-images" />
        Logout
      </button>
      </nav>
      
    </aside>

    <!-- Main Content Area -->
    <div class="dashboard-content">
      <template v-if="currentDashboardView === 'home'">
        <HomeView />
      </template>
      <template v-else-if="currentDashboardView === 'goals'">
        <GoalsView />
      </template>
      <template v-else-if="currentDashboardView === 'spends'">
        <SpendsView />
      </template>
      <template v-else-if="currentDashboardView === 'pocketMoney'">
        <PocketMoneyView />
      </template>
      <template v-else-if="currentDashboardView === 'challenges'">
        <ChallengesView />
      </template>
    </div>
  </div>
</template>

<script>
import HomeView from './Dashboard/HomeView.vue';
import GoalsView from './Dashboard/GoalsView.vue';
import SpendsView from './Dashboard/SpendsView.vue';
import PocketMoneyView from './Dashboard/PocketMoneyView.vue';
import ChallengesView from './Dashboard/ChallengesView.vue';

export default {
  name: 'ChildDashboard',
  components: {
    HomeView,
    GoalsView,
    SpendsView,
    PocketMoneyView,
    ChallengesView
  },
  emits: ['navigate'],
  data() {
    return {
      currentDashboardView: 'home' // Default view for the dashboard
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
