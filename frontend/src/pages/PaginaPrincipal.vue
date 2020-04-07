<template>
  <div>
    <InicialPrincipal></InicialPrincipal>
    <SubTitulo />
    <Cafe />
    <localizacao></localizacao>
    <contato></contato>
    <RedeSocial />
    <Footer />
  </div>
</template>

<script>
import InicialPrincipal from "@/components/InicialPrincipal.vue";
import SubTitulo from "@/components/SubTitulo";
import Cafe from "@/components/Cafe";
import Localizacao from "@/components/Localizacao";
import Contato from "@/components/Contato";
import RedeSocial from "@/components/RedeSocial.vue";
import Footer from "@/components/Footer.vue";

export default {
  components: {
    InicialPrincipal,
    SubTitulo,
    Cafe,
    Localizacao,
    Contato,
    RedeSocial,
    Footer
  }
};
</script>

<style>
@import "bootstrap/dist/css/bootstrap.css";
</style>
