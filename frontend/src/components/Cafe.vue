<template>
  <div>
    <h2 class="titulo">Nossos Produtos</h2>

    <div class="container d-flex justify-content-around flex-wrap">
      <div class="card borda" style="width: 18rem;">
        <img
          class="card-img-top"
          :src="require('@/assets/cafeteria.jpg')"
          alt="Card image cap"
        />
        <div class="card-body">
          <p class="card-text">
            Ambiente muito aconchegante, para desfrutar do nosso delicioso café.
          </p>
        </div>
      </div>

      <div class="card borda" style="width: 18rem;">
        <img
          class="card-img-top"
          :src="require('@/assets/cafeteria.jpg')"
          alt="Card image cap"
        />
        <div class="card-body">
          <p class="card-text">
            Ambiente muito aconchegante, para desfrutar do nosso delicioso café.
          </p>
        </div>
      </div>

      <div class="card borda" style="width: 18rem;">
        <img
          class="card-img-top"
          :src="require('@/assets/cafeteria.jpg')"
          alt="Card image cap"
        />
        <div class="card-body">
          <p class="card-text">
            Ambiente muito aconchegante, para desfrutar do nosso delicioso café.
          </p>
        </div>
      </div>

      <div class="card borda" style="width: 18rem;">
        <img
          class="card-img-top"
          :src="require('@/assets/cafeteria.jpg')"
          alt="Card image cap"
        />
        <div class="card-body">
          <p class="card-text">
            Ambiente muito aconchegante, para desfrutar do nosso delicioso café.
          </p>
        </div>
      </div>

      <div class="card borda" style="width: 18rem;">
        <img
          class="card-img-top"
          :src="require('@/assets/cafeteria.jpg')"
          alt="Card image cap"
        />
        <div class="card-body">
          <p class="card-text">
            Ambiente muito aconchegante, para desfrutar do nosso delicioso café.
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=ABeeZee&display=swap");

.titulo {
  font-family: "ABeeZee", sans-serif;
  text-align: center;
  color: #2c1c0d;
  margin: 0 auto;
  padding: 10px;
}

.borda {
  border: 2px solid black;
  margin: 10px 5px;
  padding: 5px;
}
</style>
