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
          <draggable v-model="items" tag="tbody">
            <tr v-for="item in expenses" :key="item.id">
              <td>
                <router-link
                  :to="{ name: 'expenses.edit', params: { id: item.id } }"
                >{{ item.name }}</router-link>
              </td>
              <td>{{ item.type_of_expenses }}</td>
              <td>{{ item.date }}</td>
              <td>{{ item.expenses }}</td>
              <td>{{ item.budgets }}</td>
            </tr>
          </draggable>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";

import store from '@/store/store';

import draggable from "vuedraggable";

export default {
  name: "expenses-table",
  components: {
    draggable
  },
  data() {
    return {
      items: [],
      currentItems: {},
      loading: false,
      dragging: false
    };
  },
  methods: {},
  computed: {
    expenses() {
      return this.$store.state.expenses;
    }
  },
  created() {
    this.$store.dispatch('loadExpenses');
  }
};
</script>