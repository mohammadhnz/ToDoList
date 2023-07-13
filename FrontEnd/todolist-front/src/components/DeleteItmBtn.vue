<template>
  <div>
    <button @click="deleteItem">Delete</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: {
    itemId: {
      type: String,
      required: true
    }
  },
  methods: {
    deleteItem() {
      axios.delete(`/api/todo/${this.itemId}`)
          .then(response => {
            this.$emit('item-deleted');
          })
          .catch(error => {
            console.log(error);
          });
    }
  }
}
</script>