<template>
  <div class="fonte-nav">
    <nav class="navbar navbar-expand-lg navbar-light navbar-color fixed-top">
      <a class="navbar-brand fonte-nav" href="#" />

      <router-link class="nav-link fonte-nav" to="/"
        ><b-img :src="require('@/assets/coffee.png')"></b-img
      ></router-link>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarText"
        aria-controls="navbarText"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <router-link
          v-for="routes in links"
          v-bind:key="routes.id"
          :to="`${routes.page}`"
        ></router-link>

        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarText">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active align-self-end">
            <router-link class="nav-link fonte-nav" to="/">Home</router-link>
          </li>
          <li class="nav-item align-self-end">
            <router-link class="nav-link fonte-nav" to="/produtos"
              >Produtos</router-link
            >
          </li>
          <li class="nav-item align-self-end">
            <a class="nav-link fonte-nav" href="#">Faça seu pedido!</a>
          </li>
          <li class="nav-item align-self-end">
            <router-link class="nav-link fonte-nav" to="/localizacao"
              >Localização</router-link
            >
          </li>
          <li class="nav-item align-self-end">
            <router-link class="nav-link fonte-nav" to="/contato"
              >Contato</router-link
            >
          </li>
        </ul>
        <span class="navbar-text fonte-nav">
          <p>
            Em um relacionamento sério com café
            <b-icon icon="heart-fill"></b-icon>
          </p>
        </span>
      </div>
    </nav>
  </div>
</template>

<script>
import "bootstrap/dist/js/bootstrap.js";

export default {
  name: "nav-bar",
  data() {
    return {
      links: [
        {
          id: 0,
          page: "/"
        },
        {
          id: 1,
          page: "/produtos"
        },
        {
          id: 2,
          page: "/localizacao"
        },
        {
          id: 3,
          page: "/contato"
        }
      ]
    };
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=ABeeZee&display=swap");
@import "bootstrap/dist/css/bootstrap.css";

.navbar-color {
  background: #534329;
}

.fonte-nav {
  font-family: "ABeeZee", sans-serif;
  color: #ffffff !important;
}

.fonte-nav a:hover {
  text-decoration: underline;
  color: #000 !important;
}
</style>
