<template>
  <div class="container-base font-inter">
    <!-- Header (always visible) -->
    <header class="header-base">
      <div class="logo-section-base">
        <img :src="require('./assets/pig-logo.png')" alt="Logo" class="logo-img-base" />
        <h1 class="app-title-base cursor-pointer" @click="goToPage('landing')">PennyWise</h1>
      </div>
      <div class="auth-buttons-base">
        <button class="btn-base btn-login-base" @click="goToPage('login')">Login</button>
        <button class="btn-base btn-signup-base" @click="goToPage('signup')">Sign Up</button>
      </div>
    </header>

    <!-- Main Content Area - Conditional Rendering -->
    <main class="flex-grow flex flex-col items-center justify-center w-full">
      <template v-if="currentPage === 'landing'">
        <LandingPage @navigate="goToPage" />
      </template>
      <template v-else-if="currentPage === 'signup'">
        <AuthPage type="signup" @navigate="handleAuthNavigate" />
      </template>
      <template v-else-if="currentPage === 'login'">
        <AuthPage type="login" @navigate="handleAuthNavigate" />
      </template>
      <template v-else-if="currentPage === 'childDashboard'">
        <ChildDashboard @navigate="goToPage" />
      </template>
      <template v-else-if="currentPage === 'parentDashboard'">
        <ParentDashboard @navigate="goToPage" />
      </template>
      <template v-else-if="currentPage === 'teacherDashboard'">
        <TeacherDashboard @navigate="goToPage" />
      </template>
    </main>

    <!-- Optional Footer Placeholder if needed -->
    <footer class="h-4"></footer>
  </div>
</template>

<script>
import LandingPage from './components/LandingPage.vue';
import AuthPage from './components/AuthPage.vue';
import ChildDashboard from './components/ChildDashboard.vue';
import ParentDashboard from './components/ParentDashboard.vue';
import TeacherDashboard from './components/TeacherDashboard.vue';

export default {
  name: 'App',
  components: {
    LandingPage,
    AuthPage,
    ChildDashboard,
    ParentDashboard,
    TeacherDashboard
  },
  data() {
    return {
      currentPage: 'landing',
      loggedInUserRole: null
    };
  },
  methods: {
    handleAuthNavigate(pageName, role = null) {
      if (pageName === 'dashboard') {
        this.loggedInUserRole = role;
        if (role === 'Child') {
          this.currentPage = 'childDashboard';
        } else if (role === 'Parent') {
          this.currentPage = 'parentDashboard';
        } else if (role === 'Teacher') {
          this.currentPage = 'teacherDashboard';
        }
      } else {
        this.currentPage = pageName;
        this.loggedInUserRole = null;
      }
    },
    goToPage(pageName) {
      this.currentPage = pageName;
      this.loggedInUserRole = null;
    }
  }
};
</script>

<style>
#app {
  font-family: 'Inter', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
</style>
