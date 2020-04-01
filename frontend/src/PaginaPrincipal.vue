<template>
  <div>
    <nav-bar></nav-bar>
    <cafe></cafe>
    <SubTitulo />
  </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import Cafe from "@/components/Cafe.vue";
import SubTitulo from "./components/SubTitulo";

export default {
  components: {
    NavBar,
    Cafe,
    SubTitulo
  }
};
</script>

<style>
@import "bootstrap/dist/css/bootstrap.css";
</style>
