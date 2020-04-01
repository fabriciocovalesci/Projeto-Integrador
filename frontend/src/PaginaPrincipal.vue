<template>
  <div>
    <nav-bar></nav-bar>
    <cafe></cafe>
  </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import Cafe from "@/components/Cafe.vue";
export default {
  components: {
    NavBar,
    Cafe
  }
};
</script>

<style>
@import "bootstrap/dist/css/bootstrap.css";
</style>
