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
                  <label class="input-group-text" for="inputGroupSelect01"
                    >Options</label
                  >
                </div>
                <select-option v-model="newExpense.type_of_expenses"
                  :items="type_of_expenses">
                </select-option>
              </div>
            </div>
          </div>
          <div class="form-row">
            <div class="form-group col-md-6">
              <label for="inputEmail4">Expenses</label>
              <number-field v-model="newExpense.expenses"></number-field>
            </div>
            <div class="form-group col-md-6">
              <label for="inputPassword4">Budget</label>
              <number-field v-model="newExpense.budgets"></number-field>
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

import { mapGetters } from "vuex";
import { FETCH_TYPE_EXPENSES } from "@/store/actions.type";

import SelectOption from "@/components/Forms/SelectOption.vue";
import NumberField from "@/components/Forms/NumberField.vue";

export default {
  name: "ExpenseAdd",
  components: {
    SelectOption, NumberField
  },
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
    }
  },
  computed: {
    ...mapGetters(["type_of_expenses", "loading"])
  },
  mounted() {
    this.$store.dispatch(FETCH_TYPE_EXPENSES);
  }
};
</script>
