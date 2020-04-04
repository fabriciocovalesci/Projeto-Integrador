import Vue from "vue";
import Router from "vue-router";
import PaginaPrincipal from "@/pages/PaginaPrincipal";
import Localizacao from "@/components/Localizacao";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "PaginaPrincipal",
      component: PaginaPrincipal,
    },
    {
      path: "/localizacao",
      name: "localizacao",
      component: Localizacao,
    },
  ],
});
