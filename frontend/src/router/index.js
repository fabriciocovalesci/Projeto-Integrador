import Vue from "vue";
import Router from "vue-router";
import PaginaPrincipal from "@/pages/PaginaPrincipal";

import InicialPrincipal from "@/components/InicialPrincipal.vue";
import Cafe from "@/components/Cafe";
import Localizacao from "@/components/Localizacao";
import Contato from "@/components/Contato";
import RedeSocial from "@/components/RedeSocial.vue";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "PaginaPrincipal",
      component: PaginaPrincipal
    },
    {
      path: "/home",
      name: "home",
      component: InicialPrincipal
    },
    {
      path: "/produtos",
      name: "Cafe",
      component: Cafe
    },
    {
      path: "/localizacao",
      name: "localizacao",
      component: Localizacao
    },
    {
      path: "/contato",
      name: "contato",
      component: Contato
    },
    {
      path: "/redesocial",
      name: "RedeSocial",
      component: RedeSocial
    }
  ]
});
