# Welcome to AI-Drug-Design

## 人工智能辅助药物发现与设计

## Artificial Intelligence-assisted Drug Discovery and Design

## 全球唯一的实战开源从0基础入门学习AIDD，手把手教学入门到博士大佬级别的教程

### The only practical open source in the world to learn AIDD from the 0-based entry, hand-to-hand teaching entry to the doctoral level tutorial.

让我为大家简要介绍一下我负责的领域——**人工智能辅助药物发现与设计**。为了更好地帮助大家理解这一复杂的前沿技术，我将通过中文为大家进行讲解，特别是为那些可能在语言上有所障碍的同学提供支持。尽管这种内容通常更适合以英语呈现，但为了确保大家能够更好地掌握核心概念并迅速上手，我选择用中文为大家提供更加直观的学习路径。

**人工智能辅助药物发现与设计**是一种利用人工智能（AI）技术来加速和优化药物开发过程的方法。传统药物研发周期长、成本高、成功率低，而 AI 能够通过大数据处理、模型预测和自动化分析，大幅提升药物设计的效率和准确性。

### **AI 在药物设计中的优势**

- **加速研发周期**：AI 能够快速筛选大量化合物，减少实验筛选的工作量。
- **提高准确性**：AI 能够通过大规模数据训练模型，提升药物设计中的预测准确性。
- **成本降低**：由于减少了实验的重复性和失败率，AI 能够有效降低药物研发成本。
- **个性化药物设计**：AI 能帮助设计个性化药物，针对特定患者或疾病特征，优化治疗效果。

人工智能在药物发现与设计中的应用，使得药物开发过程更加智能化、自动化。通过化合物筛选、靶标预测、药物生成、ADMET 分析等关键步骤，AI 能有效加速药物研发的进程，同时提高设计的准确性和效率。

