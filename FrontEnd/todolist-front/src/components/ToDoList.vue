<template>
  <div>
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
    data: () => []
  }
}
</script>