<template>
  <div class="children-management-view w-full">
    <h2 class="dashboard-header">Manage Children</h2>

    <div class="button-group-top-right">
      <button class="btn-add" @click="showAddChildForm = true">Add Child</button>
    </div>

    <!-- Add Child Form -->
    <div v-if="showAddChildForm" class="form-section mb-6 mx-auto">
      <h3 class="form-section-title">Add New Child</h3>
      <form @submit.prevent="addChild">
        <div class="form-group-dashboard">
          <label for="childName" class="form-label-dashboard">Child Name</label>
          <input type="text" id="childName" v-model="newChild.name" class="form-input-dashboard" required />
        </div>
        <div class="form-group-dashboard">
          <label for="childClass" class="form-label-dashboard">Class</label>
          <input type="text" id="childClass" v-model="newChild.class" class="form-input-dashboard" required />
        </div>
        <div class="form-group-dashboard">
          <label for="initialBalance" class="form-label-dashboard">Initial Balance</label>
          <input type="number" id="initialBalance" v-model.number="newChild.balance" class="form-input-dashboard" />
        </div>
        <button type="submit" class="form-submit-button-dashboard">Add Child</button>
        <button type="button" @click="cancelAddChild" class="form-submit-button-dashboard mt-2 bg-gray-300 text-gray-800 hover:bg-gray-400">Cancel</button>
      </form>
    </div>

    <div class="card-grid-dashboard">
      <div v-for="(child, index) in children" :key="index" class="card-item-dashboard">
        <h4 class="flex items-center gap-2">
          <img :src="require('@/assets/target.png')" alt="child" class="content-logo" />
          {{ child.name }}
        </h4>
        <p class="text-sm text-gray-500 mb-2">{{ child.class }}</p>
        <p class="font-semibold text-lg text-green-600">Balance: ₹{{ child.balance }}</p>
        <p class="text-sm text-gray-500 mt-2">Active Goals: {{ child.activeGoals }}</p>
        <div class="actions">
          <button class="btn-edit" @click="viewChild(index)">View</button>
          <button class="btn-delete" @click="sendAllowance(index)">Send Allowance</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ChildrenManagementView',
  data() {
    return {
      showAddChildForm: false,
      newChild: {
        name: '',
        class: '',
        balance: 0,
        activeGoals: 0
      },
      children: [
        {
          name: 'Spriha Mishra',
          class: '5th Grade',
          balance: 1200,
          activeGoals: 3
        },
        {
          name: 'Kalkin Mishra',
          class: '3rd Grade',
          balance: 800,
          activeGoals: 2
        }
      ]
    };
  },
  methods: {
    addChild() {
      this.children.push({ ...this.newChild });
      this.resetNewChildForm();
      this.showAddChildForm = false;
      alert('Child added successfully!');
    },
    cancelAddChild() {
      this.showAddChildForm = false;
      this.resetNewChildForm();
    },
    resetNewChildForm() {
      this.newChild = {
        name: '',
        class: '',
        balance: 0,
        activeGoals: 0
      };
    },
    viewChild(index) {
      // Implementation for viewing child details
      console.log('Viewing child:', this.children[index]);
    },
    sendAllowance(index) {
      // Implementation for sending allowance
      console.log('Sending allowance to:', this.children[index].name);
    }
  }
};
</script>

<style scoped>
/* Scoped styles specific to ChildrenManagementView */
</style>