[AI-Drug-Design](https://github.com/itWangCode/AI-drug-design) affects various aspects of human health and dramatically impacts the pharmaceutical market. However, investments in a new drug often go unrewarded due to the long and complex process of drug research and development (R&D). With the advancement of experimental technology and computer hardware, artificial intelligence (AI) has recently emerged as a leading tool in analyzing abundant and high-dimensional data. Explosive growth in the size of biomedical data provides advantages in applying AI in all stages of drug R&D. Driven by big data in biomedicine, AI has led to a revolution in drug R&D, due to its ability to discover new drugs more efficiently and at lower cost. This review begins with a brief overview of common AI models in the field of drug discovery; then, it summarizes and discusses in depth their specific applications in various stages of drug R&D, such as target discovery, drug discovery and design, preclinical research, automated drug synthesis, and influences in the pharmaceutical market. Finally, the major limitations of AI in drug R&D are fully discussed and possible solutions are proposed.

```{figure} img/platform.png
---
name: home-fig
---
Flowchart showing our platform of AIDD.
```

## 目录

## 第一节 基础部分

0. 人工智能在医学中的应用
   - Python基础
   - Numpy、Pandas
   - Matplotlib
   - 机器学习和Scikit-Learn
   - 深度学习
   - CADD
   - 图神经网络

1. Python和机器学习基础
   - 分子的文本表示：SMILES
   - 分子的向量表示：描述符和指纹
   - RDKit简介
   - 经典机器学习模型：线性回归、随机森林、支持向量机

2. 公开可用的小分子数据集的探索
   - 生物活性分子 ChEMBL 数据库
   - ZINC 数据库
   - PubChem 数据库
   - 探索性数据分析 (EDA)
   - 定量构效关系 (QSAR) 和虚拟筛选 (VS)

3. 图神经网络
   - 神经网络架构和训练
   - 分子图、原子特征化
   - 消息传递神经网络
   - 图卷积神经网络
   - 可解释性：Grad-CAM

4. 分子对接
   - 分子数据格式：SMI、SDF、MOL2、PDB
   - 力场
   - 蛋白质折叠
   - 使用 AutoDock Vina、Smina、QuickVina 进行分子对接
   - 交互指纹
   - 药效团

5. 深度生成模型
   - 自动编码器
   - 循环神经网络
   - SMILES生成器：ReLeaSE 和 REINVENT
   - 基于图的生成模型：JT-VAE
   - 分子特性优化：强化学习和贝叶斯优化

6. 蛋白质深度学习
   - 简化的蛋白质图表示
   - 体素网格表示
   - 用于编码蛋白质表面的网格表示
   - 3D卷积神经网络

7. 不确定性预测
   - 任意和认知的不确定性
   - 共形预测

## 第二节 化学信息学

1. 基础知识
   - 化学信息学 RDKit 简介
   - Pandas 在化学信息学中的应用
   - SMILES 教程
   - SMARTS 教程
   - 反应列举基础知识
   - 立体异构体和互变异构体列举

2. 使用 Datamol 和 Molfeat 精简化学信息学工作流
   - 数据处理、描述符和聚类

3. 聚类
   - K-Means 聚类
   - Taylor-Butina 聚类

4. 复杂的化学信息学分析
   - Chembl 系统分析
   - 基于 Chembl 数据库的药物数据分析
   - 基于 BindingDB 中的专利数据进行分析

5. SAR 分析
   - 脚手架识别
   - R-group 分析
   - 位置模拟扫描分析
   - Free-Wilson 分析
   - 匹配的分子对
   - 匹配的分子集

6. 机器学习模型
   - 构建并测试一个 QSAR 模型
   - 分类模型构建与比较
   - 回归模型构建与比较

7. 主动学习
   - 主动分类
   - 主动回归
   - 主动形状搜索

8. 神经网络潜能
   - 使用 Auto3D 的同分异构体能量预测

## 第三节 实战部分

### 1. **化合物数据采集与初步处理**

   - 01_从 ChEMBL 化合物数据采集
   - 02_从 PubChem 获取数据
   - 03_从 KLIFS 获取数据
     - 03_1 完整项目：《基于机器学习的生物活性预测》
   - 04_查询在线 API 网络服务

### 2. **分子过滤与预处理**

   - 05_分子过滤：ADMET 和先导化合物相似标准
     - 05_1 完整项目：《基于机器学习与深度学习的分子ADMET预测》
     - 05_2 完整项目：《基于GNN的分子毒性预测》
   - 06_分子过滤：不需要的子结构
     - 06_1 完整项目：《基于ADMET和RO5的分子筛选与化合物相似性的配体筛选》

### 3. **分子表示与相似性分析**

   - 07_分子表示
   - 08_基于配体的筛选：化合物相似性
   - 09_复合聚类
   - 10_最大公共子结构

### 4. **药效团与脱靶预测**

   - 11_基于配体的药效团
   - 12_结合位点相似性和脱靶预测

### 5. **蛋白质数据获取与结合位点检测**

   - 13_蛋白质数据获取：蛋白质数据库（PDB）
   - 14_结合位点检测

### 6. **蛋白质-配体对接**

   - 15_蛋白质-配体对接
     - 15_1 预测生物活性分子的逆合成可及性
   - 16_蛋白质-配体相互作用
   - 17_NGLview 高级使用

### 7. **分子动力学模拟**

   - 18_分子动力学模拟
   - 19_分析分子动力学模拟

### 8. **先导化合物优化与自动化流程**

   - 20_先导化合物优化的自动化流程

### 9. **机器学习与分子性质预测**

   - 21_基于配体的筛选：机器学习
   - 22_基于配体的筛选：神经网络
   - 23_基于 RNN 的分子性质预测
   - 24_基于 GNN 的分子性质预测
   - 25_分子特性预测转换器
   - 26_不确定性估计

### 10. **RNA Aptamer 设计与分析**

#### **1. 数据采集与准备**

- **27_1 RNA Aptamer 数据来源**
  - 数据来源：RNAapt3D (https://rnaapt3d.medals.jp/)
- **27_2 数据清洗与预处理**

#### **2. RNA 结构预测**

- **28_1 一级结构预测**
- **28_2 结构可视化与分析**

- **29_1 二级结构预测**
- **29_2 能量最小化与折叠稳定性分析**
  - ΔG（自由能）和折叠稳定性图

#### **30_RNA Aptamer 结合位点分析**

- **30_1 RNA Aptamer 与靶标的结合位点预测**
- **30_2 结合能计算与优化**

#### **3. 药物设计与优化**

- **30_3 基于 RNA Aptamer 的药物设计**
- **30_4 药物化学与虚拟筛选**

#### **5. 分子动力学模拟与实验验证**

- **30_5 分子动力学模拟**
- **30_6 实验验证**

### 11. **激酶相似性与分析**

   - 31_激酶相似性：序列
   - 32_激酶相似性：激酶口袋（KiSSim 指纹）
   - 33_激酶相似性：相互作用指纹
   - 34_激酶相似性：配体概况
   - 35_激酶相似性：不同观点比较
   - 36_基于激酶片段库设计激酶抑制剂

### 12. **蛋白质-配体相互作用与预测**

   - 37_蛋白质-配体相互作用预测
     - 完整项目：《项目实战：基于Transformer的有机化学反应产量预测 （Prediction of chemical reaction yields using deep learning）》
     - 完整项目：《项目实战：Mapping the space of chemical reactions using attention-based neural networks》
     - 完整项目：《项目实战：基于图数据的小分子化合物生成模型（A Graph to Graphs Framework for Retrosynthesis Prediction）》
     - 完整项目：《项目实战：基于NLP的抗体生成模型（Generative language modeling for antibody design）》

### 13. **高级建模与虚拟筛选**

   - 38_基于 KLIFS 数据跑 3D 动力学
   - 39_基于共识对接的一体化结构虚拟筛选（蛋白质制备、对接、结合位点选择、重新评分和排序）

### 14. **可视化与编码工具**

   - 40_One-Hot 编码
   - 41_使用代码绘制分子图



## **第四节 研究基因到免疫浸润**

#### **1. Introduction**
- 研究目标：探索基因与免疫浸润之间的关系
- 背景介绍：免疫浸润的重要性及其在基因表达中的影响

#### **2. Software 环境配置**
- 安装与配置所需的软件工具（如 R、Python、Bioconductor ）

#### **3. 数据下载与预处理**
- 从 GEO、TCGA 等数据库下载基因表达数据
- 数据标准化和清洗

#### **4. 数据注释** Annotation (ANN)
- 使用注释文件（如 GTF 或 GFF 文件）对基因表达数据进行注释
- 工具：`biomaRt`、`org.Hs.eg.db`

#### **5. SVA (Surrogate Variable Analysis)**
- 使用 SVA 校正批次效应
- 代码实现：`sva`包中的 `ComBat` 或 `svaseq` 方法

#### **6. 差异基因分析 **Differential Gene Expression (Diff)
- 使用 `limma`、`DESeq2` 等工具进行差异基因分析
- 生成差异表达基因（DEGs）列表

#### **7. 火山图绘制** Volcano Plot
- 使用差异分析的结果绘制火山图
- 代码实现：`ggplot2`、`EnhancedVolcano`包

#### **8. 富集分析**
- **08. Metascape**
  - 在 Metascape 网站上进行通路和功能富集分析

- **09. Gene Ontology (GO)**
  - 使用 GO 进行基因功能注释和富集分析
  - 工具：`clusterProfiler`、`topGO`

- **10. KEGG 富集分析**
  - 使用 KEGG 数据库进行信号通路富集分析
  - 工具：`clusterProfiler`、`KEGGREST`

#### **11. 蛋白质互作网络**
- **11. Protein-Protein Interaction (PPI)**
  - 构建蛋白质-蛋白质互作网络
  - 工具：`STRING` 数据库、`Cytoscape`

#### **12. 随机森林模型Random Forest**
- 构建随机森林模型，筛选重要基因

#### **13. 热图绘制Heatmap**
- 绘制差异基因的表达热图

#### **14. 基因评分计算**Gene Score
- 根据差异基因计算基因评分
- 代码实现：基于基因表达值的综合评分方法

#### **15. 神经网络模型Neural Network**
- 使用神经网络模型对基因表达进行预测
- 工具：`neuralnet`包

#### **16. ROC 曲线分析Receiver Operating Characteristic (ROC)**
- 绘制 ROC 曲线，评估模型的准确性
- 工具：`pROC` 包

#### **17. 基因评分测试Test Gene Score**
- 测试基因评分模型的准确性和可行性

#### **18. 神经网络预测测试Test Neural Network Prediction**
- 测试神经网络模型的预测能力

#### **19. ROC 测试Test ROC**
- 使用测试数据集验证 ROC 曲线

#### **20. CIBERSORT 分析**
- 使用 CIBERSORT 分析基因表达数据，估算免疫细胞的比例

#### **21. 柱状图绘制**Barplot
- 绘制免疫细胞比例的柱状图
- 工具：`ggplot2`

#### **22. 小提琴图绘制Violin Plot**
- 绘制基因表达与免疫细胞浸润之间的关系图

