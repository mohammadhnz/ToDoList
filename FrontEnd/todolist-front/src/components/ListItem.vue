<template>
  <div>
    <ul>
      <li v-for="item in items" :key="item._id">
        {{ item.title }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      items: []
    }
  },
  mounted() {
    axios.get('/api/todo')
        .then(response => {
          this.items = response.data;
        })
        .catch(error => {
          console.log(error);
        });
  }
}
</script>