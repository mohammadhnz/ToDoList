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
  width: 100%;
  margin-top: 0;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

.item:hover {
  background-color: #bdbdbd;
  cursor: pointer;
}

.item__delete {
  display: inline-flex;
  margin-left: 22rem;
  font-weight: bold;
  font-size: 20px;
  line-height: 1;
  cursor: pointer;
  color: white;
}

.item__title {
  color: white;
}

.item__head{
  margin-top: 0;
  padding: 3px;
  background-color: darkred;
  border-top-left-radius: 5px;
  border-top-right-radius: 5px;
}
.item__description{
  padding: 23px;
  margin-bottom: 5px;
}
</style>