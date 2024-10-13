<template>
  <div class="banner">
    <!-- Banner 轮播组件 -->
    <div class="banner-container">
      <swiper
        :pagination="true"
        :autoplay="{ delay: 3000, disableOnInteraction: true }"
        loop
        class="mySwiper"
      >
        <swiper-slide v-for="(item, index) in banners" :key="index">
          <div class="banner-content">
            <h1>{{ mainTitle }}</h1>
            <h2>{{ item.title }}</h2>
            <p>{{ item.description }}</p>
          </div>
          <img :src="item.image" alt="banner image" class="banner-image"/>
        </swiper-slide>
        <div class="swiper-pagination"></div>
      </swiper>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { Swiper, SwiperSlide } from "swiper/vue";
import "swiper/swiper-bundle.css";

export default defineComponent({
  name: "BannerComponent",
  components: {
    Swiper,
    SwiperSlide,
  },
  props: {
    mainTitle: {
      type: String,
      default: "欢迎来到合成生物学知识库",
    },
    banners: {
      type: Array,
      required: true,
    },
  },
});
</script>

<style lang="scss" scoped>
.banner {
  .banner-container {
    width: 100%;
    height: 100%;
    position: relative;
    overflow: hidden;
  }

  .banner-content {
    position: absolute;
    top: 50%;
    left: 10%;
    transform: translateY(-50%);
    color: white;
    z-index: 10;
  }

  .banner-image {
    width: 100%;
    height: 600px;
    object-fit: cover;
  }

  /* Swiper 样式 */
  .swiper-pagination {
    bottom: 20px;
  }
}
</style>
