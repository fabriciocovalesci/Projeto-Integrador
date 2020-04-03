import Vue from "vue";
import Router from "vue-router";
import PaginaPrincipal from "@/pages/PaginaPrincipal";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "PaginaPrincipal",
      component: PaginaPrincipal,
    },
  ],
});
