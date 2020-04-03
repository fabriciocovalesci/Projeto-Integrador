<template>
  <div>
    <nav-bar></nav-bar>
    <cafe></cafe>
    <SubTitulo />
    <localizacao></localizacao>
    <contato></contato>
  </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import Cafe from "@/components/Cafe.vue";
import SubTitulo from "@/components/SubTitulo";
import Localizacao from "@/components/Localizacao";
import Contato from "@/components/Contato";

export default {
  components: {
    NavBar,
    Cafe,
    SubTitulo,
    Localizacao,
    Contato,
  },
};
</script>

<style>
@import "bootstrap/dist/css/bootstrap.css";
</style>
