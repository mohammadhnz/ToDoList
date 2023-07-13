<template>
  <div class="item">
    <div class="item__head">
      <span class="item__delete" @click="$emit('delete')">x</span>
      <h3 class="item__title">{{ title }}</h3>
    </div>
    <p class="item__description">{{ description }}</p>
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
};
</script>

<style scoped>
.item {
  position: relative;
  width: 100%;
  margin-top: 0;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  transition: background-color 0.3s ease, box-shadow 0.3s ease;
}

.item:hover {
  background-color: #bdbdbd;
  cursor: pointer;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.item__delete {
  position: absolute;
  top: 5px;
  right: 5px;
  font-size: 1.2rem;
  color: white;
  cursor: pointer;
}

.item__title {
  color: white;
  margin-left: 18px;
}

.item__head {
  margin-top: 0;
  padding: 3px;
  background-color: darkred;
  border-top-left-radius: 5px;
  border-top-right-radius: 5px;
}

.item__description {
  padding: 23px;
  margin-bottom: 5px;
}
</style>