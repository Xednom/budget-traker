<template>
  <div class="container">
    <div class="mt-5">
      <router-link :to="{ name: 'expenses.add' }">Add</router-link>
    </div>
    <div class="card mt-5">
      <div class="card-header">Manage Expenses</div>
      <div class="card-body">
        <table class="table table-striped">
          <thead>
            <tr>
              <th scope="col">Name</th>
              <th scope="col">Type of Expenses</th>
              <th scope="col">Date</th>
              <th scope="col">Expenses</th>
              <th scope="col">Budget</th>
            </tr>
          </thead>
          <tr v-for="item in expenses.expenses" :key="item.id">
            <td>
              <router-link :to="{ name: 'expenses.edit', params: { id: item.id } }">{{ item.name }}</router-link>
            </td>
            <td>{{ item.type_of_expenses }}</td>
            <td>{{ item.date }}</td>
            <td>{{ item.expenses }}</td>
            <td>{{ item.budgets }}</td>
          </tr>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "expenses-table",
  methods: {},
  computed: mapState(['expenses']),
  created() {
    this.$store.dispatch("loadExpenses");
  }
};
</script>