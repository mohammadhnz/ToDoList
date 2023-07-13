<template>
  <div>
    <h3>{{ title }}</h3>
    <p>{{ description }}</p>
  </div>
</template>

<script>
import axios from 'axios';

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