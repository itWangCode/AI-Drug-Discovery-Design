# 9. Run profiling in AWS (EC2 instance)
## **9.1 Requirements**

1. Make sure your images and database (.sqlite) files from CellProfiler analysis are located within the S3 bucket (this is important because we will need to copy all your files to an EC2 instance before running profiling);
2. This protocol is built to use with data that was analyzed previously using CellProfiler, where a nuclei object was identified. In the scripts used in this protocol, we assume that you have a .sqlite file that has information about the location of the cells (‘Nuclei_Location_Center_X’ and ‘Nuclei_Location_Center_Y’), as well as FileName, Metadata_Plate, Metadata_Well, Metadata_Site columns. 


## **9.2 Create an instance**

1. Follow the next steps to create an instance using an AMI that's located at broad-imaging-cimini account. If you need to create your own AMI, follow the steps at the end **Appendix: Creating an AMI for DeepProfiler**.

  * `partition`:
    * EC2 => Instances => Launch Instance
    * Name and Tags:
        * Name: YOURNAME_DeepProfiler
    * Add additional tags:
        * Key: User, Value: YOURBROADUSERNAME (e.g. fossa)
        * Make sure both sets of tags are applied to both the instance and the volume(s)
    * Application and OS Images:
        * MyAMIs:
            * `DeepProfiler_p2xlarge_cuda_tensorflow253 ami-08e9d2839d316fb51(broad-imaging-cimini)` 
        * Instance type:
            * **p2.xlarge** 
    * Key pair (login):
        *  select your key pair
    * Network settings: (for broad-imaging-cimini)
        * VPC: default
        * Subnet: any
        * Firewall (security groups): select existing security group: ssh
        * Auto-assign Public IP: Enable
    * Configure storage:
         * **40 GiB**
    * Advanced details:
        * IAM instance profile:
        * ecsInstanceRole (for broad-imaging-cimini)

2. Create an alarm using AWS instructions for [creating a stop actions to Amazon CloudWatch alarms](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UsingAlarmActions.html) to stop your instance that's no longer in use.

