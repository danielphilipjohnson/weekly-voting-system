<template>
  <nav-bar />

  <router-view />
</template>
<script>
import NavBar from "@/layout/Navbar";

export default {
  components: {
    NavBar,
  },
};
</script>
