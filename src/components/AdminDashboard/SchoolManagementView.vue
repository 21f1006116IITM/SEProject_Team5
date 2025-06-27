<template>
  <div class="school-management-view w-full">
    <h2 class="dashboard-header">School Management</h2>

    <div class="button-group-top-right">
      <button class="btn-add" @click="showAddSchoolForm = true">Add New School</button>
    </div>

    <!-- Add School Form -->
    <div v-if="showAddSchoolForm" class="form-section mb-6 mx-auto">
      <h3 class="form-section-title">Add New School</h3>
      <form @submit.prevent="addSchool">
        <div class="form-group-dashboard">
          <label for="schoolName" class="form-label-dashboard">School Name</label>
          <input type="text" id="schoolName" v-model="newSchool.name" class="form-input-dashboard" required />
        </div>
        <div class="form-group-dashboard">
          <label for="schoolLocation" class="form-label-dashboard">Location</label>
          <input type="text" id="schoolLocation" v-model="newSchool.location" class="form-input-dashboard" required />
        </div>
        <div class="form-group-dashboard">
          <label for="principalName" class="form-label-dashboard">Principal Name</label>
          <input type="text" id="principalName" v-model="newSchool.principal" class="form-input-dashboard" />
        </div>
        <button type="submit" class="form-submit-button-dashboard">Add School</button>
        <button type="button" @click="cancelAddSchool" class="form-submit-button-dashboard mt-2 bg-gray-300 text-gray-800 hover:bg-gray-400">Cancel</button>
      </form>
    </div>

    <div class="content-card">
      <h3 class="text-xl font-semibold mb-4">Registered Schools</h3>
      <table class="w-full border-collapse">
        <thead>
          <tr class="bg-gray-50">
            <th class="border p-2 text-left">School Name</th>
            <th class="border p-2 text-left">Location</th>
            <th class="border p-2 text-left">Principal</th>
            <th class="border p-2 text-left">Total Users</th>
            <th class="border p-2 text-left">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="school in schools" :key="school.id">
            <td class="border p-2">{{ school.name }}</td>
            <td class="border p-2">{{ school.location }}</td>
            <td class="border p-2">{{ school.principal || 'N/A' }}</td>
            <td class="border p-2">{{ school.totalUsers }}</td>
            <td class="border p-2">
              <button class="btn-edit-inline" @click="editSchool(school)">Edit</button>
              <button class="btn-delete-inline" @click="deleteSchool(school.id)">Delete</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SchoolManagementView',
  data() {
    return {
      showAddSchoolForm: false,
      newSchool: {
        name: '',
        location: '',
        principal: ''
      },
      schools: [
        { id: 1, name: 'Greenfield Public School', location: 'Delhi', principal: 'Mrs. Sharma', totalUsers: 500 },
{ id: 2, name: 'Sunrise International School', location: 'Mumbai', principal: 'Mr. Verma', totalUsers: 300 },
{ id: 3, name: 'Silver Oak High School', location: 'Bangalore', principal: 'Ms. Iyer', totalUsers: 450 },
{ id: 4, name: 'Lotus Valley School', location: 'Chennai', principal: 'Mr. Raghavan', totalUsers: 520 },
{ id: 5, name: 'Heritage International Academy', location: 'Hyderabad', principal: 'Mrs. Khan', totalUsers: 400 },
{ id: 6, name: 'Gyan Deep Public School', location: 'Lucknow', principal: 'Mr. Tripathi', totalUsers: 350 },
{ id: 7, name: 'Bright Future School', location: 'Ahmedabad', principal: 'Ms. Patel', totalUsers: 270 },
{ id: 8, name: 'Mount Glory School', location: 'Pune', principal: 'Mr. Kulkarni', totalUsers: 390 },
{ id: 9, name: 'Starlight Academy', location: 'Jaipur', principal: 'Mrs. Mehra', totalUsers: 320 },
{ id: 10, name: 'Riverdale Public School', location: 'Kolkata', principal: 'Mr. Banerjee', totalUsers: 480 }

        ]
    };
  },
  methods: {
    addSchool() {
      this.schools.push({ ...this.newSchool, id: Date.now(), totalUsers: 0 });
      this.resetNewSchoolForm();
      this.showAddSchoolForm = false;
      alert('School added successfully!');
    },
    cancelAddSchool() {
      this.showAddSchoolForm = false;
      this.resetNewSchoolForm();
    },
    resetNewSchoolForm() {
      this.newSchool = {
        name: '',
        location: '',
        principal: ''
      };
    },
    editSchool(school) {
      console.log('Editing school:', school);
      alert(`Editing school: ${school.name}`);
    },
    deleteSchool(schoolId) {
      if (confirm('Are you sure you want to delete this school? This will remove all associated users and data.')) {
        this.schools = this.schools.filter(school => school.id !== schoolId);
        alert('School deleted successfully!');
      }
    }
  }
};
</script>

<style scoped>
/* Scoped styles for buttons are already defined in UserManagementView.vue
   If you move these to a global stylesheet or component, you can remove them here. */
.btn-edit-inline, .btn-delete-inline {
  padding: 0.25rem 0.75rem;
  border-radius: 0.25rem;
  font-size: 0.875rem;
  margin-right: 0.5rem;
  border: none;
  cursor: pointer;
}

.btn-edit-inline {
  background-color: #3b82f6; /* blue-500 */
  color: white;
}

.btn-delete-inline {
  background-color: #ef4444; /* red-500 */
  color: white;
}
</style>
