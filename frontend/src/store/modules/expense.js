import { apiService } from '@/common/api.service.js';

export const expenses = {
  state: {
    expenses: [],
    type_of_expenses: [],
    currentExpenses: {},
    newExpense: {
      name: null,
      type_of_expenses: null,
      date: "",
      expenses: null,
      budgets: null
    },
    loading: true,
    saving: true,
  },
  getters: {
    EXPENSES: state => {
      return state.expenses;
    },
    TYPE_OF_EXPENSES: state => {
      return state.type_of_expenses;
    }
  },
  mutations: {
    FETCH_EXPENSES: (state, expenses) => {
      state.expenses = expenses;
    },
    FETCH_TYPE_EXPENSES: (state, type_of_expenses) => {
      state.type_of_expenses = type_of_expenses;
    }
  },
  actions: {
    loadExpenses({ commit }) {
      let endpoint = `/api/v1/expenses/`;
      this.loading = true
      apiService(endpoint)
        .then(response => {
          commit('FETCH_EXPENSES', response);
          this.loading = false;
        })
        .catch(error => {
          console.log(error);
        })
    },
    getListExpenses({ commit }) {
      let endpoint = `/api/v1/type_of_expenses/`;
      this.loading = true;
      apiService(endpoint)
        .then(response => {
          commit('FETCH_TYPE_EXPENSES', response.data);
          this.loading = false;
        })
        .catch(err => {
          console.log(err);
        });
    },
    addExpenses({commit}, expense){
      let endpoint = `/api/v1/expenses/`;
      let method = "POST";
      this.saving = true;
      apiService(endpoint, method, this.expense)
        .then(currentExpenses => {
          this.saving = false;
          this.$router.push({
            name: "expenses.edit",
            params: { id: currentExpenses.id }
          });
        })
        .catch(err => {
          console.log(err);
        })
    }
  }
}