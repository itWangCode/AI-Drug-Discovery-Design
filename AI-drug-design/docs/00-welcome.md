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

[DeepProfiler](https://github.com/itWangCode/AI-drug-design) Drug design and discovery affects various aspects of human health and dramatically impacts the pharmaceutical market. However, investments in a new drug often go unrewarded due to the long and complex process of drug research and development (R&D). With the advancement of experimental technology and computer hardware, artificial intelligence (AI) has recently emerged as a leading tool in analyzing abundant and high-dimensional data. Explosive growth in the size of biomedical data provides advantages in applying AI in all stages of drug R&D. Driven by big data in biomedicine, AI has led to a revolution in drug R&D, due to its ability to discover new drugs more efficiently and at lower cost. This review begins with a brief overview of common AI models in the field of drug discovery; then, it summarizes and discusses in depth their specific applications in various stages of drug R&D, such as target discovery, drug discovery and design, preclinical research, automated drug synthesis, and influences in the pharmaceutical market. Finally, the major limitations of AI in drug R&D are fully discussed and possible solutions are proposed.

```{figure} img/platform.png
---
name: home-fig
---
Flowchart showing our platform of AIDD.
```

## Cell Painting CNN

```{figure} images/CellPaintingCNN.png
---
name: cp-cnn
---
The Cell Painting CNN can process the 5 image channels together to produce single-cell features.
```

If you are profiling [Cell Painting images](https://www.nature.com/articles/nprot.2016.105), you can now use our _**Cell Painting CNN**_ model to profile your experiments out of the box! No need to train a separate model for Cell Painting. [Our analysis](https://www.biorxiv.org/content/10.1101/2022.08.12.503783v1.full) indicates that the Cell Painting CNN generalizes better to new treatments because it has been trained at large scale with diverse phenotypic data. You can download the [pre-trained model]() and follow the instructions for [profiling]() in this guide to get started.
