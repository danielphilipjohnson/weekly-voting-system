<template>
  <div class="py-4">
    <img
      class="mb-4 mx-auto w-28 h-28 rounded-full"
      src="https://source.unsplash.com/random"
      alt=""
    />
    <h1 class="text-center mb-2">{{ employee.name }}</h1>

    <p class="text-center mb-4">{{ employee.nickname }}</p>
    <p class="py-2 pb-4 text-xl">Total votes: {{ score }}</p>

    <div class="flex justify-between items-between text-2xl mb-4">
      <i class="fab fa-linkedin-in"></i>
      <i class="fab fa-github"></i>
      <i class="fab fa-twitter"></i>
    </div>
    <button
      v-on:click="increase($event, id)"
      class="
        w-full
        border-2 border-gray-600
        my-2
        p-2
        text-gray-500 text-sm
        uppercase
        font-bold
        leading-loose
        tracking-widest
        rounded-full
        hover:bg-gray-600 hover:text-white
        disabled:opacity-50 disabled:bg-gray-600
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
