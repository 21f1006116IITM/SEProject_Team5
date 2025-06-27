<template>
  <div class="main-landing">
    <img :src="require('@/assets/piggy-bank-logo.jpg')" alt="Piggy Bank" class="piggy-img-landing" />

    <h2 class="main-heading-landing">
      Learn to Save, Spend & Grow Smart!
    </h2>
    
    <p class="subtext-landing">
      Empower children with financial literacy through fun, interactive money management tools designed for kids, parents, and teachers.
    </p>
    
    <div class="action-buttons-landing">
      <button class="btn-action-landing btn-get-started-landing" @click="$emit('navigate', 'signup', null)">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
          <path d="M10.894 2.553a1 1 0 00-1.788 0l-7 14a1 1 0 001.169 1.409l.646-.285A10.435 10.435 0 0010 18c2.305 0 4.47-1.192 5.77-3.176l.647.285a1 1 0 001.168-1.409l-7-14z" />
        </svg>
        <span>Get Started Free</span>
      </button>
      <button class="btn-action-landing btn-watch-demo-landing" @click="$emit('navigate', 'login', null)">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd" />
        </svg>
        <span>Watch Demo</span>
      </button>
    </div>

    <div class="features-grid-landing">
      <div class="feature-card-landing">
        <div class="icon-wrapper-landing blue">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM12 10V6a2 2 0 00-2-2H6a2 2 0 00-2 2v4a2 2 0 002 2h4a2 2 0 002-2z" />
          </svg>
        </div>
        <h3 class="feature-title-landing">For Children</h3>
        <p class="feature-description-landing">Fun savings goals, expense tracking, and money tips</p>
      </div>
      <div class="feature-card-landing">
        <div class="icon-wrapper-landing green">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" d="M17 20h-4a2 2 0 01-2-2V8H5a2 2 0 00-2 2v10a2 2 0 002 2h14a2 2 0 002-2V10a2 2 0 00-2-2h-4V6a2 2 0 00-2-2H9a2 2 0 00-2 2v2m12 0H7" />
          </svg>
        </div>
        <h3 class="feature-title-landing">For Parents</h3>
        <p class="feature-description-landing">Monitor progress, set allowances, send encouragement</p>
      </div>
      <div class="feature-card-landing">
        <div class="icon-wrapper-landing purple">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
          </svg>
        </div>
        <h3 class="feature-title-landing">For Teachers</h3>
        <p class="feature-description-landing">Classroom activities, engagement analytics, curriculum</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LandingPage',
  emits: ['navigate'] // Declare the custom event this component emits
}
</script>

<style scoped>
/* Scoped styles (if any) specific to LandingPage. Vue will handle class hashing. */
</style>
