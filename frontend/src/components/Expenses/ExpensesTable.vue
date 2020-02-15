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
          <tbody v-if="!loading">
            <tr v-for="item in expenses" :key="item.id">
              <td>
                <router-link
                  :to="{ name: 'expenses.edit', params: { id: item.id } }"
                  >{{ item.name }}</router-link
                >
              </td>
              <td>{{ item.type_of_expenses }}</td>
              <td>{{ item.date }}</td>
              <td>{{ item.expenses }}</td>
              <td>{{ item.budgets }}</td>
            </tr>
          </tbody>
          <tbody v-else>
            <div class="spinner-border" role="status">
              <span class="sr-only">Loading...</span>
            </div>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

import { FETCH_EXPENSES } from "@/store/actions.type";

export default {
  name: "expenses-table",
  methods: {},
  computed: {
    ...mapGetters(["expenses", "current_expense", "loading"])
  },
  mounted() {
    this.$store.dispatch(FETCH_EXPENSES);
  }
};
</script>
