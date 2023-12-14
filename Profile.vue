<template>
    <div class="profile-form">
      <form @submit.prevent="updateProfile">
        <div class="form-group">
          <label for="email">Email</label>
          <input type="email" class="form-control" id="email" v-model="userProfile.email">
        </div>
  
        <div class="form-group">
          <label for="dateOfBirth">Date of Birth</label>
          <input type="date" class="form-control" id="dateOfBirth" v-model="userProfile.dateOfBirth">
        </div>
  
        <div class="form-group">
          <label for="profileImage">Profile Image</label>
          <input type="file" class="form-control-file" id="profileImage" @change="onFileSelected">
        </div>
  
        <button type="submit" class="btn btn-primary">Update Profile</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        userProfile: {
          email: '',
          dateOfBirth: '',
          profileImage: null
        }
      };
    },
    methods: {
      onFileSelected(event) {
        this.userProfile.profileImage = event.target.files[0];
      },
      async updateProfile() {
        let formData = new FormData();
        formData.append('email', this.userProfile.email);
        formData.append('dateOfBirth', this.userProfile.dateOfBirth);
        if (this.userProfile.profileImage) {
          formData.append('profileImage', this.userProfile.profileImage);
        }
  
        try {
          const response = await fetch('/path-to-your-update-api/', {
            method: 'POST',
            body: formData,
            // Include headers as needed, for instance for CSRF protection or authorization
          });
          const result = await response.json();
          console.log(result);
        } catch (error) {
          console.error('Error:', error);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .profile-form {
    max-width: 500px;
    margin: 0 auto;
    padding: 20px;
  }
  
  .profile-form .form-group {
    margin-bottom: 15px;
  }
  
  .profile-form .form-control {
    border: 1px solid #ced4da;
    border-radius: 0.25rem;
  }
  
  .profile-form .form-control-file {
    display: block;
  }
  
  .profile-form .btn {
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 0.25rem;
    padding: 10px 15px;
  }
  </style>
  