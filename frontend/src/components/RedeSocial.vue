<template>
  <div>
    <h4 class="titulo">Nossas redes sociais</h4>
    <p class="paragrafo">
      Nos siga em sua redes social e acompanhe nossas promoções !!!
    </p>

    <div class="d-flex justify-content-center m-3">
      <b-img
        :src="require('@/assets/twitter.png')"
        fluid
        alt="Fluid image"
      ></b-img>

      <b-img
        class="icones"
        :src="require('@/assets/instagram.png')"
        fluid
        alt="Fluid image"
      ></b-img>

      <b-img
        class="icones"
        :src="require('@/assets/facebook.png')"
        fluid
        alt="Fluid image"
      ></b-img>

      <b-img
        class="icones"
        :src="require('@/assets/youtube.png')"
        fluid
        alt="Fluid image"
      ></b-img>

      <b-img
        class="icones"
        :src="require('@/assets/whatsapp.png')"
        fluid
        alt="Fluid image"
      ></b-img>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=ABeeZee&display=swap");
@import "bootstrap/dist/css/bootstrap.css";

.titulo {
  font-family: "ABeeZee", sans-serif;
  text-align: center;
  margin-top: 90px !important;
  color: #534329;
}

.paragrafo {
  font-family: "ABeeZee", sans-serif;
  text-align: center;
  margin: 0 auto;
}

.icones {
  padding: 10px;
}
</style>
