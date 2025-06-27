<template>
  <div class="page-container">
    <main class="content">
      <!-- Top section with title and picture -->
      <section class="hero-section">
        <div class="hero-text">
          <h1>
            Learn to <span class="highlight">Save</span>, <span class="highlight">Spend</span> & <span class="highlight">Grow Smart!</span>
          </h1>
          <p class="subtitle">
            Join PennyWise to explore money with super fun games and lessons, perfect for kids, parents, and teachers!
          </p>
          
          <div class="button-group">
            <button class="button signup-button" @click="$emit('navigate', 'signup', null)">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><line x1="19" y1="8" x2="19" y2="14"></line><line x1="22" y1="11" x2="16" y2="11"></line>
              </svg>
              <span>Start the Fun!</span>
            </button>
            <button class="button login-button" @click="$emit('navigate', 'login', null)">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4"></path><polyline points="10 17 15 12 10 7"></polyline><line x1="15" y1="12" x2="3" y2="12"></line>
              </svg>
              <span>Login & Play</span>
            </button>
          </div>
        </div>
        <div class="hero-image">
          <img :src="require('@/assets/piggy-bank-logo.jpg')" alt="Happy PennyWise Piggy" />
        </div>
      </section>

      <!-- "Who is it for?" section -->
      <section class="features-section">
        <h2>Who loves PennyWise?</h2>
        <div class="features-grid">
          <div class="card">
            <h3>For Little Savers</h3>
            <p>Fun goals, tracking money, and smart tips just for kids!</p>
          </div>
          <div class="card">
            <h3>For Super Parents</h3>
            <p>See progress, set allowances, and send happy messages securely!</p>
          </div>
          <div class="card">
            <h3>For Awesome Teachers</h3>
            <p>Ready-to-use classroom games, fun stats, and lesson plans!</p>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script>
export default {
  name: 'LandingPage',
  emits: ['navigate']
}
</script>

<style scoped>

:root {
  --primary-color: #7ED957; /* Bright Green */
  --secondary-color: #64B5F6; /* Sky Blue */
  --background-color: #FFD54F; /* Sunny Yellow */
  --text-color: #4A4A4A;
  --white-color: #FFFFFF;
}


.page-container {
  font-family: 'Inter', sans-serif;
  color: var(--text-color);
  background-color: var(--background-color);
  padding: 3rem 1rem;
}

.content {
  max-width: 1100px;
  margin: 0 auto;
}

/* --- Hero Section (Top Part) --- */
.hero-section {
  display: flex;
  flex-direction: column; /* Stacks image below text on mobile */
  align-items: center;
  text-align: center;
  gap: 2rem;
  margin-bottom: 4rem;
}

.hero-text h1 {
  font-size: 3rem;
  font-weight: 800;
  line-height: 1.2;
  margin-bottom: 1rem;
}

.hero-text .highlight {
  color: var(--primary-color);
}

.hero-text .subtitle {
  font-size: 1.25rem;
  color: #777;
  margin-bottom: 2rem;
  max-width: 600px; /* Keeps text from getting too wide */
  margin-left: auto;
  margin-right: auto;
}

.hero-image img {
  max-width: 100%;
  border-radius: 12px;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
}

/* --- Buttons --- */
.button-group {
  display: flex;
  flex-direction: column; /* Stacks buttons on mobile */
  gap: 1rem;
  align-items: center;
}

.button {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 1rem 2rem; /* Big and easy to click */
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--white-color); /* All button text is white */
  border: none;
  border-radius: 50px; /* Fun, pill-shaped buttons */
  cursor: pointer;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}

.button:hover {
  transform: translateY(-4px); /* A little "hop" effect */
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.25);
}

.button svg {
  stroke: var(--white-color); /* Make sure icon is white */
}

.signup-button {
  background-color: var(--secondary-color); /* Blue */
}

.login-button {
  background-color: var(--primary-color); /* Green */
}


.features-section {
  background-color: var(--white-color);
  border-radius: 12px;
  padding: 3rem 2rem;
  text-align: center;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

.features-section h2 {
  font-size: 2.5rem;
  font-weight: 800;
  color: var(--secondary-color);
  margin-bottom: 3rem;
}

.features-grid {
  display: grid;
  grid-template-columns: 1fr; /* 1 column on mobile */
  gap: 2rem;
}

.card {
  padding: 2rem;
  border-radius: 12px;
  transition: transform 0.2s ease;
}

.card:hover {
  transform: scale(1.05); /* Card grows a little on hover */
}

.card h3 {
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
}

.card:nth-child(1) { background-color: #E3F2FD; } /* Light Blue */
.card:nth-child(2) { background-color: #E8F5E9; } /* Light Green */
.card:nth-child(3) { background-color: #F3E5F5; } /* Light Purple */


/* --- Responsive Design for Bigger Screens --- */
@media (min-width: 768px) {
  .hero-section {
    flex-direction: row; /* Puts image next to text */
    text-align: left;
  }

  .hero-text { flex: 1; }
  .hero-image { flex: 1; }

  .hero-text .subtitle {
    margin-left: 0;
  }
  
  .button-group {
    flex-direction: row; /* Buttons side-by-side */
    justify-content: flex-start;
  }
  
  .features-grid {
    grid-template-columns: repeat(3, 1fr); /* 3 columns for cards */
  }
}
</style>
