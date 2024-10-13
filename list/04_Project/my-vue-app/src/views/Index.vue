<!-- src/views/Index.vue -->
<template>
  <div class="index">
     <!-- Banner 组件 -->
    <WyBannerComponent :banners="banners" />

    <!-- 主要功能标题组件 -->
    <WySectionTitle title="主要功能" />

    <!-- 调用 Card 组件，并传递 cards 数据 -->
    <div class="card grid">
      <WyCard
          v-for="(card, index) in cardsData"
          :key="index"
          :title="card.title"
          :description="card.description"
          :link="card.link">
        <template v-slot:icon>
          <img :src="card.icon" alt="icon" class="card-icon"/>
        </template>
      </WyCard>
    </div>

    <!-- 主要功能标题组件 -->
    <WySectionTitle title="实战科研" />

    <!-- 调用 Tab 组件，并传递 tabs 数据 -->
    <WyTabsComponent :tabs="tabsData"/>
  </div>
</template>

<script lang="ts">
import {defineComponent} from "vue";
import "swiper/swiper-bundle.css";

export default {
  data() {
    return {
      // Banner 数据，来自 JSON
      banners: [
        {
          title: "人工智能药物发现与设计平台",
          description:
              "AI 驱动的临床前新药研发开放平台，基于 AI Lab 自主研发的深度学习算法。",
          image: "src/assets/img/banner/bg.jpg",
        },
        {
          title: "创新的虚拟筛选技术",
          description:
              "通过计算模拟筛选出潜在药物，极大加速新药开发进程。",
          image: "src/assets/img/banner/1.png",
        },
        {
          title: "分子生成与优化",
          description: "利用AI技术生成分子结构并优化药物特性。",
          image: "src/assets/img/banner/3.png",
        },
      ],
      cardsData: [
        {
          title: "合成生物学知识术语库",
          description: "体验合成生物学AI语言模型",
          link: "#",
          icon: "src/assets/img/Card/1.png"
        },
        {
          title: "代谢通路设计系统",
          description: "逆向合成的策略",
          link: "#",
          icon: "src/assets/img/Card/2.png"
        },
        {
          title: "微生物代谢模拟系统",
          description: "体验模型的构建和优化迭代，提供可视化的交互界面和预测",
          link: "#",
          icon: "src/assets/img/Card/3.png"
        },
        {
          title: "蛋白质结构分析及相互作用关系分析系统",
          description: "蛋白质结构的分析及其相互作用关系的解析",
          link: "#",
          icon: "src/assets/img/Card/4.png"
        },
        {
          title: "蛋白质结构及功能模拟软件",
          description: "蛋白质结构和功能的模拟软件",
          link: "#",
          icon: "src/assets/img/Card/5.png"
        },
        {
          title: "模式微生物代谢网络，信息构建系统",
          description: "现代化的代谢网络构建系统，适用于生物信息分析",
          link: "#",
          icon: "src/assets/img/Card/1.png"
        },
        {
          title: "基因组编辑",
          description: "基因组编辑工具与功能",
          link: "#",
          icon: "src/assets/img/Card/2.png"
        },
        {
          title: "装置设计",
          description: "生物化学反应装置设计方案",
          link: "#",
          icon: "src/assets/img/Card/3.png"
        },
        {
          title: "基础数据库",
          description: "基础生物数据存储库",
          link: "#",
          icon: "src/assets/img/Card/4.png"
        },
        {
          title: "多组学",
          description: "多组学数据分析平台",
          link: "#",
          icon: "src/assets/img/Card/5.png"
        },
        {
          title: "元件库管理平台",
          description: "元件库的管理与调控系统",
          link: "#",
          icon: "src/assets/img/Card/1.png"
        },
        {
          title: "代谢合成反应设计与分析系统",
          description: "代谢合成反应设计系统与数据分析平台",
          link: "#",
          icon: "src/assets/img/Card/2.png"
        },
        {
          title: "医学统计分析系统",
          description: "医学统计分析系统平台",
          link: "#",
          icon: "src/assets/img/Card/3.png"
        },
        {
          title: "人工智能药物发现与设计理论基础-AIDD",
          description: "人工智能药物发现与设计理论基础平台",
          link: "#",
          icon: "src/assets/img/Card/4.png"
        },
        {
          title: "中药网络药理学和毒理学分析系统",
          description: "中药网络药理学和毒理学分析系统平台",
          link: "#",
          icon: "src/assets/img/Card/2.png"
        }
      ],
      tabsData: [
        {
          title: "蛋白质结构预测",
          icon: "icon-mubiao",
          content:
              "从蛋白质的氨基酸序列出发预测其3D结构，为生物信息学与理论化学所追求的重点之一。",
        },
        {
          title: "虚拟筛选",
          icon: "icon-kangti",
          content:
              "通过计算模拟筛选出潜在药物，极大加速新药开发进程。",
        },
        {
          title: "分子生成",
          icon: "icon-fenzibingli",
          content:
              "利用AI技术生成分子结构并优化药物特性。",
        },
        {
          title: "ADMET 预测",
          icon: "icon-yuce",
          content:
              "基于深度学习预测药物的吸收、分布、代谢、排泄和毒性。",
        },
        {
          title: "合成路线规划",
          icon: "icon-hexinkongjian",
          content:
              "提供优化的合成路线，帮助化学家缩短药物研发周期。",
        },
        {
          title: "抗体",
          icon: "icon-kangti",
          content:
              "抗体药物的设计与优化。",
        },
      ],
    };
  },
};
</script>

<style lang="scss" scoped>
html, body {
  height: 100%;
  margin: 0;
  padding: 0;
}


.index {
  background-color: #f5f6f7;
  /* banner */
  .banner {
    .banner-container {
      width: 100%;
      height: 500px;
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
      max-height: 600px;
      height: 100%;
      object-fit: cover;
    }

    /* Swiper 样式 */
    .swiper-pagination {
      bottom: 20px;
    }

    .section-title {
      position: relative;
      display: flex;
      align-content: center;
      justify-content: center;
      font-size: 36px;
      font-weight: bold;
      color: var(--primary-color);
      text-align: center;
      margin-top: 50px;
    }

    .section-title::after {
      content: "";
      position: absolute;
      width: 100%;
      height: 10px;
      left: 0;
      bottom: 0;
      background-color: var(--primary-color);
      opacity: .1;
    }
  }

  /* 主要功能 */
  .card, .grid {
    display: grid;
    //display: flex;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
    padding: 30px 10px;
    justify-items: center;
    align-items: stretch;


    .card-icon {
      width: 300px;
      height: auto;
      overflow: hidden;
      margin: 0 auto;
    }
  }
}
</style>
