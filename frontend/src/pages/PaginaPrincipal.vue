<template>
  <div>
    <nav-bar></nav-bar>
    <cafe></cafe>
    <SubTitulo />
    <localizacao></localizacao>
  </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import Cafe from "@/components/Cafe.vue";
import SubTitulo from "@/components/SubTitulo";
import Localizacao from "@/components/Localizacao";

export default {
  components: {
    NavBar,
    Cafe,
    SubTitulo,
    Localizacao,
  },
};
</script>

<style>
@import "bootstrap/dist/css/bootstrap.css";
</style>
