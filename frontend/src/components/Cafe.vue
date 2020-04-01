<template>
  <div>
    <section id="carrossel-principal">
      <div
        id="carousel-controladores"
        class="carousel slide"
        data-ride="carousel"
        data-interval="2500"
      >
        <ol class="carousel-indicators">
          <li
            data-target="#carousel-controladores"
            data-slide-to="0"
            class="active"
          ></li>
          <li data-target="#carousel-controladores" data-slide-to="1"></li>
        </ol>
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img
              :src="require('@/assets/cafe2.jpg')"
              class="imagem-carrossel d-block w-100"
              alt="barraca de frutas e verduras em uma feira livre"
            />
            <div class="carousel-caption h-50 d-none d-md-block">
              <h2 class="fonte-titulo shadow-sm text-center display-4">
                Depois do café eu me expresso!
              </h2>
            </div>
          </div>
          <div class="carousel-item">
            <img
              :src="require('@/assets/cafe7.jpg')"
              class="imagem-carrossel d-block w-100"
              alt="tigelas com ingredientes culinários sendo manuseadas por pessoas, vistas por cima"
            />
            <div class="carousel-caption h-50 d-none d-md-block">
              <h2 class="fonte-titulo shadow-sm text-center display-4">
                Que o dia seja tão bom como cheirinho de café.
              </h2>
            </div>
          </div>
        </div>
        <a
          class="carousel-control-prev"
          href="#carousel-controladores"
          role="button"
          data-slide="prev"
        >
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="sr-only">Previous</span>
        </a>
        <a
          class="carousel-control-next"
          href="#carousel-controladores"
          role="button"
          data-slide="next"
        >
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="sr-only">Next</span>
        </a>
      </div>
    </section>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=ABeeZee&display=swap");

.tela-inicial {
  display: flex;
  flex-direction: inherit;
}

.imagem-carrossel {
  object-fit: cover;
  object-position: 80 20%;
  height: 500px;
}

.subtitulo {
}

.foto {
  max-width: 550px;
  max-height: 500px;
  width: auto;
  height: auto;
  border: 4px solid rgb(54, 46, 46);
}
</style>
