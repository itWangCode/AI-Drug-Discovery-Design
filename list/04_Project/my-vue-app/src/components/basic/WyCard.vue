<!-- src/components/Card.vue -->
<template>
  <div class="card">
    <div class="icon">
      <slot name="icon"></slot>
    </div>
    <div class="card-content">
      <h3>{{ title }}</h3>
      <p>{{ description }}</p>
    </div>
    <div class="card-link-wrapper">
      <a :href="link" class="card-link">立即前往</a>
    </div>

  </div>
</template>
<script lang="ts">
import {defineComponent} from "vue";

export default defineComponent({
  name: "WyCard",
  props: {
    title: {
      type: String,
      required: true,
    },
    description: {
      type: String,
      required: true,
    },
    link: {
      type: String,
      required: true,
    },
  },
});
</script>

<style lang="scss" scoped>
.card {
  background-color: #fff;
  border: 1px solid #e1e4e8;
  border-radius: 8px;
  padding: 20px;
  text-align: center;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  max-width: 300px; /* 固定宽度 */
  width: 100%;
  height: 360px; /* 固定高度 */
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transition: box-shadow 0.3s ease;

  &:hover {
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  }

  .icon {
    margin-bottom: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-grow: 1;

    img {
      max-width: 60px;
      height: auto;
    }
  }

  .card-content {
    height: 100%;
    min-height: 130px;

    h3 {
      font-size: 18px;
      margin-bottom: 10px;
      color: #333;
      font-weight: 600;
    }

    p {
      font-size: 14px;
      color: #666;
      margin-bottom: 20px;
    }
  }


  .card-link-wrapper {
    .card-link {
      display: inline-block;
      padding: 8px 16px;
      background-color: #009b9d;
      color: white;
      border-radius: 4px;
      text-decoration: none;
      font-size: 14px;
      font-weight: 600;
      background-image: linear-gradient(90deg, #2fe2d1, #009b9d);


      &:hover {
        background: #33afb1;
        border-color: #33afb1;
        color: #fff;
      }
    }
  }


}
</style>
