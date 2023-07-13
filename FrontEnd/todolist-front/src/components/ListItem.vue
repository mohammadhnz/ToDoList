<template>
  <div class="item">
    <h3 class="item__title">{{ title }}</h3>
    <p>{{ description }}</p>
  </div>
</template>

<script>


export default {
  props: {
    title: {
      type: String
    },
    description: {
      type: String
    }
  }
}
</script>
<style scoped>
.item {
  width: 100%;
  margin-top: 0;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

.item:hover {
  background-color: #bdbdbd;
  cursor: pointer;
}

.item__title {
  margin-top: 0;
  padding: 3px;
  background-color: darkred;
  color: white;
  border-top-left-radius: 5px;
  border-top-right-radius: 5px;
}
</style>