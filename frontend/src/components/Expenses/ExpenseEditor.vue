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
        <router-link :to="{ name: 'home' }">
          Back
        </router-link>
      </button>
      </div>
      <div class="card mt-5">
        <div class="card-header">
          Edit
          <strong>{{ item.name }}</strong> records
        </div>
        <div class="card-body">
          <form @submit.prevent="onSubmit">
            <div class="form-row">
              <div class="form-group col-md-6">
                <label for="inputEmail4">Name</label>
                <input type="text" class="form-control" v-model="item.name" />
              </div>
              <div class="form-group col-md-6">
                <label for="inputPassword4">Type of Expenses</label>
                <input type="text" class="form-control" v-model="item.type_of_expenses" />
              </div>
            </div>
            <div class="form-row">
              <div class="form-group col-md-6">
                <label for="inputEmail4">Expenses</label>
                <input type="text" class="form-control" v-model="item.expenses" />
              </div>
              <div class="form-group col-md-6">
                <label for="inputPassword4">Budget</label>
                <input type="text" class="form-control" v-model="item.budgets" />
              </div>
            </div>
            <button type="submit" class="btn btn-info">Update</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";

export default {
  name: "ExpenseEditor",
  props: {
    id: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      item: {},
      loading: false
    };
  },
  methods: {
    viewExpenses() {
      this.loading = true;
      let endpoint = `/api/v1/expenses/${this.id}/`;
      apiService(endpoint)
        .then(data => {
          this.item = data;
          this.loading = false;
        })
        .catch(err => {
          console.log(err);
        });
    },
    onSubmit() {
      if (!this.item.expenses) {
        this.error = "You can't leave an empty expenses!";
      } else if (!this.item.budgets) {
        this.error = "Can't leave the budget field empty!";
      } else {
        this.loading = true;
        let endpoint = `/api/v1/expenses/${this.id}/`;
        let method = "PUT";
        apiService(endpoint, method, this.item)
          .then(item => {
            this.loading = false;
            this.$router.push({
              name: "expenses",
              params: { id: item.id }
            });
            this.viewExpenses();
          })
          .catch(err => {
            console.log(err);
          })
      }
    }
  },
  created() {
    this.viewExpenses();
  }
};
</script>