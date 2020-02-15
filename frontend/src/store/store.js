import Vue from 'vue';
import Vuex from 'vuex';

import { expenses } from '../store/modules/expense.js';


Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    expenses
  }
})