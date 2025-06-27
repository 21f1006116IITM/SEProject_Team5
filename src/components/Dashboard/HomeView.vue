<template>
  <div class="home-view">
    <h2 class="dashboard-header">Welcome, Future Saver!</h2>
    <p class="text-gray-600 mb-6">Here's a quick overview of your financial journey.</p>

    <div class="info-cards-grid">
      <div class="info-card">
        <h3>Total Pocket Money</h3>
        <p>₹1500</p>
      </div>
      <div class="info-card">
        <h3>Goals Progress</h3>
        <p>75% Complete</p>
      </div>
      <div class="info-card">
        <h3>This Week's Spend</h3>
        <p>₹350</p>
      </div>
    </div>

    <div class="content-card">
      <h3 class="text-xl font-semibold mb-4">Goal Statistics Over Time</h3>
      <div class="chart-placeholder">
        <img src="https://www.iseesystems.com/resources/help/v3/Content/Resources/images/placeholders06.png" alt="Goal Stats Chart" width="1000" height="300" class="hidden">
        <!-- [Placeholder: Bar Chart showing Goal Progress over Months]
        <img src="https://placehold.co/600x250/E2E8F0/64748B?text=Goal+Stats+Chart" alt="Goal Stats Chart Placeholder" class="hidden"> -->
      </div>
    </div>

    <div class="content-card">
      <h3 class="text-xl font-semibold mb-4">Pocket Money & Spend Trends</h3>
      <div class="chart-placeholder">
        <img src="https://sta.laits.utexas.edu/wp-content/uploads/files/charts.png" alt="Income vs Spend Chart" width="1000" height="300">
        <!-- [Placeholder: Line Chart showing Pocket Money Income vs. Spends]
        <img src="https://placehold.co/600x250/E2E8F0/64748B?text=Income+Vs+Spend+Chart" alt="Income vs Spend Chart Placeholder" class="hidden"> -->
      </div>
    </div>

    <div class="content-card">
      <h3 class="text-xl font-semibold mb-4">Recent Activity</h3>
      <ul class="list-none p-0 m-0">
        <li class="flex justify-between items-center py-3 border-b border-gray-200 last:border-b-0">
          <div class="flex items-center gap-3">
            <span class="text-gray-700 font-medium">Received Weekly Pocket Money</span>
          </div>
          <span class="text-green-600 font-semibold">+₹500</span>
        </li>
        <li class="flex justify-between items-center py-3 border-b border-gray-200 last:border-b-0">
          <div class="flex items-center gap-3">
            
            <span class="text-gray-700 font-medium">Bought a Comic Book</span>
          </div>
          <span class="text-red-600 font-semibold">-₹120</span>
        </li>
        <li class="flex justify-between items-center py-3 border-b border-gray-200 last:border-b-0">
          <div class="flex items-center gap-3">
            
            <span class="text-gray-700 font-medium">Added to Bicycle Goal</span>
          </div>
          <span class="text-blue-600 font-semibold">+₹100</span>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
};
</script>

<style scoped>
/* Scoped styles specific to HomeView if needed. */
</style>
