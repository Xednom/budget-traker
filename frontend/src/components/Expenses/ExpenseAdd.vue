<template>
  <div class="container col-md-4">
    <div class="row">
      <button type="button" class="btn btn-link mt-5 pull-left">
        <router-link :to="{ name: 'home' }">Back</router-link>
      </button>
    </div>
    <div class="card mt-5">
      <div class="card-header">Add Expenses</div>
      <div class="card-body">
        <form @submit.prevent="onSubmit">
          <div class="form-row">
            <div class="form-group col-md-12">
              <div class="input-group mb-12">
                <div class="input-group-prepend">
                  <label class="input-group-text" for="inputGroupSelect01">Options</label>
                </div>
                <select class="custom-select" id="inputGroupSelect01" v-model="newExpense.type_of_expenses">
                  <option v-for="expense in type_of_expenses" :key="expense.id">{{ expense.name }}</option>
                </select>
              </div>
            </div>
          </div>
          <div class="form-row">
            <div class="form-group col-md-6">
              <label for="inputEmail4">Expenses</label>
              <input type="text" class="form-control" v-model="newExpense.expenses" />
            </div>
            <div class="form-group col-md-6">
              <label for="inputPassword4">Budget</label>
              <input type="text" class="form-control" v-model="newExpense.budgets" />
            </div>
          </div>
          <button type="submit" class="btn btn-success">Add</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";

import { mapGetters} from "vuex";
import { FETCH_TYPE_EXPENSES } from "@/store/actions.type";

export default {
  name: "ExpenseAdd",

  data() {
    return {
      saving: false,
      success: false,
      expenses: {},
      currentItem: {},
      newExpense: {
        name: null,
        type_of_expenses: null,
        date: "",
        expenses: null,
        budgets: null
      }
    };
  },
  methods: {
    onSubmit() {
      this.saving = true;
      let endpoint = "/api/v1/expenses/";
      let method = "POST";
      apiService(endpoint, method, this.newExpense)
        .then(currentItem => {
          this.saving = false;
          this.success = true;
          this.$router.push({
            name: "expenses.edit",
            params: { id: currentItem.id }
          });
        })
        .catch(err => {
          console.log(err);
        });
    },
  },
  computed: {
    ...mapGetters(['type_of_expenses', 'loading'])
  },
  mounted() {
    this.$store.dispatch(FETCH_TYPE_EXPENSES);
  }
};
</script>