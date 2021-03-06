// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from "vue";
import App from "./App";
import router from "./router";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { BootstrapVue, IconsPlugin, FormPlugin } from "bootstrap-vue";
import { CardPlugin } from "bootstrap-vue";

Vue.use(CardPlugin);
Vue.use(BootstrapVue);
Vue.use(IconsPlugin);
Vue.use(FormPlugin);

Vue.use(FontAwesomeIcon);

Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: "#app",
  router,
  components: { App },
  template: "<App/>",
});
