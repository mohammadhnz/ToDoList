<template>
  <div class="todo-list">
    <div v-for="(item, index) in items" :key="index">
      <Item :title="item.title" :description="item.description" @delete="removeItem(index)" />
    </div>
  </div>
</template>

<script>
// import axios from 'axios';
import Item from "@/components/ListItem.vue";

export default {
  components: {Item},
  data() {
    return {
      items: [
        {title: "doing os", description: "i wanna dye instead!"},
        {title: "doing nlp", description: "it gives me anxiety"},
        {title: "doing this!", description: "fucking boring"}
      ]
    }
  },
  props: {
    data: () => ([])
  },
  methods: {
    removeItem(index) {
      // for test purpose
      this.items.splice(index, 1);
    }
  }
}
</script>
<style scoped>
.todo-list{
  display: flex;
  flex-direction: column;
  width: 24rem;
  padding: 3px;
}
</style>