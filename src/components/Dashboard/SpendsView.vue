<template>
  <div class="spends-view w-full">
    <h2 class="dashboard-header">My Spends</h2>

    <div class="button-group-top-right">
      <button class="btn-add" @click="showAddSpendForm = true">Note Spend</button>
    </div>

    <!-- Add Spend Form (conditionally rendered) -->
    <div v-if="showAddSpendForm" class="form-section mb-6 mx-auto">
      <h3 class="form-section-title">Add Your Spend</h3>
      <form @submit.prevent="addSpend">
        <div class="form-group-dashboard">
          <label for="spentOn" class="form-label-dashboard">Spent On (Item/Reason)</label>
          <input type="text" id="spentOn" v-model="newSpend.spentOn" class="form-input-dashboard" placeholder="e.g., Toy Car" required />
        </div>
        <div class="form-group-dashboard">
          <label for="spendAmount" class="form-label-dashboard">Amount</label>
          <input type="number" id="spendAmount" v-model.number="newSpend.amount" class="form-input-dashboard" placeholder="e.g., 200" required />
        </div>
        <div class="form-group-dashboard">
          <label for="spendDate" class="form-label-dashboard">Date</label>
          <input type="date" id="spendDate" v-model="newSpend.date" class="form-input-dashboard" required />
        </div>
        <button type="submit" class="form-submit-button-dashboard">Add Spend</button>
        <button type="button" @click="showAddSpendForm = false" class="form-submit-button-dashboard mt-2 bg-gray-300 text-gray-800 hover:bg-gray-400">Cancel</button>
      </form>
    </div>

    <!-- Edit Spend Form (conditionally rendered) -->
    <div v-if="showEditSpendForm" class="form-section mb-6 mx-auto">
      <h3 class="form-section-title">Edit Spend Record</h3>
      <form @submit.prevent="updateSpend">
        <div class="form-group-dashboard">
          <label for="editSpentOn" class="form-label-dashboard">Spent On (Item/Reason)</label>
          <input type="text" id="editSpentOn" v-model="editFormData.spentOn" class="form-input-dashboard" required />
        </div>
        <div class="form-group-dashboard">
          <label for="editSpendAmount" class="form-label-dashboard">Amount</label>
          <input type="number" id="editSpendAmount" v-model.number="editFormData.amount" class="form-input-dashboard" required />
        </div>
        <div class="form-group-dashboard">
          <label for="editSpendDate" class="form-label-dashboard">Date</label>
          <input type="date" id="editSpendDate" v-model="editFormData.date" class="form-input-dashboard" required />
        </div>
        <button type="submit" class="form-submit-button-dashboard">Update Spend</button>
        <button type="button" @click="cancelEdit" class="form-submit-button-dashboard mt-2 bg-gray-300 text-gray-800 hover:bg-gray-400">Cancel</button>
      </form>
    </div>

   <div class="spending-list">
    <div class="spending-item" v-for="(item, index) in spends" :key="index">
      <div class="description">
        <img :src="require('@/assets/spending.png')" alt="spendings" class="spending-icon" />
        <span>Spent on: {{ item.spentOn }}</span>
      </div>
      <div class="meta">
        <span class="date">Date: {{ item.date }}</span>
        <span class="amount">- ₹{{ item.amount }}</span>
      </div>
      <div class="actions">
        <button class="btn-edit" @click="editSpend(index)">Edit</button>
        <button class="btn-delete" @click="deleteSpend(index)">Delete</button>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
export default {
  name: 'SpendsView',
  data() {
    return {
      showAddSpendForm: false,
      showEditSpendForm: false, // Added for edit form
      editingIndex: -1, // Added for edit form
      newSpend: {
        spentOn: '',
        amount: 0,
        date: ''
      },
      editFormData: { // Added for edit form
        spentOn: '',
        amount: 0,
        date: ''
      },
      spends: [
        { spentOn: 'Toy Car', amount: 200, date: '2024-06-15' },
        { spentOn: 'Ice Cream', amount: 50, date: '2024-06-16' },
        { spentOn: 'Comic Book', amount: 120, date: '2024-06-17' }
      ]
    };
  },
  methods: {
    addSpend() {
      this.spends.push({ ...this.newSpend });
      this.resetNewSpendForm();
      this.showAddSpendForm = false;
      alert('Spend noted successfully!');
    },
    editSpend(index) { // Method to open and populate edit form
      this.editingIndex = index;
      this.editFormData = { ...this.spends[index] };
      this.showEditSpendForm = true;
    },
    updateSpend() { // Method to update spend record
      if (this.editingIndex !== -1) {
        this.spends[this.editingIndex] = { ...this.editFormData };
        this.showEditSpendForm = false;
        this.editingIndex = -1;
        alert('Spend record updated successfully!');
      }
    },
    cancelEdit() { // Method to cancel edit
      this.showEditSpendForm = false;
      this.editingIndex = -1;
      this.editFormData = { spentOn: '', amount: 0, date: '' }; // Reset edit form data
    },
    deleteSpend(index) {
      if (confirm('Are you sure you want to delete this spend record?')) {
        this.spends.splice(index, 1);
        alert('Spend record deleted.');
      }
    },
    resetNewSpendForm() {
      this.newSpend = {
        spentOn: '',
        amount: 0,
        date: ''
      };
    }
  }
};
</script>

<style scoped>
/* Scoped styles specific to SpendsView if needed. */
</style>
