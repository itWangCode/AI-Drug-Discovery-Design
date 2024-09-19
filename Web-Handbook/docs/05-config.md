# 5. Configuration file and examples 

The configuration file is a text file in JSON format that organizes various settings for one experiment. If you need to 
test different configurations, you can create different configuration files and run DeepProfiler with each. DeepProfiler 
searches for the configuration file in the `inputs/config/` directory, which you can use to store various configuration files. 
Note that the `--config` flag does not need you to specify the full path of the file, just the name as it is assumed to be 
stored in the `inputs/config/` directory.

## 5.1 Configuration File Organization
The configuration file is organized into four main sections as follows. We’ve included specific recommendations where possible. 
For more details, check out our [preprint](https://www.biorxiv.org/content/10.1101/2022.08.12.503783v2). For generating this config file for your project, look at the descriptions 
below together with the provided examples of metadata and configuration files.

### 1. `dataset`: description of your image collection with basic general information

  * `metadata`
      * `label_field`: _(string)_ column in the metadata file corresponding to the treatments or biologically relevant labels of images.
      * `control_value`: _(string)_ identifier or name of control samples in the column above (used to gather illumination statistics).
  * `images`
      * `channels`: _(array of strings)_ list of image channels used for profiling. The list contains the names of columns in the metadata file that hold the location of images for each channel. DeepProfiler assumes each channel is stored as a separate image, and also that the path listed in the metadata file is relative to the input/images directory (instead of absolute paths). This facilitates moving the project to another machine in a different location.
      * `file_format`: _(string)_ extension of image files, e.g. tiff, tif, png.
      * `bits`: _(int)_ pixel bit depth. Not necessary for any analysis, only used for compression purposes. 8-bit and 16-bit images are currently supported.
      * `width`: _(int)_ width of the input image in pixels
      * `height`: _(int)_ height of the input image in pixels
  * `locations`: parameterize how DeepProfiler will search for single cells in images for training and profiling.
      * `mode`: _(string)_ this field indicates if images will be processed at single-cell resolution or in full image mode. It only accepts two strings: `single_cells` - activates single-cell analysis mode, thus, requiring cell locations to be stored in the `inputs/locations/` folder (Section XXX); `full_image` - activates full image analysis (no need for locations files).
      * `box_size`: _(int)_ specifies the size in pixels of the bounding box used to crop single cells out of images. The value is used for both the width and the height of the box (a square box). This value is used even in `full_image` mode, in which case the image will be resized to these dimensions. Note that DeepProfiler enforces a fixed input size because that is what neural network models usually expect. The box size should be selected to fully cover a typical cell in the experiment. It is OK if large cells are cut a bit, as long as this is relatively rare compared to the normal cell size. Also, it is OK if cells appear with neighboring cells in the same box, which we call “single cells in context” or can be fixed by masking (see below).
      * `view_size`: _(int)_ useful only in `full_image` mode, specifies the size in pixels of the region of the image to be covered by cropping before resizing to the dimensions configured in `box_size`.
      * `mask_objects`: _(bool)_ true or false, indicates whether cells should be masked using the cell outlines in `input/outlines`. Optional, the recommended value at the moment is false (see more information below).

### 2. `prepare`: configuration for illumination correction and compression

The command `prepare` then runs illumination correction and compression, useful for preparing training datasets that can be read efficiently repeated times from disk. This is optional if you only need to do feature extraction and profiling with a pre-trained model.

  * `illumination_correction`: parameters to run a prospective illumination correction algorithm that estimates the illumination correction functions for each channel in each plate.
      * `down_scale_factor`: _(float)_ the illumination correction functions are not computed at full resolution. This parameter tells DeepProfiler how small these functions should be. A common parameter is 4, for images of about 1024x1024 pixels, resulting in illumination correction functions of 256x256 pixels.
      * `median_filter_size`: _(int)_ size in pixels of the smoothing operator applied before aggregation of the illumination correction function. Usually set to 24 for images of 1024x1024 pixels.
  * `compression`:
      * `implement`: _(bool)_ true or false, whether compression is used for training and profiling. If true, other DeepProfiler commands will use the compressed images in the `output/compressed/` directory instead of the original images in the `input/images/` directory.
      * `scaling_factor`: _(float)_ make images a fraction of what they are. 1.0 means no scaling, 0.8 means resizing to 80% of the current size in `x` and `y`. Re-scaling images results in smaller files that are faster to read during training, but loses spatial resolution, which is generally not recommended. Use a value different to 1.0 only if there is a good experimental reason.

### 3. <code>profile</code>: parameters to run an existing model on images to extract features or obtain classification outputs.

  * <code>use_pretrained_input_size</code>: <em>(int)</em> input size for the neural network models pre-trained on the ImageNet dataset. The pre-trained InceptionResNetv2 model uses <code>299</code> while pre-trained ResNet and EfficientNet models use <code>224</code>. This parameter is not needed for models trained by you, only for these three supported pre-trained models.
  * <code>feature_layer</code>: <em>(string)</em> name of the layer in the convolutional network to be used for feature extraction.
  * <code>checkpoint</code>: <em>(string)</em> name of the weights file stored in the <code>outputs/&lt;experiment&gt;/checkpoint/</code> directory after the network is trained.
  * <code>batch_size</code>: <em>(int)</em> number of samples used during the forward pass for feature extraction.


### 4. `train`: parameters for training a deep learning model on your data.

  * `partition`:
      * `targets`: _(array)_ column names in the metadata file that want to be used as classification targets for training the neural networks. It currently uses only the first element in the list, e.g., `['Compound', 'Concentration']`, means that there are two columns in the metadata file with that information and that DeepProfiler will use `'Compound'` for training. The rest of the array is currently ignored but is intended to be used in the future. If both columns are necessary for training, consider merging them in a single column, otherwise, you can leave only one column name in the array i.e., `['Compound']`
      * `split_field`: _(string)_ column name in the metadata file that indicates which images should be used for training and which ones for validation (or just ignored). This column may be one of the columns containing information about the experiment (e.g. plate id) or a custom-defined column with these decisions made by the analysis.
      * `training`: _(array)_ unique values in the `split_field` column of the metadata file that indicate which images will be used for training. For example, if `split_field=Metadata_Plate`, this array should indicate which plates are intended to used for training e.g. `["plateA", "plateB", "plateC"]`.
      * `validation`: _(array)_ unique values in the `split_field` column of the metadata file that indicate which images will be used for validation. This is the same as the `training` field above.
  * `model`: deep learning model parameters
      * `name`: _(string)_ deep learning model to be used, the name should be one of the models in the plugins folder. The default recommended model is `efficientnet` for weakly supervised learning. We also support `resnet` models.
      * `crop_generator`: _(string)_ strategy for cropping single cells from images. Crop generators are implemented in the plugins folder and can be extended with custom code if necessary. DeepProfiler currently has the following options implemented: 1) `sampled_crop_generator`, this crop generator reads single-cell images pre-cropped and exported for training (see Section XXX). This is the recommended way for training new models.  2) `online_labels_cropgen`, used for training with online label smoothing using exported single-cell datasets as before. If analyzing the dataset in full_image mode, you should use the default value. 3) `repeat_channel_crop_generator`, used for extracting features using networks pre-trained with the ImageNet dataset (RGB natural images). This crop generator transforms each gray-scale channel of your images into an RGB image to enable processing and then concatenates the features of all channels in a single vector. This crop generator is only useful for profiling and should not be used for training. It can be used in `full_image` analysis mode. 4)  `full_image_crop_generator`, used for training new models and profiling in full image mode. 
      * <code>augmentations</code>: <em>(boolean)</em> </code>switch augmentation layer on and off. DeepProfiler uses data augmentation to generate models robust to certain transformations and noise. The transformations implemented in the augmentation layer are applied at random to images of single cells during training only and include 90-degree rotations, horizontal flips, brightness and contrast illumination perturbations on each channel separately.
      * <code>metrics</code>: <em>(array of strings)</em> contains names of metrics to monitor performance during training. It supports most of the [keras metrics](https://keras.io/api/metrics/), including <code>accuracy</code>. This applies for now only for the <code>train</code> command.
      * <code>epochs</code>: <em>(int)</em> number of epochs for training.
      * <code>initialization</code>: <em>(string)</em> strategy to set the initial model weights for training. Valid values are <code>Random</code> (supported by all models) or <code>ImageNet</code> (currently supported by ResNet and EfficientNet models only). Using ImageNet weights is a better initialization strategy in practice, and usually leads to improved performance.
      * <code>checkpoint_policy</code>: <em>(string)</em> or <em>(int)</em> checkpointing policy parameter (optional). Checkpoints are files that save the state of the model during training because training sessions are usually long and may fail (or be interrupted by the system). Checkpoints help to recover the training session, or simply reuse the model after training. If the parameter is an integer number, then DeepProfiler saves model checkpoints every <code>checkpoint_policy</code> step. If the string <code>best</code> is used, then DeepProfiler saves only the best-performed checkpoint according to validation performance. By default, checkpoints are saved for every epoch.
      * <code>params</code>: model-specific values that depend on the plugin or architecture.
          * <code>learning_rate</code>: <em>(float)</em> initial learning rate for the optimizer.
          * <code>batch_size</code>: <em>(int)</em> number of samples per batch during training.
          * <code>conv_blocks</code>: <em>(int)</em> number of layers, or convolutional blocks. For ResNet valid values only include <code>50</code>, <code>101</code> and <code>152</code>.
          * <code>label_smoothing</code>:<code> </code>(<em>float</em>) label smoothing parameter for categorical cross-entropy loss.
          * <code>online_label_smoothing:</code>(<em>float</em>) label smoothing if online labeling is used.
          * <code>online_lambda:</code> (<em>float</em>) online labeling regularization parameter.
      * <code>lr_schedule</code>: <em>(array or string)</em> strategy for decreasing the learning rate during training. There are three strategies supported:
          * 1) constant rate, which doesn’t require this parameter to be set (i.e. just remove this parameter from the config file).
          * 2) step schedule: changes the learning rate to a desired value at specific epochs. This strategy needs you to configure two arrays, ”epoch” for the epochs where the learning rate will be changed (integer numbers), and “lr” with the actual desired learning rate values (e.g. <code>{"epoch":[40, 80], "lr":[0.1, 0.01]}</code>). Both arrays are expected to be the same size.
          * 3) cosine decay, which increments the learning rate from zero to the initial learning rate using a linear function during the first five epochs. After that, every epoch reduces the learning rate according to the cosine decay. Use <code>"cosine"</code> to enable this option.
  * <code>sampling</code>: parameters to load images and crop single cells during training. Those parameters are only used for the default <code>crop_generator</code> (<code>"crop_generator")</code>, which is used for exporting single cells, among others.
      * <code>factor</code>: <em>(float)</em> fraction of crops from each image to be used for training (number between 0 and 1). This parameter can be used to prevent filling up the queue with example cells from a few images only. With a small sampling factor, the queue will have more diversity of cells cropped from a variety of images to create batches, improving the training performance. In this case, more epochs will be needed to reach optimal performance.
      * <code>cache_size</code>: <em>(int)</em> number of examples to keep in memory from the sampling process. The larger the better to ensure diversity of examples for creating training batches. This needs to be set according to hardware capabilities, the number of channels, box size, etc.
      * <code>workers</code>: <em>(int)</em> number of parallel loading processes that read images, crop single cells and put them in the queue for training.
  * <code>validation</code>: parameters for experimental evaluation.
      * <code>frequency</code>: <em>(int)</em> number of epochs to run before running one validation evaluation.
      * <code>top_k</code>: <em>(int)</em> reports an accuracy metric where the correct answer is in the top K choices.
      * <code>batch_size</code>: <em>(int)</em> batch size for the validation set.
      * <code>frame</code>: <em>(string)</em> partition of the data used for validation. Valid values include “all”, “train” or “val”. Recommended default value: “val”.
      * <code>sample_first_crops</code>: <em>(bool)</em> true or false, whether to use all crops from each validation image or only sample the first N for validation, where N is the batch size.

