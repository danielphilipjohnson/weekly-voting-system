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
    UPDATE_EMPLOYEE(state, id) {
      const employees = state.employees;

      employees.map((employee) => {
        if (employee.id === id) {
          employee.score += 1;
        }
      });
      state.employees = employees;
    },
  },
  actions: {
    async getEmployees({ commit }) {
      try {
        const response = await axios.get("api/winners/");
        commit("SET_EMPLOYEES", response.data);
      } catch (error) {
        console.error(error);
      }
    },
    async incrementEmployeeScore({ commit }, id) {
      await axios.put(`api/winner/${id}`);
      commit("UPDATE_EMPLOYEE", id);
    },
  },
  modules: {},
});
