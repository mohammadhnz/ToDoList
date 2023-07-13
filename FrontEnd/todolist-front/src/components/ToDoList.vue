<template>
  <div>
    <Item
        v-for="item in items"
        :key="item._id"
        :title="item.title"
        :description="item.description"
    >
    </Item>
  </div>
</template>

<script>
import axios from 'axios';
import Item from "@/components/Item.vue";

export default {
  components: {Item},
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