## 5.2 Available examples of configuration files
The examples of configuration files can be found in the [example data](https://cytomining.github.io/DeepProfiler-handbook/docs/02-structure.html#add-project-data),
[availible in DeepProfiler repository](https://github.com/cytomining/DeepProfiler/blob/master/example_data.tar.gz)
under `/inputs/config/` folder. It contains two examples:
1. `training_profiling.json`: a configuration file for [training](https://cytomining.github.io/DeepProfiler-handbook/docs/07-train.html)
with the example data and then [profiling](https://cytomining.github.io/DeepProfiler-handbook/docs/06-profiling.html#profiling-with-self-trained-model).
2. `export.json`: a configuration file for [single-cell export](https://cytomining.github.io/DeepProfiler-handbook/docs/07-train.html#export-single-cells).

[DeepProfilerExperiments Github repository](https://github.com/broadinstitute/DeepProfilerExperiments) contains 
experiment configuration files for the benchmark datasets (in the repository you can find a corresponding folder for 
each of those: `ta-orf` (BBBC037 dataset), `bbbc022` and `cdrp` (BBBC036 dataset)) the example configuration files 
can be found in the `config` folder. There are the following examples: 

1. `cell_painting_cnn.json`: a configuration file for [profiling with the *Cell Painting CNN* model](https://cytomining.github.io/DeepProfiler-handbook/docs/06-profiling.html#profiling-with-cell-painting-cnn-model).
2. `efficientnet_train_and_profile.json`: a configuration file for [training](https://cytomining.github.io/DeepProfiler-handbook/docs/07-train.html) and then [profiling](https://cytomining.github.io/DeepProfiler-handbook/docs/06-profiling.html#profiling-with-self-trained-model) with the trained model.
    It does not differ much from the previous one, only the name of the checkpoint file is different.
3. `export.json`: a configuration file for [single-cell export](https://cytomining.github.io/DeepProfiler-handbook/docs/07-train.html#export-single-cells).
4. `pretrained_effnet.json`: a configuration file for [profiling with ImageNet pre-trained](https://cytomining.github.io/DeepProfiler-handbook/docs/06-profiling.html#profiling-with-imagenet-pre-trained-model) EfficientNet. 

