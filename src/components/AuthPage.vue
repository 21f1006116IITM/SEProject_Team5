
<template>
  <div class="auth-container">
    <div class="auth-card">
      <h2 class="auth-title">{{ capitalizedType }}</h2>

      <!-- Dynamic Form for Signup/Login -->
<form v-if="type === 'signup' || type === 'login'" @submit.prevent="handleSubmit">
  
  <!-- Role Selection (only for signup, inside the form) -->
  <div v-if="type === 'signup'" class="form-group">
    <label for="role" class="form-label">I am a...</label>
    <div class="role-selection-container">
      <label class="role-option">
        <input 
          type="radio" 
          name="role" 
          value="Teacher" 
          v-model="formData.role"
          @change="handleRoleChange"
        />
        <span class="role-label">Teacher</span>
      </label>
      <label class="role-option">
        <input 
          type="radio" 
          name="role" 
          value="Child" 
          v-model="formData.role"
          @change="handleRoleChange"
        />
        <span class="role-label">Child</span>
      </label>
      <label class="role-option">
        <input 
          type="radio" 
          name="role" 
          value="Parent" 
          v-model="formData.role"
          @change="handleRoleChange"
        />
        <span class="role-label">Parent</span>
      </label>
    </div>
  </div>

  <!-- Name Field (for all signup roles) -->
  <div v-if="type === 'signup' && formData.role" class="form-group">
    <label for="name" class="form-label">Full Name</label>
    <input 
      type="text" 
      id="name" 
      v-model="formData.name" 
      class="form-input" 
      placeholder="Enter your full name" 
      required 
    />
  </div>

  <!-- Email ID Field (for all) -->
  <div v-if="(type === 'signup' && formData.role) || type === 'login'" class="form-group">
    <label for="email" class="form-label">Email Address</label>
    <input 
      type="email" 
      id="email" 
      v-model="formData.email" 
      class="form-input" 
      placeholder="e.g., user@example.com" 
      required 
    />
  </div>

  <!-- Phone Number (only for Teacher signup) -->
  <div v-if="type === 'signup' && formData.role === 'Teacher'" class="form-group">
    <label for="phone" class="form-label">Phone Number</label>
    <input 
      type="tel" 
      id="phone" 
      v-model="formData.phoneNumber" 
      class="form-input" 
      placeholder="e.g., +1 (234) 567-8900" 
      required 
    />
  </div>

  <!-- Class (only for Child signup) -->
  <div v-if="type === 'signup' && formData.role === 'Child'" class="form-group">
    <label for="class" class="form-label">Class/Grade</label>
    <input 
      type="text" 
      id="class" 
      v-model="formData.class" 
      class="form-input" 
      placeholder="e.g., 5th Grade, Class 10" 
      required 
    />
  </div>

  <!-- Teacher ID (only for Child signup) -->
  <div v-if="type === 'signup' && formData.role === 'Child'" class="form-group">
    <label for="teacherId" class="form-label">Teacher ID (Optional)</label>
    <input 
      type="text" 
      id="teacherId" 
      v-model="formData.teacherId" 
      class="form-input" 
      placeholder="e.g., TID12345" 
    />
  </div>

  <!-- Parent ID (only for Child signup) -->
  <div v-if="type === 'signup' && formData.role === 'Child'" class="form-group">
    <label for="parentId" class="form-label">Parent ID</label>
    <input 
      type="text" 
      id="parentId" 
      v-model="formData.parentId" 
      class="form-input" 
      placeholder="e.g., PID67890" 
      required 
    />
  </div>

  <!-- Roll Number (only for Child signup) -->
  <div v-if="type === 'signup' && formData.role === 'Child'" class="form-group">
    <label for="rollNumber" class="form-label">Roll Number (Optional)</label>
    <input 
      type="text" 
      id="rollNumber" 
      v-model="formData.rollNumber" 
      class="form-input" 
      placeholder="e.g., R101, 001" 
    />
  </div>

  <!-- Password Field (common for all login/signup) -->
  <div v-if="(type === 'signup' && formData.role) || type === 'login'" class="form-group">
    <label for="password" class="form-label">Password</label>
    <input 
      type="password" 
      id="password" 
      v-model="formData.password" 
      class="form-input" 
      placeholder="Enter your password" 
      required 
    />
  </div>

  <!-- Re-enter Password Field (common for all signup) -->
  <div v-if="type === 'signup' && formData.role" class="form-group">
    <label for="reEnterPassword" class="form-label">Confirm Password</label>
    <input 
      type="password" 
      id="reEnterPassword" 
      v-model="formData.reEnterPassword" 
      class="form-input" 
      placeholder="Re-enter your password" 
      required 
    />
  </div>

  <button 
    type="submit" 
    class="auth-submit-button"
    :disabled="type === 'signup' && !formData.role"
  >
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
        } 
        else if (this.formData.email === 'admin@example.com' && this.formData.password === 'password123') { // <-- NEW Admin Login
          this.$emit('navigate', 'dashboard', 'Admin');
        }
        
        else {
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
</script>

<style scoped>
.role-selection-container {
  display: flex;
  gap: 1rem;
  margin-top: 0.5rem;
}

.role-option {
  display: flex;
  align-items: center;
  cursor: pointer;
  padding: 0.75rem 1rem;
  border: 2px solid #e5e7eb;
  border-radius: 0.5rem;
  transition: all 0.2s ease;
}

.role-option:hover {
  border-color: #3b82f6;
  background-color: #f8fafc;
}

.role-option input[type="radio"] {
  margin-right: 0.5rem;
}

.role-option input[type="radio"]:checked + .role-label {
  font-weight: 600;
  color: #3b82f6;
}

.role-option:has(input[type="radio"]:checked) {
  border-color: #3b82f6;
  background-color: #eff6ff;
}

@media (max-width: 768px) {
  .role-selection-container {
    flex-direction: column;
  }
}

</style>
```

