<template>
  <div class="fonte-nav">
    <nav class="navbar navbar-expand-lg navbar-light bg-dark">
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
            <a class="nav-link fonte-nav " href="#">O Café</a>
          </li>
          <li class="nav-item align-self-end">
            <a class="nav-link fonte-nav" href="#">Localização</a>
          </li>
          <li class="nav-item align-self-end">
            <a class="nav-link fonte-nav" href="#">Contato</a>
          </li>
        </ul>
        <span class="navbar-text fonte-nav">
          Sem definição
        </span>
      </div>
    </nav>
  </div>
</template>

<script>
import "bootstrap/dist/js/bootstrap.js";

export default {
  name: "nav-bar"
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=ABeeZee&display=swap");
@import "bootstrap/dist/css/bootstrap.css";

.fonte-nav {
  font-family: "ABeeZee", sans-serif;
  color: #ffffff !important;
}
</style>
