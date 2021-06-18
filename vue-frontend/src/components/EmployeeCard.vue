<template>
  <div class="py-4">
    <img
      class="mb-4 mx-auto w-28 h-28 rounded-full"
      src="https://source.unsplash.com/random"
      alt="profile"
    />
    <h1 class="mb-2 text-center">{{ employee.name }}</h1>

    <p class="mb-4 text-center">{{ employee.nickname }}</p>
    <p class="pt-2 pb-4 text-xl">Total votes: {{ score }}</p>

    <div class="flex justify-between items-between mb-4 text-2xl">
      <i class="fab fa-linkedin-in"></i>
      <i class="fab fa-github"></i>
      <i class="fab fa-twitter"></i>
    </div>
    <button
      v-on:click="increase($event, id)"
      class="
        w-full
        border-2 border-gray-600
        rounded-full
        my-2
        p-2
        text-gray-500 text-sm
        uppercase
        font-bold
        leading-loose
        tracking-widest
        hover:bg-gray-600 hover:text-white
        disabled:bg-gray-600
      "
    >
      Vote for me
    </button>
  </div>
</template>

<script>
export default {
  props: ["id", "employee", "score"],
  methods: {
    increase: function ($event, id) {
      $event.target.disabled = true;
      this.$store.dispatch("incrementEmployeeScore", id);
    },
  },
};
</script>

<style></style>
