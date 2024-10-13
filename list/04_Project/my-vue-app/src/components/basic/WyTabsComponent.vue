<template>
  <div class="tab-container">
    <!-- Tab 标题部分 -->
    <div class="tab-header">
      <div
          v-for="(tab, index) in tabs"
          :key="index"
          :class="['tab-item', { active: activeTab === index }]"
          @click="selectTab(index)"
      >
         <i class="iconfont  tab-icon" :class="tab.icon"></i>
<!--        <img :src="tab.icon" class="tab-icon" alt="tab-icon"/>-->
        <span>{{ tab.title }}</span>
      </div>
    </div>

    <!-- Tab 内容部分 -->
    <div class="tab-content">
      <h2>{{ tabs[activeTab].title }}</h2>
      <p>{{ tabs[activeTab].content }}</p>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from "vue";

interface Tab {
  title: string;
  icon: string;
  content: string;
}

export default defineComponent({
  name: "WyTabsComponent",
  props: {
    tabs: {
      type: Array as PropType<Tab[]>, // 使用 PropType 来指定 tabs 的类型
      required: true,
    },
  },
  data() {
    return {
      activeTab: 0, // 当前选中的 Tab 索引
    };
  },
  methods: {
    selectTab(index: number) {
      this.activeTab = index;
    },
  },
});
</script>


<style lang="scss" scoped>
.tab-container {
  width: 100%;
  text-align: center;
}

.tab-header {
  display: flex;
  justify-content: space-around;
  border-bottom: 2px solid #eaeaea;
  margin-bottom: 20px;
  .tab-icon{
    font-size: 50px;
    padding: 10px 0
  }
}

.tab-item {
  padding: 15px 20px;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  align-items: center;
  color: #333;
  transition: color 0.3s, border-bottom-color 0.3s;
}

.tab-item img {
  width: 40px;
  height: 40px;
  margin-bottom: 8px;
}

.tab-item.active {
  color: #009688; /* 选中时的颜色 */
  border-bottom: 2px solid #009688; /* 选中时的下划线 */
}

.tab-content {
  padding: 20px;
}

.tab-content h2 {
  font-size: 24px;
  margin-bottom: 10px;
  color: #333;
}

.tab-content p {
  font-size: 16px;
  line-height: 1.5;
  color: #666;
}
</style>
