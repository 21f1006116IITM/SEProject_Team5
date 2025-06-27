<template>
  <div class="students-view w-full">
    <h2 class="dashboard-header">Student Management</h2>

    <div class="button-group-top-right">
      <button class="btn-add" @click="showAddStudentForm = true">Add Student</button>
    </div>

    <!-- Add Student Form -->
    <div v-if="showAddStudentForm" class="form-section mb-6 mx-auto">
      <h3 class="form-section-title">Add New Student</h3>
      <form @submit.prevent="addStudent">
        <div class="form-group-dashboard">
          <label for="studentName" class="form-label-dashboard">Student Name</label>
          <input type="text" id="studentName" v-model="newStudent.name" class="form-input-dashboard" required />
        </div>
        <div class="form-group-dashboard">
          <label for="studentClass" class="form-label-dashboard">Class</label>
          <input type="text" id="studentClass" v-model="newStudent.class" class="form-input-dashboard" required />
        </div>
        <div class="form-group-dashboard">
          <label for="rollNumber" class="form-label-dashboard">Roll Number</label>
          <input type="text" id="rollNumber" v-model="newStudent.rollNumber" class="form-input-dashboard" required />
        </div>
        <button type="submit" class="form-submit-button-dashboard">Add Student</button>
        <button type="button" @click="cancelAddStudent" class="form-submit-button-dashboard mt-2 bg-gray-300 text-gray-800 hover:bg-gray-400">Cancel</button>
      </form>
    </div>

    <div class="card-grid-dashboard">
      <div v-for="(student, index) in students" :key="index" class="card-item-dashboard">
        <h4 class="flex items-center gap-2">
          <img :src="require('@/assets/target.png')" alt="student" class="content-logo" />
          {{ student.name }}
        </h4>
        <p class="text-sm text-gray-500 mb-2">Class: {{ student.class }}</p>
        <p class="text-sm text-gray-500 mb-2">Roll: {{ student.rollNumber }}</p>
        <p class="font-semibold text-lg text-blue-600">Score: {{ student.score }}%</p>
        <p class="text-sm text-gray-500 mt-2">Goals Completed: {{ student.goalsCompleted }}</p>
        <div class="actions">
          <button class="btn-edit" @click="viewStudent(index)">View Progress</button>
          <button class="btn-delete" @click="removeStudent(index)">Remove</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'StudentsView',
  data() {
    return {
      showAddStudentForm: false,
      newStudent: {
        name: '',
        class: '',
        rollNumber: '',
        score: 0,
        goalsCompleted: 0
      },
      students: [
        {
          name: 'Spriha Mishra',
          class: '5th Grade',
          rollNumber: 'A001',
          score: 95,
          goalsCompleted: 5
        },
        {
          name: 'Kalkin Mishra',
          class: '5th Grade',
          rollNumber: 'A002',
          score: 87,
          goalsCompleted: 3
        },
        {
          name: 'Ram Pandey',
          class: '5th Grade',
          rollNumber: 'A003',
          score: 92,
          goalsCompleted: 4
        }
      ]
    };
  },
  methods: {
    addStudent() {
      this.students.push({ ...this.newStudent });
      this.resetStudentForm();
      this.showAddStudentForm = false;
      alert('Student added successfully!');
    },
    cancelAddStudent() {
      this.showAddStudentForm = false;
      this.resetStudentForm();
    },
    resetStudentForm() {
      this.newStudent = {
        name: '',
        class: '',
        rollNumber: '',
        score: 0,
        goalsCompleted: 0
      };
    },
    viewStudent(index) {
      console.log('Viewing student progress:', this.students[index]);
      alert(`Viewing progress for ${this.students[index].name}`);
    },
    removeStudent(index) {
      if (confirm('Are you sure you want to remove this student?')) {
        this.students.splice(index, 1);
        alert('Student removed successfully!');
      }
    }
  }
};
</script>