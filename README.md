# TDI Capstone Project

## Content

- 1 - [AgricultureVision](#agvision)
    a. [Why Agriculture-Vision?](#why)
- 2 - [Conda Environment](#conda)
- 3 - [Download](#download)
- 4 - [Exploratory analysis - data preparation](#dataprep)
- 5 - [Exploratory CNN model development](#cnn)
- 6 - [Preliminary Project App](#app)
- [References](#references)

---
#agvision
## 1 - AgricultureVision

The AgricultureVision dataset [1] is joint effort with many research scientists to bring artificial intelligence and agriculture together.

The complete dataset contains more than 94,000 high-resolution images from over three thousand farmlands in the US. These images were collected between 2017 and 2019. Each image was annotated with *double plant, drydown, endrow, nutrient deficiency, planter skip, storm damage, water, waterway and weed cluster*, and contains four channels: *RGB and NIR*. These annotated patterns or anomalies had a substancial impact in field conditions and subsequently crop yield [1].

For my TDI Capstone Project, I am using a subset of these data (~ 4.4 Gb) representing the images collected in 2019. These are the same data used for the [CVPR Workshop Challenge](https://www.agriculture-vision.com/) held in June 2020. There is also more information on their [GitHub page](https://github.com/SHI-Labs/Agriculture-Vision) about this challenge.

This subset dataset contains over 21,000 farmland images from 2019, and six annotatios: *cloud shadow, double plant, planter skip, standing water, waterway and weed cluster*. These six patterns are stored separately as binary masks due to potential overlaps between patterns. Each field image has a file name in the format of \(field id)_(x1)-(y1)-(x2)-(y2).(jpg/png). Each field id uniquely identifies the farmland that the image is cropped from, and (x1, y1, x2, y2) is a 4-tuple indicating the position in which the image is cropped.


#why
### Why Agriculture-Vision?**


---
#conda
## 2 - Conda Environment

```{bash}
$ conda env create -f tdi_env.yml

$  conda activate tdi_env

(tdi_env) $  which jupyter
/Users/grachetng/miniconda3/envs/tdi_env/bin/jupyter

(tdi_env) $  jupyter notebook
```

I had a few installation issues. The only way it worked for me was installing libraries in the jupyter [notebook](1_install_libraries.ipynb).


---
#download
## 3 - Download

I contacted the authors of the paper [1], and they sent me a link to a Google Drive where the data was deposited.


---
#dataprep
## 4 - Exploratory analysis - data preparation

For my initial exploratory analysis, I decided to use a partial dataset because I don't know how to handle multiple label classes for a single image yet.

GoogleColab and my computer can't handle this massive amount of data, so I am limiting my exploratory analysis to include only images with single labels from the validation set, which yielded 4,714 total images.

1. To selected only validation masks that have one label, I tested if the [image masks](./2_get_single_image_files.ipynb), which were black & white, were all black (no label) in them using `.getextrema() == (0, 0)`. I added that information in a dictionary data structure that I converted into a `pd.DataFrame()`.

2. Then, I saved the RGB images into a `partial_dataset` directory for training the model.


---
#cnn
## 5 - Exploratory CNN model development

My first model was a Convolutional Neural Network (CNN). I divided the dataset into training (2,828) and test (1,886) datasets, and resized the images to (300, 300). I also used all six classes: cloud shadow, double_plant, planter skip, standing water, waterway, and weed cluster, and each label received a number from 0 to 5, respectively.

The CNN model isn't great. It has a 72% accuracy on test data. I have not done hyperparamenter tunning, because in the original paper [1] the authors discussed that the model they recommend for these data is Intersection over Union (IoU).


---
#app
## 6 - Preliminary Project App

![CNN App](cnn_app.gif)


---
#references
## References

1 - Mang Tik Chiu, Xingqian Xu, Yunchao Wei, Zilong Huang, Alexander Schwing, Robert Brunner,  Hrant Khachatrian, Hovnatan Karapetyan, Ivan Dozier, Greg Rose, David Wilson, Adrian Tudor, Naira Hovakimyan, Thomas S. Huang, and Honghui  Shi. Agriculture-vision: A large aerial image database for agricultural pattern analysis. arXiv preprint arXiv:2001.01306, 2020
