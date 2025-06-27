<template>
  <div class="system-settings-view w-full">
    <h2 class="dashboard-header">System Settings</h2>
    <p class="text-gray-600 mb-6">Configure application-wide settings and preferences.</p>

    <div class="content-card">
      <h3 class="text-xl font-semibold mb-4">General Settings</h3>
      <form @submit.prevent="saveGeneralSettings">
        <div class="form-group-dashboard">
          <label for="defaultCurrency" class="form-label-dashboard">Default Currency Symbol</label>
          <input type="text" id="defaultCurrency" v-model="settings.defaultCurrency" class="form-input-dashboard" />
        </div>
        <div class="form-group-dashboard">
          <label for="minPasswordLength" class="form-label-dashboard">Minimum Password Length</label>
          <input type="number" id="minPasswordLength" v-model.number="settings.minPasswordLength" class="form-input-dashboard" />
        </div>
        <div class="form-group-dashboard">
          <label for="enableRegistration" class="form-label-dashboard">Enable New User Registration</label>
          <input type="checkbox" id="enableRegistration" v-model="settings.enableRegistration" class="ml-2" />
        </div>
        <button type="submit" class="form-submit-button-dashboard">Save General Settings</button>
      </form>
    </div>

    <div class="content-card">
      <h3 class="text-xl font-semibold mb-4">Notification Settings</h3>
      <form @submit.prevent="saveNotificationSettings">
        <div class="form-group-dashboard">
          <label for="enableEmailNotifications" class="form-label-dashboard">Enable Email Notifications</label>
          <input type="checkbox" id="enableEmailNotifications" v-model="settings.enableEmailNotifications" class="ml-2" />
        </div>
        <div class="form-group-dashboard">
          <label for="weeklyReportEmails" class="form-label-dashboard">Send Weekly Performance Reports</label>
          <input type="checkbox" id="weeklyReportEmails" v-model="settings.weeklyReportEmails" class="ml-2" />
        </div>
        <button type="submit" class="form-submit-button-dashboard">Save Notification Settings</button>
      </form>
    </div>

    <div class="content-card">
      <h3 class="text-xl font-semibold mb-4">Data Management</h3>
      <button class="btn-delete-inline" @click="exportData">Export All Data</button>
      <button class="btn-delete-inline ml-4" @click="resetData">Reset Application Data (DANGER)</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SystemSettingsView',
  data() {
    return {
      settings: {
        defaultCurrency: '₹',
        minPasswordLength: 8,
        enableRegistration: true,
        enableEmailNotifications: true,
        weeklyReportEmails: true
      }
    };
  },
  methods: {
    saveGeneralSettings() {
      // Simulate API call to save settings
      console.log('Saving general settings:', this.settings);
      alert('General settings saved!');
    },
    saveNotificationSettings() {
      // Simulate API call to save settings
      console.log('Saving notification settings:', this.settings);
      alert('Notification settings saved!');
    },
    exportData() {
      // Simulate data export
      alert('Exporting data... (This would trigger a backend process)');
      console.log('Exporting all application data.');
    },
    resetData() {
      if (confirm('WARNING: This will permanently delete ALL application data. Are you absolutely sure?')) {
        alert('Application data reset initiated... (This would trigger a backend process)');
        console.log('Resetting all application data.');
      }
    }
  }
};
</script>

<style scoped>
/* Ensure any custom button styles are imported or defined here */
.btn-delete-inline {
  padding: 1rem 1rem;
  border-radius: 0.375rem;
  font-size: 1rem;
  border: none;
  cursor: pointer;
  background-color: #ef4444; /* red-500 */
  color: white;
  /* gap in buttons */
  margin-left: 0.5rem;
}
</style>
