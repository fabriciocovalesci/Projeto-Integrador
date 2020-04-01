<template>
  <div>
    <b-carousel
      id="carousel-fade"
      style="text-shadow: 0px 0px 2px #000"
      fade
      :interval="4000"
      indicators
    >
      <b-carousel-slide
        class="foto"
        caption="First slide"
        :img-src="require('@/assets/cafe2.jpg')"
      ></b-carousel-slide>
      <b-carousel-slide
        class="foto"
        caption="Second Slide"
        :img-src="require('@/assets/cafe4.jpg')"
      ></b-carousel-slide>
      <b-carousel-slide
        class="foto"
        caption="Third Slide"
        :img-src="require('@/assets/cafe5.jpg')"
      ></b-carousel-slide>
    </b-carousel>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.foto {
  width: 100%;
  object-fit: cover;
  object-position: 0 80%;
  height: calc(100vh - 56px);
}
</style>
