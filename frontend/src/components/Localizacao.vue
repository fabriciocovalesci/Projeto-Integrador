<template>
  <div class="conteiner">
    <h3 class="titulo">Localização</h3>
    <p class="endereco">
      Estamos localizados no centro da cidade para sua melhor comodidade.
    </p>
    <iframe
      class="mapa"
      src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3534.529359658877!2d-52.27427914980647!3d-27.63908933046001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94e31341c30557b5%3A0xda8cf1d5722f6e80!2sQuiero%20Caf%C3%A9!5e0!3m2!1sen!2sbr!4v1585923725044!5m2!1sen!2sbr"
    ></iframe>
    <p class="endereco">
      Avenida Fulano de Tal nº0002 <br />Bairro Centro <br />CEP 99700-000
      <br />Erechim - RS
    </p>
  </div>
</template>

<script>
export default {
  name: "localizacao",
};
</script>

<style scope>
@import url("https://fonts.googleapis.com/css?family=ABeeZee&display=swap");

.titulo {
  font-family: "ABeeZee", sans-serif;
  text-align: center;
  color: #2c1c0d;
  margin: 30px auto 10px auto;
  padding: 10px;
}

.mapa {
  width: 100%;
  height: 400px;
  margin: 0 auto;
  list-style-type: none;
  padding: 3em 0;
}

.endereco {
  font-family: "ABeeZee", sans-serif;
  text-align: justify;
  padding: 10px;
}
</style>
