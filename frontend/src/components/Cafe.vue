<template>
  <div>
    <b-carousel
      id="carousel-1"
      v-model="slide"
      :interval="4000"
      controls
      indicators
      background="#ababab"
      img-width="100%"
      img-height="400"
      style="text-shadow: 1px 1px 2px #333;"
      @sliding-start="onSlideStart"
      @sliding-end="onSlideEnd"
    >
      <!-- Text slides with image -->
      <b-carousel-slide
        caption="First slide"
        text="Nulla vitae elit libero, a pharetra augue mollis interdum."
        :img-src="require('@/assets/cafe2.jpg')"
      ></b-carousel-slide>

      <!-- Slides with custom text -->
      <b-carousel-slide :img-src="require('@/assets/cafe5.jpg')">
        <h1>Coffee</h1>
      </b-carousel-slide>

      <!-- Slides with image only -->
      <b-carousel-slide
        :img-src="require('@/assets/cafe2.jpg')"
      ></b-carousel-slide>

      <!-- Slides with img slot -->
      <!-- Note the classes .d-block and .img-fluid to prevent browser default image alignment -->
      <b-carousel-slide>
        <template v-slot:img>
          <img
            class="foto"
            :src="require('@/assets/cafe2.jpg')"
            alt="image slot"
          />
        </template>
      </b-carousel-slide>
    </b-carousel>

    <p class="mt-4">
      Slide #: {{ slide }}<br />
      Sliding: {{ sliding }}
    </p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      slide: 0,
      sliding: null
    };
  },
  methods: {
    onSlideStart(slide) {
      this.sliding = true;
    },
    onSlideEnd(slide) {
      this.sliding = false;
    }
  }
};
</script>

<style scoped>
.foto {
  width: 100%;
  object-fit: cover;
  object-position: 0 80%;
  height: 350px;
}
</style>
