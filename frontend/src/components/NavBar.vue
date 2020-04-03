<template>
  <div class="fonte-nav">
    <nav class="navbar navbar-expand-lg navbar-light navbar-color">
      <a class="navbar-brand fonte-nav" href="#" />
      <b-img :src="require('@/assets/coffee.png')"></b-img>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarText"
        aria-controls="navbarText"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarText">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active align-self-end">
            <a class="nav-link fonte-nav" href="#"
              >Home <span class="sr-only">(current)</span></a
            >
          </li>
          <li class="nav-item align-self-end">
            <a class="nav-link fonte-nav" href="#">O Café</a>
          </li>
          <li class="nav-item align-self-end">
            <a class="nav-link fonte-nav" href="#">Faça seu pedido!</a>
          </li>
          <li class="nav-item align-self-end">
            <a class="nav-link fonte-nav" href="#">Localização</a>
          </li>
          <li class="nav-item align-self-end">
            <a class="nav-link fonte-nav" href="#">Contato</a>
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
