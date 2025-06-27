<template>
  <div class="parent-messages-view w-full">
    <h2 class="dashboard-header">Messages & Communication</h2>

    <div class="button-group-top-right">
      <button class="btn-add" @click="showComposeForm = true">Compose Message</button>
    </div>

    <!-- Compose Message Form -->
    <div v-if="showComposeForm" class="form-section mb-6 mx-auto">
      <h3 class="form-section-title">Compose Message</h3>
      <form @submit.prevent="sendMessage">
        <div class="form-group-dashboard">
          <label for="recipient" class="form-label-dashboard">To</label>
          <select id="recipient" v-model="newMessage.recipient" class="form-input-dashboard" required>
            <option value="">Select recipient</option>
            <option value="teacher">Teacher</option>
            <option v-for="child in children" :key="child.id" :value="child.name">{{ child.name }}</option>
          </select>
        </div>
        <div class="form-group-dashboard">
          <label for="subject" class="form-label-dashboard">Subject</label>
          <input type="text" id="subject" v-model="newMessage.subject" class="form-input-dashboard" required />
        </div>
        <div class="form-group-dashboard">
          <label for="messageBody" class="form-label-dashboard">Message</label>
          <textarea id="messageBody" v-model="newMessage.body" class="form-input-dashboard" rows="4" required></textarea>
        </div>
        <button type="submit" class="form-submit-button-dashboard">Send Message</button>
        <button type="button" @click="cancelCompose" class="form-submit-button-dashboard mt-2 bg-gray-300 text-gray-800 hover:bg-gray-400">Cancel</button>
      </form>
    </div>

    <div class="messages-container">
      <div class="messages-tabs">
        <button
          class="tab-button"
          :class="{ 'active': activeTab === 'inbox' }"
          @click="activeTab = 'inbox'"
        >
          Inbox ({{ inboxMessages.length }})
        </button>
        <button
          class="tab-button"
          :class="{ 'active': activeTab === 'sent' }"
          @click="activeTab = 'sent'"
        >
          Sent ({{ sentMessages.length }})
        </button>
      </div>

      <div class="messages-list">
        <div v-if="activeTab === 'inbox'">
          <div v-for="message in inboxMessages" :key="message.id" class="message-item">
            <div class="message-header">
              <h4>{{ message.subject }}</h4>
              <span class="message-date">{{ message.date }}</span>
            </div>
            <p class="message-sender">From: {{ message.sender }}</p>
            <p class="message-preview">{{ message.body }}</p>
            <div class="message-actions">
              <button class="btn-reply" @click="replyToMessage(message)">Reply</button>
              <button class="btn-delete" @click="deleteMessage(message.id, 'inbox')">Delete</button>
            </div>
          </div>
        </div>

        <div v-if="activeTab === 'sent'">
          <div v-for="message in sentMessages" :key="message.id" class="message-item">
            <div class="message-header">
              <h4>{{ message.subject }}</h4>
              <span class="message-date">{{ message.date }}</span>
            </div>
            <p class="message-recipient">To: {{ message.recipient }}</p>
            <p class="message-preview">{{ message.body }}</p>
            <div class="message-actions">
              <button class="btn-delete" @click="deleteMessage(message.id, 'sent')">Delete</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ParentMessagesView',
  data() {
    return {
      activeTab: 'inbox',
      showComposeForm: false,
      newMessage: {
        recipient: '',
        subject: '',
        body: ''
      },
      children: [
        { id: 1, name: 'Spriha Mishra' },
        { id: 2, name: 'Kalkin Mishra' }
      ],
      inboxMessages: [
        {
          id: 1,
          sender: 'Teacher Mishra',
          subject: 'Spriha\'s Progress Update',
          body: 'Spriha has been doing excellent work in our financial literacy program...',
          date: '2024-06-25'
        },
        {
          id: 2,
          sender: 'Spriha Mishra',
          subject: 'New Goal Request',
          body: 'Hi Mom, I want to save for a new bicycle. Can you help me set a goal?',
          date: '2024-06-24'
        }
      ],
      sentMessages: [
        {
          id: 1,
          recipient: 'Teacher Mishra',
          subject: 'Question about homework',
          body: 'Hello, I wanted to ask about Spriha\'s recent assignment...',
          date: '2024-06-23'
        }
      ]
    };
  },
  methods: {
    sendMessage() {
      this.sentMessages.push({
        id: Date.now(),
        recipient: this.newMessage.recipient,
        subject: this.newMessage.subject,
        body: this.newMessage.body,
        date: new Date().toISOString().split('T')[0]
      });
      this.resetMessageForm();
      this.showComposeForm = false;
      alert('Message sent successfully!');
    },
    cancelCompose() {
      this.showComposeForm = false;
      this.resetMessageForm();
    },
    resetMessageForm() {
      this.newMessage = {
        recipient: '',
        subject: '',
        body: ''
      };
    },
    replyToMessage(message) {
      this.newMessage = {
        recipient: message.sender,
        subject: 'Re: ' + message.subject,
        body: ''
      };
      this.showComposeForm = true;
    },
    deleteMessage(messageId, type) {
      if (confirm('Are you sure you want to delete this message?')) {
        if (type === 'inbox') {
          this.inboxMessages = this.inboxMessages.filter(m => m.id !== messageId);
        } else {
          this.sentMessages = this.sentMessages.filter(m => m.id !== messageId);
        }
        alert('Message deleted successfully!');
      }
    }
  }
};
</script>

<style scoped>
.messages-container {
  background: white;
  border-radius: 0.5rem;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.messages-tabs {
  display: flex;
  border-bottom: 1px solid #e5e7eb;
}

.tab-button {
  flex: 1;
  padding: 1rem;
  background: #f9fafb;
  border: none;
  cursor: pointer;
  font-weight: 500;
}

.tab-button.active {
  background: white;
  border-bottom: 2px solid #7c3aed;
}

.messages-list {
  padding: 1rem;
}

.message-item {
  border-bottom: 1px solid #e5e7eb;
  padding: 1rem 0;
}

.message-item:last-child {
  border-bottom: none;
}

.message-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.5rem;
}

.message-header h4 {
  font-weight: 600;
  margin: 0;
}

.message-date {
  font-size: 0.875rem;
  color: #6b7280;
}

.message-sender,
.message-recipient {
  font-size: 0.875rem;
  color: #6b7280;
  margin-bottom: 0.5rem;
}

.message-preview {
  color: #374151;
  margin-bottom: 1rem;
}

.message-actions {
  display: flex;
  gap: 0.5rem;
}

.btn-reply,
.btn-delete {
  padding: 0.25rem 0.75rem;
  border: none;
  border-radius: 0.25rem;
  cursor: pointer;
  font-size: 0.875rem;
}

.btn-reply {
  background: #7c3aed;
  color: white;
}

.btn-delete {
  background: #ef4444;
  color: white;
}
</style>