<template>
  <div class="allowances-view w-full">
    <h2 class="dashboard-header">Manage Allowances</h2>

    <div class="button-group-top-right">
      <button class="btn-add" @click="showSendAllowanceForm = true">Send Allowance</button>
    </div>

    <!-- Send Allowance Form -->
    <div v-if="showSendAllowanceForm" class="form-section mb-6 mx-auto">
      <h3 class="form-section-title">Send Allowance</h3>
      <form @submit.prevent="sendAllowance">
        <div class="form-group-dashboard">
          <label for="childSelect" class="form-label-dashboard">Select Child</label>
          <select id="childSelect" v-model="newAllowance.childId" class="form-input-dashboard" required>
            <option value="">Choose a child</option>
            <option v-for="child in children" :key="child.id" :value="child.id">{{ child.name }}</option>
          </select>
        </div>
        <div class="form-group-dashboard">
          <label for="amount" class="form-label-dashboard">Amount</label>
          <input type="number" id="amount" v-model.number="newAllowance.amount" class="form-input-dashboard" required />
        </div>
        <div class="form-group-dashboard">
          <label for="description" class="form-label-dashboard">Description</label>
          <input type="text" id="description" v-model="newAllowance.description" class="form-input-dashboard" />
        </div>
        <button type="submit" class="form-submit-button-dashboard">Send Allowance</button>
        <button type="button" @click="cancelSendAllowance" class="form-submit-button-dashboard mt-2 bg-gray-300 text-gray-800 hover:bg-gray-400">Cancel</button>
      </form>
    </div>

    <div class="card-grid-dashboard">
      <div v-for="(allowance, index) in allowances" :key="index" class="card-item-dashboard">
        <h4 class="flex items-center gap-2">
          <img :src="require('@/assets/wallet.png')" alt="allowance" class="content-logo" />
          {{ allowance.childName }}
        </h4>
        <p class="text-sm text-gray-500 mb-2">{{ allowance.description }}</p>
        <p class="font-semibold text-lg text-green-600">Amount: ₹{{ allowance.amount }}</p>
        <p class="text-sm text-gray-500 mt-2">Date: {{ allowance.date }}</p>
        <div class="actions">
          <button class="btn-edit" @click="editAllowance(index)">Edit</button>
          <button class="btn-delete" @click="deleteAllowance(index)">Delete</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AllowancesView',
  data() {
    return {
      showSendAllowanceForm: false,
      newAllowance: {
        childId: '',
        amount: 0,
        description: ''
      },
      children: [
        { id: 1, name: 'Spriha Mishra' },
        { id: 2, name: 'Kalkin Mishra' }
      ],
      allowances: [
        {
          childName: 'Spriha Mishra',
          amount: 500,
          description: 'Weekly allowance',
          date: '2024-06-25'
        },
        {
          childName: 'Kalkin Mishra',
          amount: 300,
          description: 'Chore completion bonus',
          date: '2024-06-24'
        }
      ]
    };
  },
  methods: {
    sendAllowance() {
      const selectedChild = this.children.find(c => c.id === this.newAllowance.childId);
      this.allowances.push({
        childName: selectedChild.name,
        amount: this.newAllowance.amount,
        description: this.newAllowance.description,
        date: new Date().toISOString().split('T')[0]
      });
      this.resetAllowanceForm();
      this.showSendAllowanceForm = false;
      alert('Allowance sent successfully!');
    },
    cancelSendAllowance() {
      this.showSendAllowanceForm = false;
      this.resetAllowanceForm();
    },
    resetAllowanceForm() {
      this.newAllowance = {
        childId: '',
        amount: 0,
        description: ''
      };
    },
    editAllowance(index) {
      console.log('Editing allowance:', this.allowances[index]);
    },
    deleteAllowance(index) {
      if (confirm('Are you sure you want to delete this allowance record?')) {
        this.allowances.splice(index, 1);
        alert('Allowance record deleted successfully!');
      }
    }
  }
};
</script>