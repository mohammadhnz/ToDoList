<template>
  <div>
    <h1>My Todo List</h1>
    <List :data="items"></List>
  </div>
</template>

<script>
import List from './components/ToDoList.vue';


export default {
  data() {
    return {
      items: [
        {title: "doing os", description: "i wanna dye instead!"},
        {title: "doing nlp", description: "it gives me anxiety"},
        {title: "doing this!", description: "fucking boring"}
      ]
    }
  },
  components: {
    List,
  },
  methods: {
    fetchItems() {
      return [];
    }
  },
  mounted() {
    // this.fetchItems();
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
