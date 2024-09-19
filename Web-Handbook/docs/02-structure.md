# 2. Project structure

After installing DeepProfiler on your machine, the next step is to create a project directory structure that holds your 
data with the required inputs and space for generated outputs.


## **2.1 Initialize your project**

In the following sections, we assume that you have an Ubuntu environment and a user account named “ubuntu”. Make sure to
replace the example path (`/home/ubuntu`) with the directories that you are using in practice. Go to your base path and 
create an empty directory for your project (called `project`):


```
cd /home/ubuntu
mkdir project
```


Go back to the DeepProfiler to initialize the contents of your new project directory:


```
cd /path/to/DeepProfiler
python3 deepprofiler --root=/home/ubuntu/project setup
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
```
.
└── project/
    ├── inputs/
    │   ├── config
    │   ├── images
    │   ├── locations
    │   ├── outlines
    │   └── metadata
    └── outputs/
        ├── compressed/
        │   ├── images
        │   └── metadata
        ├── intensities
        └── results/
            ├── checkpoint
            ├── features
            ├── logs
            └── summaries
 ```

```{admonition} Note
:class: tip
You can create this directory structure manually if you want, but make sure you follow these conventions because DeepProfiler expects these directories to exist and does not explicitly validate if that is the case.
```



## **2.2 Add project data**

The directories created in the previous step are empty, so your next task is to put your project data in the right place.
A small example dataset can be obtained from our web servers, so you can test and debug DeepProfiler issues easily. 
Example data is provided in the DeepProfiler repository, you only need to unpack the archive which is available in the 
main directory of DeepProfiler:

```
cd /path/to/DeepProfiler/
tar -xzf example_data.tar.gz
```

The example dataset contains a few images from the Cell Painting [BBBC037 dataset](https://bbbc.broadinstitute.org/BBBC037),
together with the necessary files to configure the DeepProfiler project. Copy the essential data to the corresponding 
project directory. Note that the images in this example data are already processed and compressed, this means that the 
images are not stored in `project/inputs/images`, but in `project/outputs/compressed/images`. The example data already 
follows the DeepProfiler project structure. The example dataset also includes segmentation masks (outlines).

```
cp -r example-data/* /home/ubuntu/project/*
```

More information about some of these files can be found in the following sections.
