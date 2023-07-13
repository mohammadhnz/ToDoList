<template>
  <div class="todo-list">
    <Item
        v-for="item in data"
        :key="item._id"
        :title="item.title"
        :description="item.description"
    >
    </Item>
  </div>
</template>

<script>
// import axios from 'axios';
import Item from "@/components/ListItem.vue";

export default {
  components: {Item},
  props: {
    data: () => ([])
  }
}
</script>
<style scoped>
.todo-list{
  display: flex;
  flex-direction: column;
  border: 2px solid darkred;
  width: 24rem;
  padding: 3px;
}
</style>