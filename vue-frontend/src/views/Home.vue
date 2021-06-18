<template>
  <section class="container mx-auto">
    <h1 class="text-center text-5xl font-bold py-8">Voting</h1>

    <section class="flex flex-shrink-0 flex-wrap justify-between">
      <employee-card />
      <employee-card />
      <employee-card />
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
  mounted() {
    this.$store.dispatch("getEmployees");
  },
};
</script>
