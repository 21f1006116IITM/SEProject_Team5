# Complete Updated AuthPage.vue

```vue
<template>
  <div class="auth-container">
    <div class="auth-card">
      <h2 class="auth-title">{{ capitalizedType }}</h2>

      <!-- Role Selection for Sign Up -->
      <div v-if="type === 'signup' && !userRole" class="role-selection-buttons">
        <button
          class="role-button"
          :class="{ 'active': selectedRole === 'Teacher' }"
          @click="selectRole('Teacher')"
        >
          Teacher
        </button>
        <button
          class="role-button"
          :class="{ 'active': selectedRole === 'Child' }"
          @click="selectRole('Child')"
        >
          Child
        </button>
        <button
          class="role-button"
          :class="{ 'active': selectedRole === 'Parent' }"
          @click="selectRole('Parent')"
        >
          Parent
        </button>
      </div>

      <!-- Back button for role selection -->
      <button v-if="type === 'signup' && userRole" @click="userRole = null" class="auth-link mb-4">
        &larr; Back to Role Selection
      </button>

      <!-- Dynamic Form based on Type and Role -->
      <form v-if="(type === 'signup' && userRole) || type === 'login'" @submit.prevent="handleSubmit">
        <!-- Name Field (for all signup roles) -->
        <div v-if="type === 'signup' && (userRole === 'Teacher' || userRole === 'Child' || userRole === 'Parent')" class="form-group">
          <label for="name" class="form-label">Name</label>
          <input type="text" id="name" v-model="formData.name" class="form-input" placeholder="Enter your full name" required />
        </div>

        <!-- Email ID Field (for all) -->
        <div class="form-group">
          <label for="email" class="form-label">Email ID</label>
          <input type="email" id="email" v-model="formData.email" class="form-input" placeholder="e.g., user@example.com" required />
        </div>

        <!-- Phone Number (only for Teacher signup) -->
        <div v-if="type === 'signup' && userRole === 'Teacher'" class="form-group">
          <label for="phone" class="form-label">Phone Number</label>
          <input type="tel" id="phone" v-model="formData.phoneNumber" class="form-input" placeholder="e.g., +11234567890" :required="userRole === 'Teacher' && type === 'signup'" />
        </div>

        <!-- Class (only for Child signup) -->
        <div v-if="type === 'signup' && userRole === 'Child'" class="form-group">
          <label for="class" class="form-label">Class</label>
          <input type="text" id="class" v-model="formData.class" class="form-input" placeholder="e.g., 5th Grade" :required="userRole === 'Child' && type === 'signup'" />
        </div>

        <!-- Teacher ID (only for Child signup) -->
        <div v-if="type === 'signup' && userRole === 'Child'" class="form-group">
          <label for="teacherId" class="form-label">Teacher ID</label>
          <input type="text" id="teacherId" v-model="formData.teacherId" class="form-input" placeholder="e.g., TID12345" />
        </div>

        <!-- Parent ID (only for Child signup) -->
        <div v-if="type === 'signup' && userRole === 'Child'" class="form-group">
          <label for="parentId" class="form-label">Parent ID</label>
          <input type="text" id="parentId" v-model="formData.parentId" class="form-input" placeholder="e.g., PID67890" :required="userRole === 'Child' && type === 'signup'" />
        </div>

        <!-- Roll Number (only for Child signup) -->
        <div v-if="type === 'signup' && userRole === 'Child'" class="form-group">
          <label for="rollNumber" class="form-label">Roll Number</label>
          <input type="text" id="rollNumber" v-model="formData.rollNumber" class="form-input" placeholder="e.g., R101" />
        </div>

        <!-- Password Field (common for all login/signup) -->
        <div class="form-group">
          <label for="password" class="form-label">Password</label>
          <input type="password" id="password" v-model="formData.password" class="form-input" placeholder="Enter your password" required />
        </div>

        <!-- Re-enter Password Field (common for all signup) -->
        <div v-if="type === 'signup'" class="form-group">
          <label for="reEnterPassword" class="form-label">Re-enter Password</label>
          <input type="password" id="reEnterPassword" v-model="formData.reEnterPassword" class="form-input" placeholder="Re-enter your password" required />
        </div>

        <button type="submit" class="auth-submit-button">
          {{ capitalizedType }}
        </button>
      </form>

      <!-- Navigation Links -->
      <a v-if="type === 'signup'" href="#" @click.prevent="$emit('navigate', 'login')" class="auth-link">
        Already have an account? Login
      </a>
      <a v-else-if="type === 'login'" href="#" @click.prevent="$emit('navigate', 'signup')" class="auth-link">
        Don't have an account? Sign Up
      </a>
    </div>
  </div>
</template>

<script>
/* eslint-disable no-unused-vars */
export default {
  name: 'AuthPage',
  props: {
    type: {
      type: String,
      required: true
    }
  },
  emits: ['navigate'],
  data() {
    return {
      selectedRole: null,
      formData: {
        name: '',
        email: '',
        phoneNumber: '',
        class: '',
        teacherId: '',
        parentId: '',
        rollNumber: '',
        password: '',
        reEnterPassword: '',
      }
    };
  },
  computed: {
    capitalizedType() {
      return this.type.charAt(0).toUpperCase() + this.type.slice(1);
    },
    userRole: {
      get() {
        return this.type === 'login' ? 'login' : this.selectedRole;
      },
      set(value) {
        this.selectedRole = value;
      }
    }
  },
  watch: {
    type: {
      immediate: true,
      handler(newType) {
        this.resetForm();
        if (newType === 'login') {
          this.selectedRole = null;
        }
      }
    },
    selectedRole() {
      this.resetForm();
    }
  },
  methods: {
    selectRole(role) {
      this.selectedRole = role;
    },
    handleSubmit() {
      if (this.type === 'signup') {
        if (this.formData.password !== this.formData.reEnterPassword) {
          alert('Passwords do not match!');
          return;
        }

        if (this.selectedRole === 'Child') {
          this.saveChildToLocalStorage(this.formData);
          alert('Child Sign-up successful! You can now log in.');
          this.$emit('navigate', 'login');
        } else {
          alert(`${this.capitalizedType} successful for ${this.selectedRole} role!`);
          this.$emit('navigate', 'landing');
        }
      } else if (this.type === 'login') {
        // **ENHANCED LOGIN LOGIC - This is the new addition**
        // Handle different user types with demo credentials
        if (this.formData.email === 'child@example.com' && this.formData.password === 'password123') {
          alert('Child Login successful! Redirecting to Dashboard.');
          this.$emit('navigate', 'dashboard', 'Child');
        } else if (this.formData.email === 'parent@example.com' && this.formData.password === 'password123') {
          alert('Parent Login successful! Redirecting to Dashboard.');
          this.$emit('navigate', 'dashboard', 'Parent');
        } else if (this.formData.email === 'teacher@example.com' && this.formData.password === 'password123') {
          alert('Teacher Login successful! Redirecting to Dashboard.');
          this.$emit('navigate', 'dashboard', 'Teacher');
        } else {
          // Check stored children users (existing functionality)
          const storedChildren = JSON.parse(localStorage.getItem('pennywise_children_users') || '[]');
          const foundChild = storedChildren.find(child =>
            child.email === this.formData.email && child.password === this.formData.password
          );
          
          if (foundChild) {
            alert('Child Login successful! Redirecting to Dashboard.');
            this.$emit('navigate', 'dashboard', 'Child');
          } else {
            alert('Login failed. Invalid email or password.');
          }
        }
      }
      console.log(`${this.capitalizedType} attempt for role: ${this.userRole}`, this.formData);
    },
    resetForm() {
      this.formData = {
        name: '',
        email: '',
        phoneNumber: '',
        class: '',
        teacherId: '',
        parentId: '',
        rollNumber: '',
        password: '',
        reEnterPassword: ''
      };
    },
    saveChildToLocalStorage(childData) {
      let children = JSON.parse(localStorage.getItem('pennywise_children_users') || '[]');
      
      const existingChildIndex = children.findIndex(child => child.email === childData.email);
      if (existingChildIndex > -1) {
        alert('A child with this email already exists. Please login or use a different email.');
        return;
      }

      const { reEnterPassword, ...dataToSave } = childData;
      children.push(dataToSave);
      localStorage.setItem('pennywise_children_users', JSON.stringify(children));
    }
  }
};
/* eslint-enable no-unused-vars */
</script>

<style scoped>
/* No specific scoped styles needed here, as global styles handle the look. */
</style>
```


## Demo Credentials for Testing:

- **Child**: `child@example.com` / `password123`
- **Parent**: `parent@example.com` / `password123`  
- **Teacher**: `teacher@example.com` / `password123`
- **Registered Children**: Any child registered through the signup form

