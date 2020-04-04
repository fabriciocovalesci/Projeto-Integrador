<template>
  <div>
    <nav-bar></nav-bar>
    <InicialPrincipal></InicialPrincipal>
    <SubTitulo />
    <Cafe />
    <localizacao></localizacao>
    <contato></contato>
    <Footer />
  </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import InicialPrincipal from "@/components/InicialPrincipal.vue";
import SubTitulo from "@/components/SubTitulo";
import Cafe from "@/components/Cafe";
import Localizacao from "@/components/Localizacao";
import Contato from "@/components/Contato";
import Footer from "@/components/Footer.vue";

export default {
  components: {
    NavBar,
    InicialPrincipal,
    SubTitulo,
    Cafe,
    Localizacao,
    Contato,
    Footer,
  },
};
</script>

<style>
@import "bootstrap/dist/css/bootstrap.css";
</style>
