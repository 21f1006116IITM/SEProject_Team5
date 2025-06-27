<template>
  <div class="challenges-view">
    <h2 class="dashboard-header">Challenges & Tips</h2>

    <div class="challenge-tip">

      <div>
        <h3>
          Tip of the Week
        </h3>
        <p>
          The 50-30-20 Rule for Kids! Try spending 50% on needs, 30% on wants, and save 20% for your goals. It's like having a money recipe! 🧑‍🍳
        </p>
      </div>
      <div>
        <img :src="require('@/assets/tips.png')" alt="Tips" class="piggy-bank-icon"  />
      </div>


    </div>

    <div class="challenge-weekly">
  <div class="text-content">
    <h3>Weekly Challenge</h3>
    <p class="font-semibold text-lg mb-2">Spend ₹50 less this week</p>
    <div class="progress-bar-container">
      <div class="progress-bar-fill" style="width: 40%;"></div>
    </div>
    <p class="text-sm text-gray-700 mt-2">Progress: ₹20 saved / ₹50 target</p>
  </div>

  <img :src="require('@/assets/weeklytask.png')" alt="Weekly Task" class="piggy-bank-icon" />
</div>

   <div class="challenge-past-tips">
  <div class="text-content">
    <h3>Past Tips</h3>
    <ul>
      <li>Compare prices before buying</li>
      <li>Keep a spending diary</li>
      <li>Save coins in a jar</li>
      <li>Ask "Do I need this or want this?"</li>
    </ul>
  </div>

  <img :src="require('@/assets/money.png')" alt="Past Tip" class="piggy-bank-icon" />
</div>

  </div>
</template>

<script>
export default {
  name: 'ChallengesView',
};
</script>

<style scoped>
/* Scoped styles specific to ChallengesView if needed. */
</style>
