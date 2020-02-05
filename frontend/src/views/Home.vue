<template>
  <div class="home">
    <expenses-table />
  </div>
</template>

<script>
import ExpensesTable from "@/components/Expenses/ExpensesTable.vue";

export default {
  name: "home",
  components: {
    ExpensesTable,
  }
};
</script>
