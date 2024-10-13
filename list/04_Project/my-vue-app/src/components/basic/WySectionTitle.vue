<template>
  <div class="section-title">
    <span>{{ title }}</span>
  </div>
</template>

<script lang="ts">
import {defineComponent} from "vue";

export default defineComponent({
  name: "SectionTitle",
  props: {
    title: {
      type: String,
      required: true,
    },
  },
});
</script>

<style lang="scss" scoped>
.section-title {
  position: relative;
  display: flex;
  align-content: center;
  justify-content: center;
  font-size: 36px;
  font-weight: bold;
  color: var(--primary-color);
  text-align: center;
  padding-top: 50px;
  padding-bottom: 50px;
  background-color: white;

  span{
    position: relative;
  }

  span::after,&::after {
    content: "";
    position: absolute;
    width: 100%;
    height: 10px;
    left: 0;
    bottom: 0;
    background-color: #009b9d;
    opacity: .1;
  }
}

</style>
