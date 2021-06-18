<template>
  <nav-bar />

  <router-view />
  <Footer />
</template>
<script>
import NavBar from "@/layout/Navbar";
import Footer from "@/layout/Footer";

export default {
  components: {
    NavBar,
    Footer,
  },
};
</script>
