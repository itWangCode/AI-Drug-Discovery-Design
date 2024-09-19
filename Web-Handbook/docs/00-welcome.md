# Welcome to DeepProfiler

[AIDD](https://github.com/itWangCode/AI-drug-design) uses representation learning for extracting phenotypic information from microscopy images of cells. This guide describes how to install and run DeepProfiler using the provided example data. After completing this guide, you should have a running version of DeepProfiler, and a general understanding of how to structure your data to use this software, as well as the output that it produces.

```{figure} images/image1.png
---
name: home-fig
---
Flowchart showing the inputs and outputs of DeepProfiler.
```

In a nutshell, DeepProfiler requires three types of input: 1) microscopy images, 2) metadata describing the organization
of images in an experiment, and 3) metadata files indicating the locations of single cells in images. Then, DeepProfiler
can be run in two modes: 1) training a neural network model that learns to extract features from images, and 2) profiling
single cells by running an existing model. The output of DeepProfiler during training is a model file with the learned 
parameters of a neural network, which can be shared or later reused. During profiling, DeepProfiler creates files with 
single-cell feature embeddings for the images listed in the metadata file.

What DeepProfiler does not do: 1) it does not identify the location of single cells or segment cells from the images. 
These locations need to be obtained using other software, such as [CellProfiler](https://cellprofiler.org/), 
[Ilastik](https://www.ilastik.org/), or [Cellpose](https://www.cellpose.org/). 2) DeepProfiler does not create aggregated
profiles of cell populations. The single-cell feature embeddings need to be processed separately to perform the 
corresponding downstream analysis, using tools such as [pycytominer](https://github.com/cytomining/pycytominer).

## Cell Painting CNN

```{figure} images/CellPaintingCNN.png
---
name: cp-cnn
---
The Cell Painting CNN can process the 5 image channels together to produce single-cell features.
```

If you are profiling [Cell Painting images](https://www.nature.com/articles/nprot.2016.105), you can now use our _**Cell Painting CNN**_ model to profile your experiments out of the box! No need to train a separate model for Cell Painting. [Our analysis](https://www.biorxiv.org/content/10.1101/2022.08.12.503783v1.full) indicates that the Cell Painting CNN generalizes better to new treatments because it has been trained at large scale with diverse phenotypic data. You can download the [pre-trained model]() and follow the instructions for [profiling]() in this guide to get started.
