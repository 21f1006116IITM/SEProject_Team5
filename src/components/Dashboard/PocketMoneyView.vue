<template>
  <div class="pocket-money-view w-full">
    <h2 class="dashboard-header">My Pocket Money</h2>

    <div class="button-group-top-right">
      <button class="btn-add" @click="showAddPocketMoneyForm = true">Add Money Source</button>
    </div>

    <!-- Add Pocket Money Form (conditionally rendered) -->
    <div v-if="showAddPocketMoneyForm" class="form-section mb-6 mx-auto">
      <h3 class="form-section-title">Add Pocket Money Source</h3>
      <form @submit.prevent="addPocketMoney">
        <div class="form-group-dashboard">
          <label for="whereItIs" class="form-label-dashboard">Where is it from?</label>
          <input type="text" id="whereItIs" v-model="newPocketMoney.location" class="form-input-dashboard" placeholder="e.g., Piggy Bank, Wallet, Allowance" required />
        </div>
        <div class="form-group-dashboard">
          <label for="pmAmount" class="form-label-dashboard">Amount</label>
          <input type="number" id="pmAmount" v-model.number="newPocketMoney.amount" class="form-input-dashboard" placeholder="e.g., 500" required />
        </div>
        <div class="form-group-dashboard">
          <label for="pmDate" class="form-label-dashboard">Date</label>
          <input type="date" id="pmDate" v-model="newPocketMoney.date" class="form-input-dashboard" required />
        </div>
        <button type="submit" class="form-submit-button-dashboard">Add Pocket Money</button>
        <button type="button" @click="showAddPocketMoneyForm = false" class="form-submit-button-dashboard mt-2 bg-gray-300 text-gray-800 hover:bg-gray-400">Cancel</button>
      </form>
    </div>

    <!-- Edit Pocket Money Form (conditionally rendered) -->
    <div v-if="showEditPocketMoneyForm" class="form-section mb-6 mx-auto">
      <h3 class="form-section-title">Edit Pocket Money Entry</h3>
      <form @submit.prevent="updatePocketMoney">
        <div class="form-group-dashboard">
          <label for="editWhereItIs" class="form-label-dashboard">Where is it from?</label>
          <input type="text" id="editWhereItIs" v-model="editFormData.location" class="form-input-dashboard" required />
        </div>
        <div class="form-group-dashboard">
          <label for="editPmAmount" class="form-label-dashboard">Amount</label>
          <input type="number" id="editPmAmount" v-model.number="editFormData.amount" class="form-input-dashboard" required />
        </div>
        <div class="form-group-dashboard">
          <label for="editPmDate" class="form-label-dashboard">Date</label>
          <input type="date" id="editPmDate" v-model="editFormData.date" class="form-input-dashboard" required />
        </div>
        <button type="submit" class="form-submit-button-dashboard">Update Pocket Money</button>
        <button type="button" @click="cancelEdit" class="form-submit-button-dashboard mt-2 bg-gray-300 text-gray-800 hover:bg-gray-400">Cancel</button>
      </form>
    </div>

    <div class="piggy-bank-grid">
      <div v-for="(pm, index) in pocketMoneyEntries" :key="index" class="piggy-bank-card">
        <img :src="require('@/assets/wallet.png')" alt="pocket" class="piggy-bank-icon" />

        <h4>{{ pm.location }}</h4>
        <p class="text-xl font-bold text-purple-600">₹{{ pm.amount }}</p>
        <p class="text-sm text-gray-500">Last Added: {{ pm.date }}</p>
        <div class="actions">
          <button class="btn-edit" @click="editPocketMoney(index)">Edit</button>
          <button class="btn-delete" @click="deletePocketMoney(index)">Delete</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PocketMoneyView',
  data() {
    return {
      showAddPocketMoneyForm: false,
      showEditPocketMoneyForm: false, // Added for edit form
      editingIndex: -1, // Added for edit form
      newPocketMoney: {
        location: '',
        amount: 0,
        date: ''
      },
      editFormData: { // Added for edit form
        location: '',
        amount: 0,
        date: ''
      },
      pocketMoneyEntries: [
        { location: 'Piggy Bank', amount: 500, date: '2024-06-01' },
        { location: 'Wallet', amount: 300, date: '2024-06-10' }
      ]
    };
  },
  methods: {
    addPocketMoney() {
      this.pocketMoneyEntries.push({ ...this.newPocketMoney });
      this.resetNewPocketMoneyForm();
      this.showAddPocketMoneyForm = false;
      alert('Pocket money added!');
    },
    editPocketMoney(index) { // Method to open and populate edit form
      this.editingIndex = index;
      this.editFormData = { ...this.pocketMoneyEntries[index] };
      this.showEditPocketMoneyForm = true;
    },
    updatePocketMoney() { // Method to update pocket money entry
      if (this.editingIndex !== -1) {
        this.pocketMoneyEntries[this.editingIndex] = { ...this.editFormData };
        this.showEditPocketMoneyForm = false;
        this.editingIndex = -1;
        alert('Pocket money entry updated successfully!');
      }
    },
    cancelEdit() { // Method to cancel edit
      this.showEditPocketMoneyForm = false;
      this.editingIndex = -1;
      this.editFormData = { location: '', amount: 0, date: '' }; // Reset edit form data
    },
    deletePocketMoney(index) {
      if (confirm('Are you sure you want to delete this pocket money entry?')) {
        this.pocketMoneyEntries.splice(index, 1);
        alert('Pocket money entry deleted.');
      }
    },
    resetNewPocketMoneyForm() {
      this.newPocketMoney = {
        location: '',
        amount: 0,
        date: ''
      };
    }
  }
};
</script>

<style scoped>
/* Scoped styles specific to PocketMoneyView if needed. */
</style>
