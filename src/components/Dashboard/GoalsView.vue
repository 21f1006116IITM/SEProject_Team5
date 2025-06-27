<template>
  <div class="goals-view w-full">
    <h2 class="dashboard-header">My Savings Goals</h2>

    <div class="button-group-top-right">
      <button class="btn-add" @click="showAddGoalForm = true">Add Saving Goal</button>
    </div>

    <!-- Add Goal Form (conditionally rendered) -->
    <div v-if="showAddGoalForm" class="form-section mb-6 mx-auto">
      <h3 class="form-section-title">Add Your Savings Goals</h3>
      <form @submit.prevent="addGoal">
        <div class="form-group-dashboard">
          <label for="newGoalName" class="form-label-dashboard">Your Goal Name</label>
          <input type="text" id="newGoalName" v-model="newGoal.name" class="form-input-dashboard" placeholder="e.g., New Bicycle" required />
        </div>
        <div class="form-group-dashboard">
          <label for="newGoalDescription" class="form-label-dashboard">Goal Description</label>
          <textarea id="newGoalDescription" v-model="newGoal.description" class="form-input-dashboard" rows="3" placeholder="e.g., For riding to school with friends"></textarea>
        </div>
        <div class="form-row-dashboard">
          <div class="form-group-dashboard">
            <label for="newGoalAmount" class="form-label-dashboard">Goal Amount in INR</label>
            <input type="number" id="newGoalAmount" v-model.number="newGoal.targetAmount" class="form-input-dashboard" placeholder="e.g., 1000" required />
          </div>
          <div class="form-group-dashboard">
            <label for="newGoalDate" class="form-label-dashboard">Goal Achieve Date</label>
            <input type="date" id="newGoalDate" v-model="newGoal.deadline" class="form-input-dashboard" required />
          </div>
        </div>
        <button type="submit" class="form-submit-button-dashboard">Add Saving Goal</button>
        <button type="button" @click="showAddGoalForm = false" class="form-submit-button-dashboard mt-2 bg-gray-300 text-gray-800 hover:bg-gray-400">Cancel</button>
      </form>
    </div>

    <!-- Edit Goal Form (conditionally rendered) -->
    <div v-if="showEditGoalForm" class="form-section mb-6 mx-auto">
      <h3 class="form-section-title">Edit the Goal</h3>
      <form @submit.prevent="updateGoal">
        <div class="form-group-dashboard">
          <label for="editGoalName" class="form-label-dashboard">Name of Goal</label>
          <input type="text" id="editGoalName" v-model="editFormData.name" class="form-input-dashboard" required />
        </div>
        <div class="form-group-dashboard">
          <label for="editGoalAmount" class="form-label-dashboard">Amount</label>
          <input type="number" id="editGoalAmount" v-model.number="editFormData.targetAmount" class="form-input-dashboard" required />
        </div>
        <div class="form-group-dashboard">
          <label for="editGoalDescription" class="form-label-dashboard">Description</label>
          <textarea id="editGoalDescription" v-model="editFormData.description" class="form-input-dashboard" rows="3"></textarea>
        </div>
        <div class="form-group-dashboard">
          <label for="editGoalDate" class="form-label-dashboard">Date</label>
          <input type="date" id="editGoalDate" v-model="editFormData.deadline" class="form-input-dashboard" required />
        </div>
        <button type="submit" class="form-submit-button-dashboard">Submit</button>
        <button type="button" @click="cancelEdit" class="form-submit-button-dashboard mt-2 bg-gray-300 text-gray-800 hover:bg-gray-400">Cancel</button>
      </form>
    </div>


    <div class="card-grid-dashboard">
      <div v-for="(goal, index) in goals" :key="index" class="card-item-dashboard">
        <h4 class="flex items-center gap-2">
          <img :src="require('@/assets/target.png')" alt="targets" class="content-logo" />
          {{ goal.name }}
        </h4>
        <p class="text-sm text-gray-500 mb-2">{{ goal.description }}</p>
        <p class="font-semibold text-lg text-green-600">₹{{ goal.currentAmount }} / ₹{{ goal.targetAmount }}</p>
        <div class="progress-bar-container mt-2">
          <div class="progress-bar-fill" :style="{ width: (goal.currentAmount / goal.targetAmount * 100) + '%' }"></div>
        </div>
        <p class="text-sm text-gray-500 mt-2">Deadline: {{ goal.deadline }}</p>
        <div class="actions">
          <button class="btn-edit" @click="editGoal(index)">Edit</button>
          <button class="btn-delete" @click="deleteGoal(index)">Delete</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'GoalsView',
  data() {
    return {
      showAddGoalForm: false,
      showEditGoalForm: false,
      editingIndex: -1,
      newGoal: {
        name: '',
        description: '',
        targetAmount: 0,
        currentAmount: 0,
        deadline: ''
      },
      editFormData: {
        name: '',
        description: '',
        targetAmount: 0,
        deadline: ''
      },
      goals: [
        { name: 'New Bicycle', description: 'For riding to school', targetAmount: 1000, currentAmount: 650, deadline: '2025-12-25' },
        { name: 'Video Game', description: 'Latest adventure game', targetAmount: 500, currentAmount: 200, deadline: '2024-11-15' },
        { name: 'New Shoes', description: 'Sport shoes for play', targetAmount: 800, currentAmount: 800, deadline: '2024-09-01' }
      ]
    };
  },
  methods: {
    addGoal() {
      this.goals.push({ ...this.newGoal });
      this.resetNewGoalForm();
      this.showAddGoalForm = false;
      alert('Goal added successfully!');
    },
    editGoal(index) {
      this.editingIndex = index;
      this.editFormData = { ...this.goals[index] }; // Copy data for editing
      this.showEditGoalForm = true;
    },
    updateGoal() {
      if (this.editingIndex !== -1) {
        // Update only the editable fields, keep currentAmount same
        this.goals[this.editingIndex].name = this.editFormData.name;
        this.goals[this.editingIndex].description = this.editFormData.description;
        this.goals[this.editingIndex].targetAmount = this.editFormData.targetAmount;
        this.goals[this.editingIndex].deadline = this.editFormData.deadline;
        
        this.showEditGoalForm = false;
        this.editingIndex = -1;
        alert('Goal updated successfully!');
      }
    },
    cancelEdit() {
      this.showEditGoalForm = false;
      this.editingIndex = -1;
      this.resetNewGoalForm(); // Clear any partial new goal data
    },
    deleteGoal(index) {
      if (confirm('Are you sure you want to delete this goal?')) {
        this.goals.splice(index, 1);
        alert('Goal deleted successfully!');
      }
    },
    resetNewGoalForm() {
      this.newGoal = {
        name: '',
        description: '',
        targetAmount: 0,
        currentAmount: 0,
        deadline: ''
      };
    }
  }
};
</script>

<style scoped>
/* Scoped styles specific to GoalsView if needed. */
</style>
