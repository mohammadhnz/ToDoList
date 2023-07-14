<template>
  <div class="todo-list">
    <div class="grid">
      <div class="grid-item" v-for="(item, index) in items" :key="index">
        <Item :title="item.title" :description="item.description" @delete="removeItem(index)" />
      </div>
    </div>
    <button class="add-item-btn" @click="showModal = true" v-if="!showModal">Add</button>
    <div class="modal" v-if="showModal">
      <div class="modal-content">
        <span class="close" @click="showModal = false">&times;</span>
        <h2>Add Item</h2>
        <form @submit.prevent="addItem">
          <label for="title-input">Title</label>
          <input type="text" id="title-input" v-model="newItem.title" required />
          <label for="description-input">Description</label>
          <textarea id="description-input" v-model="newItem.description" required></textarea>
          <button type="submit">Submit</button>
        </form>
      </div>
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
      ],
      showModal: false,
      newItem: {
        title: "",
        description: ""
      },
      columns: []
    }
  },
  created() {
    this.columns.push([]);
  },
  props: {
    data: {
      type: Array,
    }
  },
  methods: {
    removeItem(index) {
      // for test purpose
      this.items.splice(index, 1);
    },
    addItem() {
      this.items.push({
        title: this.newItem.title,
        description: this.newItem.description
      });
      this.newItem.title = "";
      this.newItem.description = "";
      this.showModal = false;
      this.updateColumns();
    },
    updateColumns() {
      const itemsPerColumn = 3; // Change this to set the number of items per column
      this.columns = [];
      for (let i = 0; i < this.items.length; i += itemsPerColumn) {
        const columnItems = this.items.slice(i, i + itemsPerColumn);
        this.columns.push(columnItems);
      }
    }
  },
  watch: {
    items() {
      this.updateColumns();
    }
  }
}
</script>
<style scoped>
.todo-list {
  display: flex;
  flex-direction: column;
  width: 100%;
  padding: 3px;
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  grid-gap: 10px;
}

.add-item-btn{
  position: relative;
  width: 50%;
  height: 2rem;
  margin-top: 5px;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  transform: translateX(50%);
  transition: background-color 0.3s ease, box-shadow 0.3s ease;
  background-color: darkred;
  color: white;
}

.add-item-btn:hover {
  background-color: #490404;
  cursor: pointer;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}
.modal {
  display: flex;
  align-items: center;
  justify-content: center;
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.4);
}

.modal-content {
  background-color: white;
  border-radius: 5px;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.close {
  float: right;
  font-size: 28px;
  font-weight: bold;
  cursor: pointer;
}

.close:hover {
  color: #888;
}

form {
  display: flex;
  flex-direction: column;
}

label {
  margin-top: 10px;
}

input[type="text"],
textarea {
  margin-top: 5px;
  border-radius: 5px;
  border: 1px solid #ccc;
  padding: 3px;
}

button[type="submit"] {
  margin-top: 10px;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  transition: background-color 0.3s ease, box-shadow 0.3s ease;
  background-color: darkred;
  color: white;
}

button[type="submit"]:hover {
  background-color: #490404;
  cursor: pointer;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

</style>