import { createStore } from "vuex";
import axios from "axios";

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
  actions: {
    async getEmployees({ commit }) {
      try {
        const response = await axios.get("api/winners/");
        console.log(response);
        commit("SET_EMPLOYEES", response.data);
      } catch (error) {
        console.error(error);
      }
    },
  },
  modules: {},
});
