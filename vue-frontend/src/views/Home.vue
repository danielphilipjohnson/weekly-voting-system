<template>
  <section class="container mx-auto">
    <h1 class="py-8 text-center text-5xl font-bold">Voting</h1>
    <section class="flex flex-wrap justify-between">
      <div
        class="w-64 border mb-8 mx-6 py-4 px-8 shadow-xl"
        v-for="fetchedEmployee in fetchedEmployees"
        :key="fetchedEmployee.id"
      >
        <employee-card
          v-bind:employee="fetchedEmployee.employee"
          v-bind:id="fetchedEmployee.id"
          v-bind:score="fetchedEmployee.score"
        />
      </div>
    </section>
  </section>
</template>

<script>
import EmployeeCard from "@/components/EmployeeCard.vue";
export default {
  name: "Home",
  components: {
    EmployeeCard,
  },
  computed: {
    fetchedEmployees() {
      return this.$store.getters.employees;
    },
  },
  mounted() {
    this.$store.dispatch("getEmployees");
  },
};
</script>
