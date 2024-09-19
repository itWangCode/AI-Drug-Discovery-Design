
# Welcome to DeepProfiler

DeepProfiler aims to use deep learning and representation learning for extracting phenotypic information from microscopy images of cells. This guide describes how to install and run DeepProfiler using the provided example data. After completing this guide, you should have a running version of DeepProfiler, and a general understanding of how to structure your data to use this software, as well as the output that it produces.

```{figure} images/image1.png
---
name: home-fig
---
Flowchart of the inputs and outputs of DeepProfiler.
```

In a nutshell, DeepProfiler requires three types of input: 1) microscopy images, 2) metadata describing the organization of images in an experiment, and 3) metadata files indicating the locations of single cells in images. Then, DeepProfiler can be run in two modes: 1) training a neural network model that learns to extract features from images, and 2) profiling single cells by running an existing model. The output of DeepProfiler during training is a model file with the learned parameters of a neural network, which can be shared or later reused. During profiling, DeepProfiler creates files with single-cell feature embeddings for the images listed in the metadata file.

What DeepProfiler does not do: 1) it does not identify the location of single cells or segment cells from the images. These locations need to be obtained using other software, such as [CellProfiler](https://cellprofiler.org/) or [Ilastik](https://www.ilastik.org/). 2) DeepProfiler does not create aggregated profiles of cell populations. The single-cell feature embeddings need to be processed separately to perform the corresponding downstream analysis, using tools such as [pycytominer](https://github.com/cytomining/pycytominer). We include a short tutorial for creating aggregated profiles with pycytominer in Section 5.


# 1. Install DeepProfiler

There are two options for installation: installing DeepProfiler from source and using a docker container. We recommend you use docker if your environment needs to be quickly recreated (e.g., virtual machines in the cloud) or if you plan to do large scale processing. Install from source when you need flexibility to adjust code and configurations, for instance when testing new models or for adjusting advanced training settings. If using a docker container, download a [Docker Image](https://hub.docker.com/r/michaelbornholdt/deep_profiler/tags) using the command `docker pull michaelbornholdt/deep_profiler:aws-0` then proceed to step 2. The instructions in this section assist you with installing DeepProfiler from source in a Linux environment. The provided code snippets assume the use of Ubuntu but any Linux distribution can work for installing DeepProfiler; just make sure your environment is configured accordingly.


## **1.1 Clone the repository**

On the command line, enter the directory where you want to install DeepProfiler, then clone the GitHub repo:


```
git clone https://github.com/broadinstitute/DeepProfiler.git
```


Alternatively, you can fork it to keep track of your own changes, and eventually contribute back.


## **1.2 Install dependencies and packages**

First make sure that your python installation is up to date. DeepProfiler runs in Python 3.6 or higher (Python 3.8 recommended).


```
sudo apt update
```


If you don’t have sudo, use `conda update --all`


```
sudo apt install python3
```


We strongly advise using a virtual environment for DeepProfiler. This will help not to interfere with system-wide installed python packages. Virtualenv ([https://pypi.org/project/virtualenv/](https://pypi.org/project/virtualenv/)) can be installed with the following command:


```
sudo install virtualenv
```


If you don’t have sudo privileges in your system, use:


```
pip3 install virtualenv
```


Next, you will be able to create a virtual environment in a current directory:


```
virtualenv -p python3 deepprofenv
```


To activate the created virtualenv use:


```
source ./deepprofenv/bin/activate
```

```{admonition} Note
:class: tip
If you have access to a GPU, make sure that you have the correct drivers and the `tensorflow` package installed and configured correctly. You can follow this link for more details about how to install TensorFlow with GPU support in your machine: [https://www.tensorflow.org/install](https://www.tensorflow.org/install) . The command to check if the correct GPU is being utilized is `nvidia-smi` .
```

Now you can enter the DeepProfiler directory and install it using pip. This will pull the missing dependencies and will also create runnable packages in your clone.


```
cd DeepProfiler/
pip install -e .
python3 deepprofiler
```

```{admonition} Note
:class: tip
The above environment does not include the package of ‘Imagecodecs’, that needs to be installed separately.
```

The following is the expected output of running the DeepProfiler entry point:


```
Using TensorFlow backend.
Usage: deepprofiler [OPTIONS] COMMAND [ARGS]...


Options:
  --root PATH         Root directory for DeepProfiler experiment
  --config TEXT       Path to existing config file (filename in project_root/inputs/config/)
  --cores INTEGER     Number of CPU cores for parallel processing (all=0) for prepare command
  --gpu TEXT          GPU device id (the id can be checked with nvidia-smi)
  --exp TEXT          Name of experiment, this folder will be created in project_root/outputs/
  --logging TEXT      Path to file with comet.ml API key (filename in project_root/inputs/config/)
  --sample TEXT       Name of the folder with single-cell sample (output for sample-sc command, input for training with sampled crop generator or online labels crop generator)
  --metadata TEXT	Metadata filename
  --help              Show this message and exit.


Commands:
  download-bbbc021
  prepare
  profile
  setup
  split
  train
  traintf2
  export-sc
```



## **1.4 Troubleshooting**

Some dependencies need to be manually installed depending on your environment. If you pulled the latest version of DeepProfiler in an existing clone, try reinstalling it again as in step 1.2 to make sure the dependencies are still up to date.


# 2. Project structure

After installing DeepProfiler on your machine, the next step is to create a project directory structure that holds your data with the required inputs and space for generated outputs.


## **2.1 Initialize your project**

In the following sections, we assume that you have an Ubuntu environment and a user account named “ubuntu”. Make sure to replace the example path (`/home/ubuntu`) with the directories that you are using in practice. Go to your base path and create an empty directory for your project (called `project`):


```
cd /home/ubuntu
mkdir project
```


Go back to the DeepProfiler to initialize the contents of your new project directory:


```
cd DeepProfiler
python3 deepprofiler --root=/home/ubuntu/project --config=config.json setup
```

```{admonition} Note
:class: tip
Note that the root project directory needs to exist before running this command.

Also, the root and the config file flags are always required, and the config file does not need to exist for the `setup` command to run. The experiment name is optional.
```


The following is the expected output:


```
Using TensorFlow backend.
Directory exists:  /home/ubuntu/project/
Creating directory:  /home/ubuntu/project/inputs/locations/
Creating directory:  /home/ubuntu/project/inputs/config/
Creating directory:  /home/ubuntu/project/inputs/images/
Creating directory:  /home/ubuntu/project/inputs/metadata/
Creating directory:  /home/ubuntu/project/inputs/pretrained/
Creating directory:  /home/ubuntu/project/outputs/intensities/
Creating directory:  /home/ubuntu/project/outputs/compressed/images/
Creating directory:  /home/ubuntu/project/outputs/compressed/metadata/
Creating directory:  /home/ubuntu/project/outputs/results/
Creating directory:  /home/ubuntu/project/outputs/results/checkpoint/
Creating directory:  /home/ubuntu/project/outputs/results/logs/
Creating directory:  /home/ubuntu/project/outputs/results/summaries/
Creating directory:  /home/ubuntu/project/outputs/results/features/
```


Resulting in a directory structure like this:


```{figure} images/image2.png
---
width: 300px
name: dir-fig
---
Illustration of the project directory structure expected by DeepProfiler.
```

```{admonition} Note
:class: tip
You can create this directory structure manually if you want, but make sure you follow these conventions because DeepProfiler expects these directories to exist and does not explicitly validate if that is the case.
```



## **2.2 Add project data**

The directories created in the previous step are empty, so your next task is to put your project data in the right place. A small example dataset can be obtained from our web servers, so you can test and debug DeepProfiler issues easily. Follow these steps to download the example data:


```
cd /home/ubuntu
wget https://imaging-platform.s3.amazonaws.com/projects/deepprofiler-examples/example-data.tar.gz
tar -xzf example-data.tar.gz
```


The example dataset contains a few images from the [BBBC021 collection](https://bbbc.broadinstitute.org/BBBC021), together with the necessary files to configure the DeepProfiler project. Copy the essential data to the corresponding input directories, including the provided configuration file.


```
cp -R example-data/BBBC021-small/images/* project/inputs/images/
cp example-data/BBBC021-small/metadata/* project/inputs/metadata/
cp -R example-data/BBBC021-small/locations/* project/inputs/locations/
cp example-data/config.json project/inputs/config/
```


More information about some of these files can be found below.

## **2.3 The index.csv file**

The index.csv file (located in _project/inputs/metadata/index.csv) _is critical for running DeepProfile. It follows a comma-separated-values format with a header, contains information about the experiment, and lists all images in your project. DeepProfiler uses this file to guide image sampling for running learning algorithms, and to find the images that we want to process. This file is expected to contain metadata to identify the context of images in the physical experiment that produced them, for instance, identifiers of plates, wells and fields of view (Figure 3). DeepProfiler assumes that each row in the file represents one (multi-channel) field of view. The following list indicates the columns that the index.csv file is expected to have:



1. `Metadata_Plate`: Name or identifier of the plate (i.e., highest level of experimental organization), e.g. Week1_22124. The field header cannot be renamed.
2. `Metadata_Well`: Position in the plate, e.g. B08 (i.e., middle level of organization within plates). The field header cannot be renamed.
3. `Metadata_Site`: A microscope acquires images in different sites within each well (i.e., lowest level organization within wells). For instance, sites may cover a 4x4 grid or a 9x9 grid, depending on resolution and other factors. The site identifier for each image goes here, e.g. s3. The field header cannot be renamed.
4. `Plate_Map_Name`: Name or identifier of the plate layout used, e.g. Week1. The field header cannot be renamed.
5. `Channel_Name`: Relative path to the image file of each channel. An experiment may have multiple imaging channels (i.e., colors) and DeepProfiler assumes that each channel is stored in a separate image file (all channels stored in the same file is not currently supported). Therefore, to put together all the channels of a single image, the index.csv file will need to have multiple _channel_name_ columns. These columns can be renamed as necessary, and should point to the corresponding image files using a path relative to the root directory. For example, an assay with DNA, Actin, and Tubulin stains will have three channel columns named accordingly, with entries in each column pointing to the corresponding image file. The field may have different names.
6. `Treatment`: We assume that cells in a well have been treated in a biologically meaningful way or represent different experimental conditions. This column keeps track of that information, which may have other names (in the provided example data, it is called “Compound_Concentration”). It is useful as an identifier of the type of biological experiment, treatment, perturbation or condition of cells observed in the images. This column must be a biologically meaningful label that could be used by DeepProfiler for training purposes. May have different names.
7. `Replicate`: Number or identifier indicating which repetition of the treatment an image corresponds to.

These are the minimum columns required in the index file. You can append more columns with information specific to your experiment as needed, to keep track of other metadata in your project. Notice that the order of columns is not important, as long as these are available. The meaning of the columns can be interpreted differently according to your problem, for instance, instead of plates, you may be interested in subjects or patients. However, the three levels of organization (plate, well, site) are expected, even if you don’t explicitly use it (e.g. set wells to a constant string if it does not apply to your data). The name of certain columns can be changed as well and later associated with the expected information in the configuration file [(Section 3](#heading=h.5i3187icaj4t)).


```{figure} images/image3.png
---
name: plate-fig
---
Schematic of plates, wells and sites, which are three metadata fields required by DeepProfiler in the index.csv file.
```


Example of index.csv file:

```{image} images/image4.png
:alt: index file
:align: center
```


## **2.4 Masking cells**

The pixels in an image that belong to cells can be identified using segmentation algorithms, such as those available in [CellProfiler](https://cellprofiler.org/). The segmentation boundaries can be stored as binary images with the outlines of cells in white on a black background. These outlines can be used in DeepProfiler to mask cells and isolate the content of single cells for training neural networks and computing features. This may be useful for projects where the structure of single cells determines the phenotype of interest. In our experience, masking cells can sometimes reduce the performance of learning algorithms in identifying phenotypic information. If cell context is necessary for the study of phenotypic variations in your dataset, we recommend you skip cell masking.

To mask cells, you first need to segment them using an external tool like [CellProfiler](https://cellprofiler.org/) or [Ilastik]([Ilastik.org](https://www.ilastik.org/)) and save the binary image of their outlines. Save these images in the `input/outlines` directory. Next, you need to create a csv file with the list of the outline images with three additional columns: plate, well and site. Save this file in the `input/metadata` directory. The final step is to update the configuration file ([Section 3](#heading=h.5i3187icaj4t)) to let DeepProfiler know that you want to use these outlines for masking the cells. Specifically, the `mask_objects `setting under `locations` must be set to `true` in the configuration file to use masks (more details below).


# 3. The configuration file

The configuration file is a text file in JSON format that organizes various settings for one experiment. If you need to test different configurations, you can create different configuration files and run DeepProfiler with each. DeepProfiler searches for the configuration file in the `inputs/config/` directory, which you can use to store various configuration files. Note that the `--config` flag does not need you to specify the full path of the file, just the name as it is assumed to be stored in the `inputs/config/` directory.

The configuration file is organized in four main sections as follows. We’ve included specific recommendations where possible. For more details, check out our paper (link). For generating this config file for your own project, look at the descriptions below together with the provided examples of index.csv and config.json files.



1. `dataset`: description of your image collection with basic general information
    * `metadata`
        * `label_field`: _(string)_ column in the index.csv file corresponding to the treatments or biologically relevant labels of images.
        * `control_value` : _(string)_ identifier or name of control samples in the column above (used to gather illumination statistics).
    * `images`
        * `channels`: _(array of strings)_ list of image channels used for profiling. The list contains the names of columns in the index.csv file that hold the location of images for each channel. DeepProfiler assumes each channel is stored as a separate image, and also that the path listed in the index.csv file is relative to the input/images directory (instead of absolute paths). This facilitates moving the project to another machine in a different location.
        * `file_format`: _(string)_ extension of image files, e.g. tiff, tif, png.
        * `bits`: _(int)_ pixel bit depth. Not necessary for any analysis, only used for compression purposes. 8-bit and 16-bit images are currently supported.
        * `width`: _(int)_ width of the input image in pixels
        * `height`: _(int)_ height of the input image in pixels
    * `locations`: parameterize the way in which DeepProfiler will search for single cells in images for training and for profiling.
        * `mode`: _(string)_ this field indicates if images will be processed at single cell resolution or in full image mode. It only accepts two strings: `single_cells` - activates single-cell analysis mode, thus, requiring cell locations to be stored in the `inputs/locations/` folder (Section XXX); `full_image` - activates full image analysis (no need for locations files).
        * `box_size`: _(int)_ specifies the size in pixels of the bounding box used to crop single cells out of images. The value is used for both the width and the height of the box (a square box). This value is used even in `full_image` mode, in which case the image will be resized to these dimensions. Note that DeepProfiler enforces a fixed input size because that is what neural network models usually expect. The box size should be selected to fully cover a typical cell in the experiment. It is OK if large cells are cut a bit, as long as this is relatively rare compared to the normal cell size. Also, it is OK if cells appear with neighboring cells in the same box, which we call “single cells in context” or can be fixed by masking (see below).
        * `area_coverage`: _(float)_ useful only in `full_image` mode, specifies the fraction of the image to be covered by cropping before resizing to the dimensions configured in `box_size`. For instance, consider an image of 1080x1080 pixels and `box_size=256`; an `area_coverage=0.5` will result in cropping a region of 540x540 pixels from the original image and then resizing it to 256x256.
        * `mask_objects`: _(bool)_ true or false, indicates whether cells should be masked using the cell outlines in `input/outlines`. Optional, the recommended value at the moment is false (see more information below).
2. `prepare`: configuration for illumination correction and compression, which are run sequentially with the command `prepare`. This command is useful for preparing training datasets that can be read efficiently repeated times from disk. This is optional if you only need to do feature extraction and profiling with a pre-trained model.
    * `illumination_correction`: parameters to run a prospective illumination correction algorithm that estimates the illumination correction functions for each channel in each plate.
        * `down_scale_factor`: _(float)_ the illumination correction functions are not computed at full resolution. This parameter tells DeepProfiler how small these functions should be. A common parameter is 4, for images of about 1024x1024 pixels, resulting in illumination correction functions of 256x256 pixels.
        * `median_filter_size`: _(int)_ size in pixels of the smoothing operator applied before aggregation of the illumination correction function. Usually set to 24 for images of 1024x1024 pixels.
    * `compression`:
        * `implement`: _(bool)_ true or false, whether compression is used for training and profiling. If true, other DeepProfiler commands will use the compressed images in the `output/compressed/` directory instead of the original images in the `input/images/` directory.
        * `scaling_factor`: _(float)_ make images a fraction of what they are. 1.0 means no scaling, 0.8 means resize to 80% of the current size in x and y. Re-scaling images results in smaller files that are faster to read during training, but loses spatial resolution, which is generally not recommended. Use a value different to 1.0 only if there is a good experimental reason.
3. `train`: parameters for training a deep learning model on your data.
    * `partition`:
        * `targets`: _(array)_ column names in the metadata (`index.csv` file) that want to be used as classification targets for training the neural networks. It currently uses only the first element in the list, e.g., `['Compound', 'Concentration']`, means that there are two columns in the `index.csv `file with that information, and that DeepProfiler will use `'Compound'` for training. The rest of the array is currently ignored, but is intended to be used in the future. If both columns are necessary for training, consider merging them in a single column, otherwise you can leave only one column name in the array i.e., `['Compound']`
        * `split_field`: _(string)_ column name in the `index.csv` file that indicates which images should be used for training and which ones for validation (or just ignored). This column may be one of the columns containing information about the experiment (e.g. plate id) or a custom-defined column with these decisions made by the analysis.
        * `training`: _(array)_ unique values in the `split_field` column of the `index.csv` file that indicate which images will be used for training. For example, if `split_field=Metadata_Plate`, this array should indicate which plates are intended to used for training e.g. `["plateA", "plateB", "plateC"]`.
        * `validation`: _(array)_ unique values in the `split_field` column of the `index.csv` file that indicate which images will be used for validation. This is the same as the `training` field above.
    * `model`: deep learning model parameters
        * `name`: _(string)_ deep learning model to be used, the name should be one of the models in the plugins folder. The default recommended model is `efficientnet` for weakly supervised learning. Other models currently supported include: `resnet` and `InceptionResNetv2` (supported only for pre-trained feature extraction, not for training).
        * `crop_generator`: _(string)_ strategy for cropping single cells from images. Crop generators are implemented in the plugins folder and can be extended with custom code if necessary. DeepProfiler currently has the following options implemented: 1) `crop_generator` is the main strategy for obtaining crops of single cells. It leverages the cell locations stored in `inputs/locations` and combines that information with images to generate crops with single cells. It can be used for training and for profiling, however, it is not recommended for training because it is not efficient enough for creating accurate models. This crop generator also works in `full_image` analysis mode. 2) `sampled_crop_generator`, this crop generator reads single-cell images pre-cropped and exported for training (see Section XXX). This is the recommended way for training new models.  3) `online_labels_cropgen`, used for training with online label smoothing using exported single-cell datasets as before. If analyzing the dataset in full_image mode, you should use the default value. 4)  `repeat_channel_crop_generator`, used for extracting features using networks pre-trained with the ImageNet dataset (RGB natural images). This crop generator transforms each gray-scale channel of your images into an RGB image to enable processing, and then concatenates the features of all channels in a single vector. This crop generator is only useful for profiling and should not be used for training. It can be used in `full_image` analysis mode.
        * <code>Augmentations: <em>(boolean)</em> </code>switch augmentation layer on and off. DeepProfiler uses data augmentation to generate models robust to certain transformations and noise. The transformations implemented in the augmentation layer are applied at random to images of single cells during training only, and include: 90 degree rotations, horizontal flips, brightness and contrast illumination perturbations on each channel separately.
        * <code>metrics</code>: <em>(array of strings)</em> contains names of metrics to monitor performance during training. It supports most of the [keras metrics](https://keras.io/api/metrics/), including <code>accuracy</code>. This applies for now only for the <code>train</code> command.
        * <code>epochs</code>: <em>(int)</em> number of epochs for training.
        * <code>initialization</code>: <em>(string)</em> strategy to set the initial model weights for training. Valid values are <code>Random</code> (supported by all models) or <code>ImageNet</code> (currently supported by ResNet and EfficientNet models only). Using ImageNet weights is a better initialization strategy in practice, and usually leads to improved performance.
        * <code>checkpoint_policy</code>: <em>(string)</em> or <em>(int)</em> checkpointing policy parameter (optional). Checkpoints are files that save the state of the model during training, because training sessions are usually long and may fail (or be interrupted by the system). Checkpoints help to recover the training session, or simply reuse the model after training. If the parameter is an integer number, then DeepProfiler saves model checkpoints every <code>checkpoint_policy</code> step. If the string <code>best</code> is used, then DeepProfiler saves only the best-performed checkpoint according to validation performance. By default, checkpoints are saved for every epoch.
        * <code>params</code>: model-specific values that depend on the plugin or architecture.
            * <code>learning_rate</code>: <em>(float)</em> initial learning rate for the optimizer.
            * <code>batch_size</code>: <em>(int)</em> number of samples per batch during training.
            * <code>conv_blocks</code>: <em>(int)</em> number of layers, or convolutional blocks. For ResNet valid values only include <code>50</code>, <code>101</code> and <code>152</code>.
            * <code>label_smoothing</code>:<code> </code>(<em>float</em>) label smoothing parameter for categorical cross entropy loss.
            * <code>online_label_smoothing:</code>(<em>float</em>) label smoothing if online labeling is used.
            * <code>online_lambda:</code> (<em>float</em>) online labeling regularization parameter.
        * <code>lr_schedule</code>: <em>(array or string)</em> strategy for decreasing the learning rate during training. There are three strategies supported:
            * 1) constant rate, which doesn’t require this parameter to be set (i.e. just remove this parameter from the config file).
            * 2) step schedule: changes the learning rate to a desired value at specific epochs. This strategy needs you to configure two arrays, ”epoch” for the epochs where the learning rate will be changed (integer numbers), and “lr” with the actual desired learning rate values (e.g. <code>{"epoch":[40, 80], "lr":[0.1, 0.01]}</code>). Both arrays are expected to be the same size.
            * 3) cosine decay, which increments the learning rate from zero to the initial learning rate using a linear function during the first five epochs. After that, every epoch reduces the learning rate according to the cosine decay. Use <code>"cosine"</code> to enable this option.
    * <code>sampling</code>: parameters to load images and crop single cells during training. Those parameters are only used for the default <code>crop_generator</code> (<code>"crop_generator")</code>, which is used for exporting single cells, among others.
        * <code>factor</code>: <em>(float)</em> fraction of crops from each image to be used for training (number between 0 and 1). This parameter can be used to prevent filling up the queue with example cells from a few images only. With a small sampling factor, the queue will have more diversity of cells cropped from a variety of images to create batches, improving the training performance. In this case, more epochs will be needed to reach optimal performance.
        * <code>cache_size</code>: <em>(int)</em> number of examples to keep in memory from the sampling process. The larger the better to ensure diversity of examples for creating training batches. This needs to be set according to hardware capabilities, number of channels, box size, etc.
        * <code>workers</code>: <em>(int)</em> number of parallel loading processes that read images, crop single cells and put them in the queue for training.
    * <code>validation</code>: parameters for experimental evaluation.
        * <code>frequency</code>: <em>(int)</em> number of epochs to run before running one validation evaluation.
        * <code>top_k</code>: <em>(int)</em> reports an accuracy metric where the correct answer is in the top K choices.
        * <code>batch_size</code>: <em>(int)</em> batch size for the validation set.
        * <code>frame</code>: <em>(string)</em> partition of the data used for validation. Valid values include “all”, “train” or “val”. Recommended default value: “val”.
        * <code>sample_first_crops</code>: <em>(bool)</em> true or false, whether to use all crops from each validation image or only sample the first N for validation, where N is the batch size.
4. <code>profile</code>: configuration to run an existing model on images with the purpose of extracting features or obtaining classification outputs.
    * <code>use_pretrained_input_size</code>: <em>(int)</em> input size for the neural network models pre-trained on the ImageNet dataset. The pretrained InceptionResNetv2 model uses <code>299</code> while pretrained ResNet and EfficientNet models use <code>224</code>. This parameter is not needed for models trained by you, only for these three supported pretrained models.
    * <code>feature_layer</code>: <em>(string)</em> name of the layer in the convolutional network to be used for feature extraction.
    * <code>checkpoint</code>: <em>(string)</em> name of the weights file stored in the <code>outputs/results/checkpoint/</code> directory after the network is trained.
    * <code>batch_size</code>: <em>(int)</em> number of samples used during the forward pass for feature extraction.


## <strong>3.1 Logging</strong>


### **3.1.1 Comet.ml logging**

This is an optional feature and is not enabled by default. _Comet.ml_ is a service that hosts the results of your machine learning experiments to make easy comparisons of configuration outcomes. The basic service is free and makes the results open to the rest of the world, pretty much like _GitHub_ makes open source code available to everybody. In this case, comet.ml is great if you are doing open science. We, the developers of DeepProfiler, will make our experiments open for others to reproduce and understand what to expect when they run their own private science experiments. We also plan on releasing the models that we train, which will be documented here soon.

If you want to enable _comet.ml_ for your experiments, you need to create an account in the [comet.ml website](https://www.comet.ml/), and obtain an API key. Then, you have to create a file that contains that key in the `inputs/config/` directory, with the following JSON format:


```
{
    "log_type":"comet_ml",
    "api_key": "your-api-key",
    "project_name": "your-project-name"
}
```


You can then use this in a training experiment by adding the flag `--logging=mykeyfile.key`. Only when you add this key, your experiments will start logging.

**Juan stopped here.**


# 4. Train a model and profile cells

After configuring the project, running DeepProfiler is straightforward. There are two main commands that can be run for training and then extracting features with a trained network.


## **4.1 Train a model:**

If using a pretrained model, skip this step and move to 4.2 directly.

```
python3 deepprofiler --root=/home/ubuntu/project/ --config filename.json train
```


## **4.2 Infer profiles from a model:**


```
python3 deepprofiler --root=/home/ubuntu/project/ --config filename.json --exp experiment_name profile
```

```{admonition} Note
:class: tip
The `--config filename.json` parameter points to the name of a file from /inputs/config folder.
```


### Profiling from a self-trained model:

After training your own model, you can profile your data using the checkpoints from the training:

The _profile_ section of your config should look something like this:


```
"profile": {
      "feature_layer": "pool5",
      "checkpoint": "checkpoint_0020.hdf5",
      "batch_size": 128
    }
```


When profiling from a model pre-trained on ImageNet images, the ‘checkpoint’ simply is replaced with “None”.





## **Optional project-dependent functions:**

````{dropdown} **Prepare a dataset:**

This tool computes illumination statistics, illumination correction functions and compresses images into PNG format. This is useful when the image collection used for training is too large and cannot be kept in a single server (think TBs of imaging data in a data center). Compressing a large collection of images can make training feasible for a diversity of cellular phenotypes. We designed this functionality to compress images as much as possible while losing the minimum amount of information.


```
python3 deepprofiler --root=/home/ubuntu/project/ --config filename.json prepare
python3 deepprofiler --root=/project_folder/example_data --config=config.json prepare
```


````

````{dropdown} **Split index file**:

Create multiple files with parts of the index for parallelization purposes. Parallelization is not automatic, it requires manually launching different DeepProfiler instances using different index files. This function just loads the index and creates separate files without repeating information, so a different machine can be assigned to profile different parts of the dataset.

```
python3 deepprofiler --root=/home/ubuntu/project/ --config filename.json split
```


````



# 5. Aggregating profiles

DeepProfiler single-cell profiles can be aggregated via a [Pycytominer](https://github.com/cytomining/pycytominer) function called [DeepProfiler_Processing](https://github.com/cytomining/pycytominer/blob/master/pycytominer/cyto_utils/DeepProfiler_processing.py). This function reads the output features of DeepProfiler, including the metadata, aggregates, and saves the data in a Pycytominer and Cytominer-eval readable data frame format.

This code gives an example on how to run the aggregation function:

Make sure to install this version of pycytominer:


```
pip install git+git://github.com/cytomining/pycytominer@update_agg_TF2

import os
import numpy as np
import pandas as pd

from pycytominer.cyto_utils.DeepProfiler_processing import AggregateDeepProfiler

project_dir = os.path.join(
    os.path.dirname(__file__)
)

experiment = 'folder_name'

profile_dir = os.path.join(project_dir, "outputs", experiment, "features")

index_file = os.path.join(project_dir, "inputs", "metadata", "index.csv")

output_folder = os.path.join(project_dir, 'outputs',experiment,'aggregated')

well_class = AggregateDeepProfiler(
    index_file=index_file,
    profile_dir=profile_dir,
    aggregate_operation="median",
    aggregate_on="well",
    output_file=output_folder,
)
df_well = well_class.aggregate_deep()

df_well.to_csv('aggregated_efficientnet_median.csv')
```



# 6. Processing DeepProfiler features

After aggregating, profiles are typically processed before being used for analysis purposes. Downstream processing can be done with the different operations of [Pycytominer](https://github.com/cytomining/pycytominer). Typically well-level data is spherized and then aggregated to compound level (no normalization and feature selection).

The [Cytominer-eval](https://github.com/cytomining/cytominer-eval) repository contains six functions that calculate different quality metrics for perturbation profiling experiments: Precision@K and Recall@K, Enrichment, Hit@k, Replicate reproducibility, MP-value, and Grit.


# 7. Run example data

The following instructions help first-time users to download some example data and run important DeepProfiler commands.



1. `cd /home/ubuntu`
2. `wget https://imaging-platform.s3.amazonaws.com/projects/deepprofiler-examples/example-data.tar.gz`
3. `tar -xzf example-data.tar.gz`
4. Your folder `example-data` is now your project directory for this example project. In other words, when running commands in the DP folder, you refer to this as root.
5. `cd /home/ubuntu/DeepProfiler `
6. If you are running DP on a docker, mount docker via ``docker run -it --rm -v ~/home/ubuntu/example_data:/example_data michaelbornholdt/deep_profiler:0.3.0``
7. Check that the mount worked: ``ls /example_data/` should give inputs and outputs`
8. Prepare images via: ``python3 deepprofiler --root=/example_data/ --config=config.json prepare``
9. in ``/jamboree/example_data/inputs/config/config.json`` change the `profile: checkpoint` to ``"None"``
10. ``python3 deepprofiler --root=/example_data/ --config=config.json profile``
11. Aggregate data via
    1. `cd /example_data/`
    2. `Python3 run_aggregation.py`
12. Plot correlation matrix?
