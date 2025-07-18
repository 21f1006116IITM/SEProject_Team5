<template>
  <div class="user-management-view w-full">
    <h2 class="dashboard-header">User Management</h2>

    <div class="button-group-top-right">
      <button class="btn-add" @click="showAddUserForm = true">Add New User</button>
    </div>

    <!-- Add User Form -->
    <div v-if="showAddUserForm" class="form-section mb-6 mx-auto">
      <h3 class="form-section-title">Add New User</h3>
      <form @submit.prevent="addUser">
        <div class="form-group-dashboard">
          <label for="userName" class="form-label-dashboard">Name</label>
          <input type="text" id="userName" v-model="newUser.name" class="form-input-dashboard" required />
        </div>
        <div class="form-group-dashboard">
          <label for="userEmail" class="form-label-dashboard">Email</label>
          <input type="email" id="userEmail" v-model="newUser.email" class="form-input-dashboard" required />
        </div>
        <div class="form-group-dashboard">
          <label for="userRole" class="form-label-dashboard">Role</label>
          <select id="userRole" v-model="newUser.role" class="form-input-dashboard" required>
            <option value="">Select Role</option>
            <option value="child">Child</option>
            <option value="parent">Parent</option>
            <option value="teacher">Teacher</option>
            <option value="admin">Admin</option>
          </select>
        </div>
        <div class="form-group-dashboard">
          <label for="userSchool" class="form-label-dashboard">School</label>
          <select id="userSchool" v-model="newUser.school" class="form-input-dashboard">
            <option value="">Select School (Optional)</option>
            <option v-for="school in schools" :key="school.id" :value="school.name">{{ school.name }}</option>
          </select>
        </div>
        <button type="submit" class="form-submit-button-dashboard">Add User</button>
        <button type="button" @click="cancelAddUser" class="form-submit-button-dashboard mt-2 bg-gray-300 text-gray-800 hover:bg-gray-400">Cancel</button>
      </form>
    </div>

    <div class="content-card">
      <h3 class="text-xl font-semibold mb-4">All System Users</h3>
      <table class="w-full border-collapse">
        <thead>
          <tr class="bg-gray-50">
            <th class="border p-2 text-left">Name</th>
            <th class="border p-2 text-left">Email</th>
            <th class="border p-2 text-left">Role</th>
            <th class="border p-2 text-left">School</th>
            <th class="border p-2 text-left">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="user in users" :key="user.id">
            <td class="border p-2">{{ user.name }}</td>
            <td class="border p-2">{{ user.email }}</td>
            <td class="border p-2 capitalize">{{ user.role }}</td>
            <td class="border p-2">{{ user.school || 'N/A' }}</td>
            <td class="border p-2">
              <button class="btn-edit-inline" @click="editUser(user)">Edit</button>
              <button class="btn-delete-inline" @click="deleteUser(user.id)">Delete</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UserManagementView',
  data() {
    return {
      showAddUserForm: false,
      newUser: {
        name: '',
        email: '',
        role: '',
        school: ''
      },
      users: [
  { id: 1, name: 'Ananya Mehta', email: 'ananya.mehta@example.com', role: 'child', school: 'Greenfield Public School' },
  { id: 2, name: 'Rajesh Mehta', email: 'rajesh.mehta@example.com', role: 'parent', school: 'Greenfield Public School' },
  { id: 3, name: 'Neha Iyer', email: 'neha.iyer@example.com', role: 'teacher', school: 'Silver Oak High School' },
  { id: 4, name: 'System Admin', email: 'admin@eduindia.in', role: 'admin', school: '' },
  { id: 5, name: 'Kabir Singh', email: 'kabir.singh@example.com', role: 'child', school: 'Sunrise International School' },
  { id: 6, name: 'Poonam Singh', email: 'poonam.singh@example.com', role: 'parent', school: 'Sunrise International School' },
  { id: 7, name: 'Amit Banerjee', email: 'amit.banerjee@example.com', role: 'teacher', school: 'Riverdale Public School' },
  { id: 8, name: 'Diya Patel', email: 'diya.patel@example.com', role: 'child', school: 'Bright Future School' },
  { id: 9, name: 'Mehul Patel', email: 'mehul.patel@example.com', role: 'parent', school: 'Bright Future School' }
],

schools: [
  { id: 1, name: 'Greenfield Public School' },
  { id: 2, name: 'Sunrise International School' },
  { id: 3, name: 'Silver Oak High School' },
  { id: 4, name: 'Lotus Valley School' },
  { id: 5, name: 'Heritage International Academy' },
  { id: 6, name: 'Gyan Deep Public School' },
  { id: 7, name: 'Bright Future School' },
  { id: 8, name: 'Mount Glory School' },
  { id: 9, name: 'Starlight Academy' },
  { id: 10, name: 'Riverdale Public School' }
]

    };
  },
  methods: {
    addUser() {
      this.users.push({ ...this.newUser, id: Date.now() });
      this.resetNewUserForm();
      this.showAddUserForm = false;
      alert('User added successfully!');
    },
    cancelAddUser() {
      this.showAddUserForm = false;
      this.resetNewUserForm();
    },
    resetNewUserForm() {
      this.newUser = {
        name: '',
        email: '',
        role: '',
        school: ''
      };
    },
    editUser(user) {
      console.log('Editing user:', user);
      alert(`Editing user: ${user.name}`);
    },
    deleteUser(userId) {
      if (confirm('Are you sure you want to delete this user?')) {
        this.users = this.users.filter(user => user.id !== userId);
        alert('User deleted successfully!');
      }
    }
  }
};
</script>

<style scoped>
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
table {
    width: 100%;
    border-collapse: collapse;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    border-radius: 8px;
    overflow: hidden;
  }
  th, td {
    border: 1px solid #ddd;
    padding: 12px 16px;
    text-align: left;
  }
  thead {
    background-color: #e6f0ff;
    text-transform: uppercase;
    font-size: 14px;
  }
  tr:hover {
    background-color: #f0f8ff;
  }
</style>
