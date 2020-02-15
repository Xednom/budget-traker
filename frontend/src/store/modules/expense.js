import { apiService } from '@/common/api.service.js';
import { FETCH_EXPENSES, FETCH_TYPE_EXPENSES, FETCH_AN_EXPENSE } from '@/store/actions.type';
import { FETCH_START, FETCH_END, SET_EXPENSES, SET_AN_EXPENSE, SET_TYPE_EXPENSES } from '@/store/mutations.type'

const state = {
  // a list of state related to expenses

  expenses: [],
  typeOfExpenses: [],
  expense: {},
  newExpense: {
    name: null,
    type_of_expenses: null,
    date: "",
    expenses: null,
    budgets: null
  },
  loading: false,
  saving: false,
}

const getters = {
  // define method to access state value

  expenses: state => {
    return state.expenses;
  },
  expense: state => {
    return state.expense;
  },
  type_of_expenses: state => {
    return state.typeOfExpenses;
  },
  loading: state => {
    return state.loading;
  }
}

const mutations = {
  // define mutations to redefine state value

  [FETCH_START] (state) {
    state.loading = true
  },
  [FETCH_END] (state) {
    state.loading = false
  },
  [SET_EXPENSES] (state, pExpenses) {
    state.expenses = pExpenses
  },
  [SET_AN_EXPENSE] (state, pExpense) {
    state.expense = pExpense
  },
  [SET_TYPE_EXPENSES] (state, pTypeOfExpenses) {
    state.typeOfExpenses = pTypeOfExpenses;
  }

}

const actions = {
  // define actions like FETCH_AN_EXPENSE

  [FETCH_EXPENSES] ({ commit }) {
    let endpoint = `/api/v1/expenses/`;
    commit(FETCH_START)
    apiService(endpoint)
      .then(response => {
        commit(SET_EXPENSES, response);
        commit(FETCH_END)
      })
      .catch(error => {
        console.log(error);
      })
  },
  [FETCH_TYPE_EXPENSES] ({ commit }) {
    let endpoint = `/api/v1/type_of_expenses/`;
    commit(FETCH_START)
    apiService(endpoint)
      .then(response => {
        commit(SET_TYPE_EXPENSES, response);
        commit(FETCH_END)
      })
      .catch(err => {
        console.log(err);
      });
  },
  [FETCH_AN_EXPENSE] ({ commit }, payload) {
    commit(FETCH_START)
    const expense_id = payload
    let endpoint = `/api/v1/expenses/${expense_id}/`;
    apiService(endpoint)
      .then(data => {
        commit(SET_AN_EXPENSE, data)
        commit(FETCH_END)
      })
      .catch(err => {
        console.log(err);
      })
  },
}

export const expenses = {
  state,
  getters,
  mutations,
  actions
}