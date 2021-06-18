<template>
  <section class="container mx-auto">
    <h1 class="text-center text-5xl font-bold py-8">Voting</h1>
    <section class="flex flex-shrink-0 flex-wrap justify-between">
      <div
        class="mx-6 px-8 py-4 shadow-xl border mb-8 w-64"
        v-for="fetchedEmployee in fetchedEmployees"
        :key="fetchedEmployee.id"
      >
        <employee-card
          v-bind:employee="fetchedEmployee.employee"
          v-bind:id="fetchedEmployees.id"
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
