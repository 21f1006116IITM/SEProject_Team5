<template>
  <div class="classroom-view w-full">
    <h2 class="dashboard-header">Classroom Management</h2>

    <div class="button-group-top-right">
      <button class="btn-add" @click="showCreateActivityForm = true">Create Activity</button>
    </div>

    <!-- Create Activity Form -->
    <div v-if="showCreateActivityForm" class="form-section mb-6 mx-auto">
      <h3 class="form-section-title">Create New Activity</h3>
      <form @submit.prevent="createActivity">
        <div class="form-group-dashboard">
          <label for="activityTitle" class="form-label-dashboard">Activity Title</label>
          <input type="text" id="activityTitle" v-model="newActivity.title" class="form-input-dashboard" required />
        </div>
        <div class="form-group-dashboard">
          <label for="activityDescription" class="form-label-dashboard">Description</label>
          <textarea id="activityDescription" v-model="newActivity.description" class="form-input-dashboard" rows="3"></textarea>
        </div>
        <div class="form-group-dashboard">
          <label for="activityType" class="form-label-dashboard">Activity Type</label>
          <select id="activityType" v-model="newActivity.type" class="form-input-dashboard" required>
            <option value="challenge">Challenge</option>
            <option value="quiz">Quiz</option>
            <option value="exercise">Exercise</option>
          </select>
        </div>
        <div class="form-group-dashboard">
          <label for="activityPoints" class="form-label-dashboard">Points</label>
          <input type="number" id="activityPoints" v-model.number="newActivity.points" class="form-input-dashboard" required />
        </div>
        <button type="submit" class="form-submit-button-dashboard">Create Activity</button>
        <button type="button" @click="cancelCreateActivity" class="form-submit-button-dashboard mt-2 bg-gray-300 text-gray-800 hover:bg-gray-400">Cancel</button>
      </form>
    </div>

    <div class="card-grid-dashboard">
      <div v-for="(activity, index) in activities" :key="index" class="card-item-dashboard">
        <h4 class="flex items-center gap-2">
          <img :src="require('@/assets/target.png')" alt="activity" class="content-logo" />
          {{ activity.title }}
        </h4>
        <p class="text-sm text-gray-500 mb-2">{{ activity.description }}</p>
        <p class="font-semibold text-lg text-blue-600">Type: {{ activity.type }}</p>
        <p class="text-sm text-gray-500 mt-2">Points: {{ activity.points }}</p>
        <p class="text-sm text-gray-500">Participants: {{ activity.participants }}</p>
        <div class="actions">
          <button class="btn-edit" @click="editActivity(index)">Edit</button>
          <button class="btn-delete" @click="deleteActivity(index)">Delete</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ClassroomView',
  data() {
    return {
      showCreateActivityForm: false,
      newActivity: {
        title: '',
        description: '',
        type: 'challenge',
        points: 0,
        participants: 0
      },
      activities: [
        {
          title: 'Weekly Savings Challenge',
          description: 'Save ₹50 this week',
          type: 'challenge',
          points: 10,
          participants: 25
        },
        {
          title: 'Budgeting Quiz',
          description: 'Test your budgeting knowledge',
          type: 'quiz',
          points: 15,
          participants: 28
        }
      ]
    };
  },
  methods: {
    createActivity() {
      this.activities.push({ ...this.newActivity });
      this.resetNewActivityForm();
      this.showCreateActivityForm = false;
      alert('Activity created successfully!');
    },
    cancelCreateActivity() {
      this.showCreateActivityForm = false;
      this.resetNewActivityForm();
    },
    resetNewActivityForm() {
      this.newActivity = {
        title: '',
        description: '',
        type: 'challenge',
        points: 0,
        participants: 0
      };
    },
    editActivity(index) {
      console.log('Editing activity:', this.activities[index]);
    },
    deleteActivity(index) {
      if (confirm('Are you sure you want to delete this activity?')) {
        this.activities.splice(index, 1);
        alert('Activity deleted successfully!');
      }
    }
  }
};
</script>

<style scoped>
/* Scoped styles specific to ClassroomView */
</style>
