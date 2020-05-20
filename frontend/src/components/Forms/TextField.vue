<template>
  <div>
    <b-form-input v-bind:item="item"
      v-on:input="$emit('input', $emit.target.value)"
    ></b-form-input>
    <div class="mt-2">Value: {{ item }}</div>
  </div>
</template>

<script>
  export default {
    props: {
        item: {
            type: String
        }
    },
    data() {
      return {
      }
    }
  }
</script>