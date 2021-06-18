import { createStore } from "vuex";

export default createStore({
  state: {
    employees: null,
  },
  getters: {
    employees: (state) => state.employees,
  },
  mutations: {
    SET_EMPLOYEES(state, employees) {
      state.employees = employees;
    },
  },
  actions: {},
  modules: {},
});