3. Follow the AWS instructions for [creating](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-creating-volume.html#console) and [attaching](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-attaching-volume.html#console) an external EBS volume that will be used just for this batch. 

```{admonition} Critical to create a volume
:class: important
The volume must be created in the same subnet as your backend creation machine (`us-east-1a`), and should be 2X the size as the analysis files in your batch.
Determine your analysis size by navigating to the analysis folder on S3 web console and selecting **Actions** => **Calculate total size**. 
(Note: The HD actually needs to be 2X the size of analysis files that will be running in parallel - most of the time this is your whole batch but if youâ€™re working on a very large dataset, it will be smaller).
```

```{note}
If your dataset is large, consider using [Distributed-DeepProfiler](https://github.com/DistributedScience/Distributed-DeepProfiler) instead of this protocol. 
```

## **9.3 Prepare for profiling**

This section was based on **Cell-Painting-Documentation-Internal**.

1. **Connect to your DeepProfiler EC2 computer** 
	* **AWS** => **Services** => **EC2** => **Instances** => **YOURFIRSTNAME_DeepProfiler**     
	* **Instance State** => **Start** *or* right-click => **Start Instance**

    ```{tip}
    If you see no running instances, check the upper right corner. 
    It should have your location as us-east-1 N. Virginia.
    ```
    * Log into your EC2 machine.

	```
	ssh -i ~/.ssh/$YOUR_KEY_NAME.pem ubuntu@LOGIN_ADDRESS
	```

	* With your computer selected, LOGIN_ADDRESS can be found in the Description tab as Public DNS (Ipv4). 
	* You will get an authenticity warning the first time you log in. Say `yes`. 


    * Create or attach a tmux.  
    To create new tmux:` tmux new -s NEWNAME`  
    To see existing tmux sessions: `tmux list-sessions`  
    To attach an old tmux: `tmux a -t EXISTINGNAME`   
    ```{note}
    a=attach t=target s=session.  
    Name your tmux simply based on the project title or step e.g. `cmqtl` or `backends`.
    ```

2. **Install AWS CLI**  
    If you have not previously used AWS CLI on your machine, you may need to install AWS CLI by following [these instructions](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

3. **Create a temp directory**  

    ```
    mkdir ~/ebs_tmp
    ```

4. **Mount your volume to your EC2 machine**  
    You will need to mount your external EBS volume every time that you turn your EC2 instance on/off, though you will only need to create the file system once.

    Run `lsblk` to find the name of the volume. 
    It will return something like:
        
    ```
    NAME    	MAJ:MIN 	RM   	SIZE 	RO 	TYPE MOUNTPOINT
    xvda    		202:0    	0     	8G  	0 	disk
    --xvda1 	202:1    	0    	 8G  	0 	part /
    xvdb    		202:80   	0   	100G  	0 	disk 
    ```

    To see if you have a file system on your harddrive:
    ```
    sudo file -s /dev/VOLUMENAME
    ```

    * If you get `/dev/VOLUMENAME: data`   in response, create the file system, mount it, and change file permissions:
        ```
        sudo mkfs -t ext4 /dev/VOLUMENAME
        ```
    * If you get `/dev/VOLUMENAME: Linux rev 1.0 ext4 filesystem` in response, you are good to go.

    Run
    ```
    sudo mount /dev/VOLUMENAME /home/ubuntu/ebs_tmp
    sudo chmod 777 ~/ebs_tmp/
    ```

    Run `lsblk` again and check that the volume now has a mountpoint.
    It will return something like this:

    ```    
        NAME    	MAJ:MIN 	RM   	SIZE 	RO 	TYPE MOUNTPOINT
        xvda    		202:0    	0     	8G  	0 	disk
        â””â”€xvda1 	202:1    	0     	8G  	0 	part /
        xvdb    		202:16   	0   	110G  	0 	disk /home/ubuntu/ebs_tmp
    ```

5. **Define environment variables**  

    ```
    PROJECT_NAME=<Project_Name in AWS>
    BATCH_ID=<Batch_folder inside Project_Name>
    BUCKET=imaging-platform-ssf (name of your S3 bucket)
    EXPERIMENT_NAME=<Name this DeepProfiler experiment>
    ```

    ```{Tip}
    To check the content of a variable: `echo $PROJECT_NAME`
    ```

## **9.4 Install DeepProfiler**

1. Create folders inside ~/ebs_tmp:

    ```
    mkdir -p ~/ebs_tmp/work/projects/${PROJECT_NAME}/workspace/{deepprofiler,software,backend}
    ```


2. Run the next commands to clone the DeepProfiler repository, checkout to an specific commit and install it:

    ```
    cd ~/ebs_tmp/work/projects/${PROJECT_NAME}/workspace/software
    git clone https://github.com/broadinstitute/DeepProfiler.git
    cd DeepProfiler/
    git checkout 779bd4cffe5dd8a39cf981f616af6f95f73b7088
    pip install .
    ```

3. Test if DeepProfiler is working. See [1.4 Run DeepProfiler to check it works](01-install.md).

    ```
    python deepprofiler 
    ```

## **9.5 Create necessary files**

1. Create folders using DeepProfiler setup:
    ```
    mkdir -p ~/ebs_tmp/work/projects/${PROJECT_NAME}/workspace/deepprofiler/${BATCH_ID}
    python3 deepprofiler --root=/home/ubuntu/ebs_tmp/work/projects/${PROJECT_NAME}/workspace/deepprofiler/${BATCH_ID} setup
    ```

2. Create configuration file:

  * `partition`:
    * Execute the next command to create the profiling.json file:
        ```
        cd ~/ebs_tmp/work/projects/${PROJECT_NAME}/workspace/deepprofiler/${BATCH_ID}/inputs/config
        nano profiling.json
        ```
    * With the profiling.json open, paste the example configuration file:
        ```
        {
            "dataset": {
                "metadata": {
                    "label_field": "Metadata_Plate",
                    "control_value": "X"
                },
                "images": {
                    "channels": [
                        "DNA",
                        "RNA",
                        "ER",
                        "AGP",
                        "Mito"
                    ],
                    "file_format": "tif",
                    "bits": 16,
                    "width": 1224,
                    "height": 904
                },
            "locations":{
                "mode": "single_cells",
                "area_coverage": 0.75,
                "box_size": 128,
                "mask_objects": false
            }
            },
            "prepare": {
                "illumination_correction": {
                    "down_scale_factor": 4,
                    "median_filter_size": 24
                },
                "compression": {
                    "implement": false,
                    "scaling_factor": 1.0
                }
            },
            "train": {
                "partition": {
                    "targets": [
                        "Metadata_Plate"
                    ],
                    "split_field": "Split",
                    "training": [0],
                    "validation": [1]
                },
                "model": {
                    "name": "efficientnet",
                    "crop_generator": "sampled_crop_generator",
                    "augmentations": true,
                    "metrics": ["accuracy", "top_k", "average_class_precision"],
                    "epochs": 3,
                    "initialization":"ImageNet",
                    "params": {
                        "label_smoothing":0.0,
                        "learning_rate": 0.005,
                        "batch_size": 32,
                        "conv_blocks": 0
                    }
                },
                "sampling": {
                "factor": 1,
                    "workers": 1
                },
                "validation": {
                "frequency": 1,
                    "top_k": 5,
                    "batch_size": 32,
                    "frame": "val",
                    "sample_first_crops": true
                }
            },
            "profile": {
            "feature_layer": "block6a_activation",
            "checkpoint": "Cell_Painting_CNN_v1.hdf5",
            "batch_size": 32
            }
        }
        ```
    * The “prepare” and “train” arguments must stay so the software runs; you don’t have to change anything there, just copy. 
    * These are the parameters you should change depending on your dataset:
        * `images`: file_format, bits, width, and height of the images;
        * `profile`: change the checkpoint if you use another model than `Cell_Painting_CNN_v1.hdf5`. 
    * For more details check [5. Configuration file and examples](05-config.md).

3. Download the CNN Cell Painting model to your EC2 instance:
    ```
    cd ~/ebs_tmp/work/projects/${PROJECT_NAME}/workspace/deepprofiler/${BATCH_ID}/outputs/${EXPERIMENT_NAME}/checkpoint
    wget https://zenodo.org/record/7114558/files/Cell_Painting_CNN_v1.hdf5
    ```

4. Download the backend/database (.sqlite) files from S3 bucket.
    This command will download all the plates inside your `BATCH_ID` folder.
    ```
    aws s3 sync s3://${BUCKET}/projects/${PROJECT_NAME}/workspace/backend/${BATCH_ID} ~/ebs_tmp/work/projects/${PROJECT_NAME}/workspace/backend/${BATCH_ID} --exclude="*" --include="*.sqlite"
    ```

5. Get list of plates and define plate variable 

    ```
    mkdir -p ~/ebs_tmp/work/projects/${PROJECT_NAME}/workspace/scratch/${BATCH_ID}/
    PLATES=$(readlink -f ~/ebs_tmp/work/projects/${PROJECT_NAME}/workspace/scratch/${BATCH_ID}/plates_to_process.txt)
    aws s3 ls s3://${BUCKET}/projects/${PROJECT_NAME}/workspace/analysis/${BATCH_ID}/ |cut -d " " -f29 | cut -d "/" -f1 >> ${PLATES}
    ```

    Check the contents of PLATES and confirm that the plate names have parsed correctly and there are the correct number.
    
    ```
    nano $PLATES
    ``` 

6. Create the locations file
  * `partition`:
    * Paste the following to create a .py file that, when we run, will get the locations of the single cells, as well as the FileName and Metadata info and create an index file.
        ```
        cd ~/ebs_tmp/work/projects/${PROJECT_NAME}/workspace/deepprofiler/${BATCH_ID}/inputs/locations
        nano extract_locations.py
        ```
    * Paste the following into the extract_locations.py new blank file. Change the name of the “FileName_” columns if your columns are named otherwise. Then `Control-o. Enter. Control-x.`:
        ```
        '''
        Script to extract locations and index from CellProfiler
        '''
        import sqlite3
        import argparse
        import csv
        from collections import defaultdict
        import os.path
        from os import makedirs

        parser = argparse.ArgumentParser(
            description='Extract Metadata and Filenames from SQLite database generated by CellProfiler, to latter usage in DeepProfiler.')
        parser.add_argument('dbpath', help='main path to sqlite files')
        parser.add_argument(
            'locdir', help='destination folder to write locations files in csv format')
        parser.add_argument(
            'csvdir', help='destination folder to write index file in csv format')
        parser.add_argument(
            'plate', help='plates list in a txt file, use it to run this code for the plates in a loop')

        args = parser.parse_args()

        QUERY = '''
        SELECT
            Metadata_Plate,
            Metadata_Well,
            Metadata_Site,
            FileName_OrigER AS ER,
            FileName_OrigRNA AS RNA,
            FileName_OrigAGP AS AGP,
            FileName_OrigMito AS Mito,
            FileName_OrigDNA as DNA,
            CAST(Nuclei_Location_Center_X AS INTEGER),
            CAST(Nuclei_Location_Center_Y AS INTEGER)
        FROM
            Nuclei
        JOIN Image ON
            Image.TableNumber = Nuclei.TableNumber
        '''

        mainpath = args.dbpath
        plate = args.plate
        dbfile = os.path.join(f"{mainpath}",f"{plate}",f"{plate}.sqlite")

        locations = defaultdict(list) #extract and save to a dict
        index = defaultdict(list)
        csv_index = f'{plate}_index.csv'
        with sqlite3.connect(dbfile) as conn:
            cur = conn.cursor()
            for row in cur.execute(QUERY):
                plate_id, well_id, site_id, er, rna, agp, mito, dna, xpos, ypos = row
                csvfile = f'{well_id}-{site_id}-Nuclei.csv'
                locations[csvfile].append((xpos, ypos))
                index[csv_index].append((plate_id, well_id, site_id, f'{plate_id}/{er}', f'{plate_id}/{rna}', f'{plate_id}/{agp}', f'{plate_id}/{mito}', f'{plate_id}/{dna}'))

        makedirs(os.path.join(args.locdir, plate), exist_ok=True) 
        header = 'Nuclei_Location_Center_X', 'Nuclei_Location_Center_Y'
        for csvfile, values in locations.items():
            csvpath = os.path.join(args.locdir, plate, csvfile)
            with open(csvpath, 'w', newline='', encoding='utf-8') as fpointer:
                writer = csv.writer(fpointer)
                writer.writerow(header)
                for row in values:
                    writer.writerow(row)

        csv_indexpath = os.path.join(args.csvdir, csv_index)
        makedirs(args.csvdir, exist_ok=True) 
        header_index = 'Metadata_Plate', 'Metadata_Well', 'Metadata_Site', 'ER', 'RNA', 'AGP', 'Mito', 'DNA'
        for key, values in index.items():
            with open(csv_indexpath, 'w', newline='', encoding='utf-8') as npointer:
                writer = csv.writer(npointer)
                writer.writerow(header_index)
                for row in values:
                    writer.writerow(row)
        ```
    * Run the next command to execute the script. Location and metadata files will be saved inside ~/inputs/locations and ~/inputs/metadata:
        ```
        parallel \
        python extract_locations.py  ~/ebs_tmp/work/projects/${PROJECT_NAME}/workspace/backend/${BATCH_ID} ~/ebs_tmp/work/projects/${PROJECT_NAME}/workspace/deepprofiler/${BATCH_ID}/inputs/locations ~/ebs_tmp/work/projects/${PROJECT_NAME}/workspace/deepprofiler/${BATCH_ID}/inputs/metadata :::: ${PLATES}
        ```

7. Create one index.csv file to process all plates at the same time:
      * `partition`:
        * Run the following to create a join_csv.py file:
            ```
            cd ~/ebs_tmp/work/projects/${PROJECT_NAME}/workspace/deepprofiler/${BATCH_ID}/inputs/metadata
            nano join_csv.py
            ```
        * Paste the content inside the file. Then `Control-o. Enter. Control-x.`:
            ```
            import argparse
            import os
            import csv
            
            parser = argparse.ArgumentParser(
                description='Aggregate csvs to create index metadata file for DeepProfiler.')
            parser.add_argument(
                'indexdir', help='input folder where all index csv files are')
            parser.add_argument(
                'plate', help='plates list in a txt file, use it to run this code for the plates in a loop')

            args = parser.parse_args()

            # Get list of files
            plate = args.plate
            plates = open(plate, 'r')
            data = list(csv.reader(plates, delimiter=","))
            list_files = [f"{value[0]}_index.csv" for value in data]

            # Create the header
            header_index = 'Metadata_Plate', 'Metadata_Well', 'Metadata_Site', 'ER', 'RNA', 'AGP', 'Mito', 'DNA\n'
            f = open('index.csv', 'w')
            f.write(",".join(header_index))   
            # Open the csvs and save them into one final csv
            for filename in list_files:
                file = os.path.join(args.indexdir, filename)
                with open(file) as open_csv:
                    first_row = True
                    for line in open_csv:
                        # Ignore the header row
                        if first_row:
                            first_row = False
                            continue
                        # Add all the rest of the CSV data to the output file
                        f.write(line)

            # Close the output file
            f.close()
            ```
        * Run the next to create one single `index.csv` files for all your plates:
            ```
            python join_csv.py ~/ebs_tmp/work/projects/${PROJECT_NAME}/workspace/deepprofiler/${BATCH_ID}/inputs/metadata ${PLATES}
            ```

8. Copy images to your instance:
    The next script creates the directory with the plate name and download images from AWS to the inputs/images/PLATE folder, based on the list of folder names we provide.
    * `partition`:
        * Run the following to create a load_images.py file:
            ```
            cd ~/ebs_tmp/work/projects/${PROJECT_NAME}/workspace/deepprofiler/${BATCH_ID}/inputs/images
            nano load_images.py
            ```
        * Paste the script. Then `Control-o. Enter. Control-x.`:
            ```
            '''
            Script to provide plate names
            '''
            import sqlite3
            import argparse
            import csv
            from collections import defaultdict
            import os.path
            import subprocess, os
            from os import makedirs

            parser = argparse.ArgumentParser(
                description='Extract Metadata and Filenames from SQLite database generated by CellProfiler, to latter usage in DeepProfiler.')
            parser.add_argument(
                'plate', help='plates list in a txt file, use it to run this code for the plates in a loop')
            parser.add_argument(
                'bucket', help='plates list in a txt file, use it to run this code for the plates in a loop')
            parser.add_argument(
                'project_name', help='plates list in a txt file, use it to run this code for the plates in a loop')
            parser.add_argument(
                'batch_id', help='plates list in a txt file, use it to run this code for the plates in a loop')

            args = parser.parse_args()

            # Get list of files
            plate = args.plate
            plates = open(plate, 'r')
            data = list(csv.reader(plates, delimiter=","))
            list_files = [f"{value[0]}" for value in data]

            for pl in list_files:
                os.system(f'mkdir -p {pl}')
                os.system(f"aws s3 sync s3://{args.bucket}/projects/{args.project_name}/{args.batch_id}/images/{pl}/images ~/ebs_tmp/work/projects/{args.project_name}/workspace/deepprofiler/{args.batch_id}/inputs/images/{pl}")
            ```
        * Run the command to create the folders and download the images. This may take a while:
            ```
            python load_images.py ${PLATES} ${BUCKET} ${PROJECT_NAME} ${BATCH_ID}
            ```
        
## **9.6 Run profiling**

Run the next command to run the profiling with DeepProfiler:

```
cd ~/ebs_tmp/work/projects/${PROJECT_NAME}/workspace/software/DeepProfiler
python3 deepprofiler --root=/home/ubuntu/ebs_tmp/work/projects/${PROJECT_NAME}/workspace/deepprofiler/${BATCH_ID} --config profiling.json --metadata index.csv --exp ${EXPERIMENT_NAME} profile
```

## **9.7 Sync features to S3 bucket**

You can sync the outputs folder to your S3 bucket project folder by running:

```
aws s3 sync ~/ebs_tmp/work/projects/${PROJECT_NAME}/workspace/deepprofiler/${BATCH_ID}/outputs/${EXPERIMENT_NAME}/ s3://${BUCKET}/projects/${PROJECT_NAME}/workspace/deepprofiler/${BATCH_ID}/outputs/${EXPERIMENT_NAME}/results/
```

## **9.8 Delete volume**

Check if all the features were synced to your S3 bucket. Now, [delete the temporary volume](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-deleting-volume.html) associated with your instance. 

# Appendix: Creating an AMI for DeepProfiler

1. To create the instance, use the same configurations as above (**9.2 Create an instance**), but use a Quick Start AMI:
    * Use an Ubuntu AMI (for example, use Quick Start AMIs > Ubuntu > Ubuntu Server 18.04)

2. Connect to the instance:
    ```
    ssh -i ~/.ssh/YOUR_KEY_NAME.pem ubuntu@LOGIN_ADDRESS
    ```

3. Then, to update the Nvidia driver of a p2.xlarge machine, follow the next instructions:
    * `partition`:
        * Run 
            ```
            sudo apt-get update
            ```

            ```
            sudo apt-get upgrade
            ```

        * Reboot the instance by running 
            ```
            sudo reboot
            ```
            * (The putty session will become inactive as the instance reboots. It might take a few minutes before you can connect through a new session)
        * Run 
            ```
            sudo apt-get install xorg
            ```
        
        * Run
            ```
            sudo apt-get install nvidia-driver-460
            ```
        
        * Reboot again: 
            ```
            sudo reboot
            ```
        
        * Run to verify that the GPU is now installed:
            ```
            nvidia-smi 
            ```

4. Proceed with this protocol. Save this AMI to use later. 


