<template>
  <div>
    <h1>My Todo List</h1>
    <todo-list @item-deleted="fetchItems"></todo-list>
    <add-item @item-added="fetchItems"></add-item>
  </div>
</template>

<script>
import TodoList from './components/TodoList.vue';
import AddItem from './components/AddItem.vue';

export default {
  components: {
    TodoList,
    AddItem
  },
  methods: {
    fetchItems() {
      // Fetch the list of items from the backend API
    }
  },
  mounted() {
    this.fetchItems();
  }
}
</script>