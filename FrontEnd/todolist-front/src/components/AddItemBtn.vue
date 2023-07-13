<template>
  <div>
    <form @submit.prevent="addItem">
      <input type="text" v-model="title" placeholder="Add a new item">
      <button type="submit">Add</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      title: ''
    }
  },
  methods: {
    addItem() {
      axios.post('/api/todo', { title: this.title })
          .then(response => {
            this.title = '';
            this.$emit('item-added', response.data);
          })
          .catch(error => {
            console.log(error);
          });
    }
  }
}
</script>