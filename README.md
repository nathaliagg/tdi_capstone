# TDI Capstone Project

## Content

- 1 - [AgricultureVision](#1---agriculturevision)  
        1.a. [Why AgricultureVision?](#why-agriculturevision)  
- 2 - [Conda Environment](#2---conda-environment)
- 3 - [Download](#3---download)
- 4 - [Exploratory Data Preparation](#4---exploratory-data-preparation)
- 5 - [Exploratory CNN model development](#5---exploratory-cnn-model-development)
- 6 - [Preliminary Project App](#6---preliminary-project-app)
- 7 - [Next steps](#7---next-steps)
- [References](#references)

---
## 1 - AgricultureVision

The AgricultureVision dataset [1] is joint effort with many research scientists to bring artificial intelligence and agriculture together.

The complete dataset contains more than 94,000 high-resolution images from over three thousand farmlands in the US. These images were collected between 2017 and 2019. Each image was annotated by experienced agronomists, and contains four channels: *RGB and NIR*. The annotations fall in several categories including *double plant, planter skip, cloud shadow, standing water, waterway and weed cluster*. These annotated patterns or anomalies had a substancial impact in field conditions and subsequently crop yield [1].

For my TDI Capstone Project, I am using a subset of these data (~ 4.4 Gb) representing the images collected in 2019. There is also more information on this group's [GitHub page](https://github.com/SHI-Labs/Agriculture-Vision).

The subset dataset contains over 21,000 farmland images from 2019, and six annotations: *cloud shadow, double plant, planter skip, standing water, waterway and weed cluster*. These six patterns are stored separately as binary masks due to potential overlaps between patterns.


### Why AgricultureVision
- I have a BS in Ag. Engineering (2012), and MS in Entomology and Plant Pathology (2015), so my early career training has been very focused on crop production and protection
- My interest in remote sensing started when I took two internships at an ag. precision company (2008 and 2009) that made soil fertilizer recommendations (variable rate method) for farmers in the midwest of Brazil (soybean, corn, cotton producing areas)
- Within field variability (e.g., weed population, storm damage, planter skip) can significantly impact crop yield and are often overlooked
- Deep learning is driving advancements in the agricultural sector, and it can help farmers make better decisions such as targeted chemical and fertilizer applications
- Target stakeholders of this project would be farmers, crop consultants and agricultural deep learning startups. 


---
## 2 - Conda Environment

I had several installation issues with tensorflow. The only way it worked for me was creating a conda environment and installing libraries in the jupyter [notebook](1_install_libraries.ipynb).

```{bash}
$ conda env create -f tdi_env.yml

$  conda activate tdi_env

(tdi_env) $  which jupyter
/Users/grachetng/miniconda3/envs/tdi_env/bin/jupyter

(tdi_env) $  jupyter notebook
```

---
## 3 - Download

I contacted the authors of the paper [1], and they sent me a link to a Google Drive where the data was deposited.


---
## 4 - Exploratory Data Preparation

In my initial exploratory analysis, I decided to use a partial dataset because I don't know how to handle multiple label classes for a single image yet and the NIR channel.

In addition, GoogleColab (GPU) and my computer couldn't handle the entire 2019 data (~4.4 Gb), so I am limiting my exploratory analysis to include only images with single labels from the validation set, which yielded 4,157 total images.

1. To selected only validation masks that have one label, I tested if the [image masks](./2_get_single_image_files.ipynb), which were black & white, were all black (no label) in them using `.getextrema() == (0, 0)`. I added that information in a dictionary data structure that I converted into a `pd.DataFrame()`.

2. Then, I [saved the RGB images](./3_select_single_images.ipynb) into a `partial_dataset` directory for training the model.


| Number of labels | Number of images |  
| ------           | ------           |  
| 1                | 4157             |  
| 2                | 266              |  
| 3                | 7                |  
| 4                | 1                |  


| Label type       | Number of images |    
| ------           | ------           |    
| planter skip     |  16              |
| cloud shadow     |  197             |  
| standing water   |  262             |  
| double plant     |  361             |  
| waterway         |  362             |  
| weed cluster     |  2959            |  


It is possible to see that the dataset is not balanced, which certainly is an issue. In the paper [1], the authors discuss the process of image annotation, which was done by experienced agronomists. But, even with their expertise, some images are hard to annotate. Weed is a common problem worldwide, and it is rather easy to identify. Weed clusters are evident in a fallow field, and often weed plants habe a different color than the actual crop. I think that might be one of the reasons for the unbalance.

---
## 5 - Exploratory CNN model development

From the information I was able to gather (== understand), I believe that I needed a semantic segmentation approach for this project.

My first model was a Convolutional Neural Network (CNN). I divided the dataset into training (n = 2,828) and testing (n = 1,886), and resized the images to (300, 300). I also used all six classes: cloud shadow, double_plant, planter skip, standing water, waterway, and weed cluster, and each label received a number from 0 to 5, respectively.

The CNN model isn't great. It has a 72% accuracy on test data. I used the accuracy score or pixel accuracy, which is not a reliable metric. In the original paper [1], the authors discussed and recommended Intersection over Union (IoU) metric for accuracy.

I need to address the dataset unbalance, and develop this into a multiclass semantic segmentation approach.


---
## 6 - Preliminary Project App

![CNN App](cnn_app.gif)


---
## 7 - Next steps

- Find computing/GPU resources that can handle more data.
- Test the model on more image files.
- Make the dataset classes/labels more balanced
- Incorporate IoU accuracy metric
- Incorporate NIR channel
- Develop a multiclass semantic segmentation
- Study and test other approaches and model architectures (like VGG16)

---
## References

1 - Mang Tik Chiu, Xingqian Xu, Yunchao Wei, Zilong Huang, Alexander Schwing, Robert Brunner,  Hrant Khachatrian, Hovnatan Karapetyan, Ivan Dozier, Greg Rose, David Wilson, Adrian Tudor, Naira Hovakimyan, Thomas S. Huang, and Honghui  Shi. Agriculture-vision: A large aerial image database for agricultural pattern analysis. arXiv preprint arXiv:2001.01306, 2020
