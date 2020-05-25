<template>
  <div class="container">
    <div class="mt-5" v-if="loading">
      <div class="spinner-border" role="status">
        <span class="sr-only">Loading...</span>
      </div>
    </div>
    <div v-else>
      <div class="row">
        <button type="button" class="btn btn-link mt-5 pull-left">
          <router-link :to="{ name: 'home' }">Back</router-link>
        </button>
      </div>
      <div class="card mt-5">
        <div class="card-header">
          Edit
          <strong>{{ expense.name }}</strong> records
        </div>
        <div class="card-body">
          <form @submit.prevent="onSubmit">
            <div class="form-row">
              <div class="form-group col-md-6">
                <label for="inputEmail4">Name</label>
                <input
                  type="text"
                  class="form-control"
                  disabled
                  v-model="expense.name"
                />
              </div>
              <div class="form-group col-md-6">
                <label for="inputEmail4">Type of Expenses</label>
                <div class="input-group mb-3">
                  <div class="input-group-prepend">
                    <label class="input-group-text" for="inputGroupSelect01"
                      >Options</label
                    >
                  </div>
                  <select-option v-model="expense.type_of_expenses"
                    :items="type_of_expenses"></select-option>
                </div>
              </div>
            </div>
            <div class="form-row">
              <div class="form-group col-md-6">
                <label for="inputEmail4">Expenses</label>
                <number-field v-model="expense.expenses"></number-field>
              </div>
              <div class="form-group col-md-6">
                <label for="inputPassword4">Budget</label>
                <number-field v-model="expense.budgets"></number-field>
              </div>
            </div>
            <button type="submit" class="btn btn-info">Update</button>
            <button
              type="submit"
              class="btn btn-danger ml-2"
              @click="deleteExpense"
            >
              Delete
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";

import { mapGetters } from "vuex";
import { FETCH_AN_EXPENSE, FETCH_TYPE_EXPENSES } from "@/store/actions.type";

import SelectOption from "@/components/Forms/SelectOption.vue";
import NumberField from "@/components/Forms/NumberField.vue";

export default {
  name: "ExpenseEditor",
  components: {
    NumberField, SelectOption
  },
  props: {
    id: {
      type: String,
      required: true
    }
  },
  methods: {
    onSubmit() {
      if (!this.expense.expenses) {
        this.error = "You can't leave an empty expenses!";
      } else if (!this.expense.budgets) {
        this.error = "Can't leave the budget field empty!";
      } else {
        this.loading = true;
        let endpoint = `/api/v1/expenses/${this.id}/`;
        let method = "PUT";
        apiService(endpoint, method, this.expense)
          .then(expense => {
            this.loading = false;
            this.$router.push({
              name: "expenses.edit",
              params: { id: expense.id }
            });
            this.viewExpenses();
          })
          .catch(err => {
            console.log(err);
          });
      }
    },
    deleteExpense() {
      let endpoint = `/api/v1/expenses/${this.id}/`;
      let method = "DELETE";
      apiService(endpoint, method).then(() => {
        this.$router
          .push({
            name: "home"
          })
          .catch(err => {
            console.log(err);
          });
      });
    }
  },
  computed: {
    ...mapGetters(["expense", "type_of_expenses", "loading"])
  },
  mounted() {
    this.$store.dispatch(FETCH_AN_EXPENSE, this.$route.params.id);
    this.$store.dispatch(FETCH_TYPE_EXPENSES);
  }
};
</script>
