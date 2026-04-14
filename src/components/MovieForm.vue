<template>
  <div>
    <!-- Success message -->
    <div v-if="successMessage" class="alert alert-success">
      {{ successMessage }}
    </div>

    <!-- Error messages -->
    <div v-if="errors.length > 0" class="alert alert-danger">
      <ul class="mb-0">
        <li v-for="(error, index) in errors" :key="index">{{ error }}</li>
      </ul>
    </div>

    <form id="movieForm" @submit.prevent="saveMovie">
      <div class="form-group mb-3">
        <label for="title" class="form-label">Movie Title</label>
        <input type="text" name="title" id="title" class="form-control" />
      </div>

      <div class="form-group mb-3">
        <label for="description" class="form-label">Description</label>
        <textarea name="description" id="description" class="form-control" rows="4"></textarea>
      </div>

      <div class="form-group mb-3">
        <label for="poster" class="form-label">Photo Upload</label>
        <input type="file" name="poster" id="poster" class="form-control" accept="image/*" />
      </div>

      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const csrf_token     = ref('')
const successMessage = ref('')
const errors         = ref([])

function getCsrfToken() {
  fetch('/api/v1/csrf-token')
    .then((response) => response.json())
    .then((data) => {
      csrf_token.value = data.csrf_token
    })
}

onMounted(() => {
  getCsrfToken()
})

function saveMovie() {
  successMessage.value = ''
  errors.value = []

  let movieForm = document.getElementById('movieForm')
  let form_data = new FormData(movieForm)

  fetch('/api/v1/movies', {
    method: 'POST',
    body: form_data,
    headers: {
      'X-CSRFToken': csrf_token.value
    }
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.errors) {
        errors.value = data.errors
      } else {
        successMessage.value = data.message
        movieForm.reset()
      }
    })
    .catch((error) => {
      console.log(error)
    })
}
</script>
