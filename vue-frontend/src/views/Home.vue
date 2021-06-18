<template>
  <section class="container mx-auto">
    <h1 class="text-center text-5xl font-bold py-8">Voting</h1>
    <section class="flex flex-shrink-0 flex-wrap justify-between">
      <div class="mx-6 px-8 py-4 shadow-xl border mb-8 w-64">
        <div class="py-4">
          <img
            class="mb-4 mx-auto w-28 h-28 rounded-full"
            src="https://source.unsplash.com/random"
            alt=""
          />
          <h1 class="text-center mb-2">Employee Name</h1>

          <p class="text-center mb-4">Employee Nickname</p>
          <p class="py-2 pb-4 text-xl">Total votes: 8</p>

          <div class="flex justify-between items-between text-2xl mb-4">
            <i class="fab fa-linkedin-in"></i>
            <i class="fab fa-github"></i>
            <i class="fab fa-twitter"></i>
          </div>
          <button
            class="
              w-full
              border-2 border-gray-600
              my-2
              p-2
              text-gray-500
              uppercase
              font-bold
              text-sm
              leading-loose
              tracking-widest
              rounded-full
              hover:bg-gray-600 hover:text-white
            "
          >
            Vote for me
          </button>
        </div>
      </div>
    </section>
  </section>
</template>

<script>
export default {
  name: "Home",
};
</script>
