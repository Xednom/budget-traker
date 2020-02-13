import Vue from 'vue';
import Vuex from 'vuex';

import { apiService } from "@/common/api.service.js";


Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    expenses: [],
    expense: {
      name: null,
      type_of_expenses: null,
      date: '',
      expenses: null,
      budgets: null
    }
  },
  getters: {
    EXPENSES: state => {
      return state.expenses;
    }
  },
  mutations: {
    FETCH_EXPENSES: (state, expenses) => {
      state.expenses = expenses;
    }
  },

  actions: {
    loadExpenses({ commit }) {
      let endpoint = `/api/v1/expenses/`;
      apiService(endpoint)
        .then(items => {
          commit('FETCH_EXPENSES', items);
        })
        .catch(error => {
          console.log(error);
        })
    }
  }
})