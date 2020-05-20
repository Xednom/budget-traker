<template>
  <select class="custom-select" 
    @change="$emit('input', $event.target.items)">
    <option 
      v-for="item in items" 
      :key="item.id" 
      :selected="item === items">
      {{ item.name }}
    </option>
  </select>
</template>

<script>
export default {
  props: {
    items: {
      type: Array
    }
  }
};
</script>