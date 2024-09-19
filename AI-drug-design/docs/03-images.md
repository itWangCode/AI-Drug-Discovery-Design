# 3. Images and segmentation masks

## **3.1 Images**

DeepProfiler expects either TIFF or PNG files with images of cells. The image channels are expected to be stored in separate 
files, and their paths can be organized as needed in the project and documented in the metadata file. The size of images is, 
in principle, flexible and DeepProfiler can work with different resolutions and image dimensions. The workflow of DeepProfiler
is standard and compatible with most high-throughput microscopy systems.

## **3.2 Dataset compression and illumination correction**

The compression tool is primarily useful when preparing a dataset for training a new model. Compression improves training 
efficiency when the image collection used for training is too large (think TBs of imaging data) and it needs to be read 
multiple times over several training epochs. Then, image compression can make training feasible for a diversity of cellular 
phenotypes resulting in faster image loading. 

```{admonition} Note
:class: tip
Compression is not necessary for profiling cells (feature extraction). If you have access to a pre-trained model (e.g. the Cell Painting CNN), then DeepProfiler can extract features from cells without compressing TIFF images.
```


The compression tool assumes that images come from high-throughput experiments and are organized in wells and plates. Then, 
the procedure starts by computing illumination statistics, applying illumination correction functions to whole images and 
finally compressing TIFF images with PNG format. We designed this functionality to compress images as much as possible 
while losing the minimum amount of information. In our evaluations, compressing images has a marginal impact on downstream 
analysis. To run compression, you need to run the `prepare` command, which runs the pipeline described above, 
as follows:

```
python3 deepprofiler --root=/home/ubuntu/project/ --config filename.json prepare
```


## **3.2 Masking cells**

The pixels that belong to cells in an image can be identified using segmentation algorithms, such
as those available in [CellProfiler](https://cellprofiler.org/). The segmentation boundaries can be stored as binary images
with the outlines of cells in white on a black background. These outlines are the format used in DeepProfiler to mask cells
and isolate the content of single cells for training neural networks and computing features. Masking cells is optional,
and you can do training and profiling with cells in context without the masks.

Masking the context of cells may be useful for some projects. However, in our experiments on Cell Painting data, we found
that masking cells can reduce the performance of learning algorithms and downstream analysis. If you want to preserve
cell context for your study, we recommend skipping cell masking. Otherwise, you need to complete the following two steps
described below.

To mask cells, you first need to segment them using an external tool like [CellProfiler](https://cellprofiler.org/) or 
[Ilastik](https://www.ilastik.org/) and save the binary image of their outlines (see example figure). Save these images
in the `input/outlines` directory. Next, you need to create a CSV file with the list of the outline images with three
additional columns: plate, well and site. Save this file in the `input/metadata` directory. The final step is to update
the configuration file ([Section 3](#heading=h.5i3187icaj4t)) to let DeepProfiler know that you want to use these outlines
for masking the cells. Specifically, the `mask_objects `setting under `locations` must be set to `true` in the configuration
file to use masks (more details below).
