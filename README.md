# TDI Capstone Project

## Content

- [1 - AgricultureVision](#agriculturevision)
- [2 - Conda Environment](#conda-environment)
- [3 - Download](#download)
- [References](#references)


## 1 - AgricultureVision

The AgricultureVision dataset [1] is joint effort with many research scientists to bring artificial intelligence and agriculture together.

The complete dataset contains more than 94,000 high-resolution images from over three thousand farmlands in the US. These images were collected between 2017 and 2019. Each image was annotated with *double plant, drydown, endrow, nutrient deficiency, planter skip, storm damage, water, waterway and weed cluster*, and contains four channels: *RGB and NIR*. These annotated patterns or anomalies had a substancial impact in field conditions and subsequently crop yield [1].

For my TDI Capstone Project, I am using a subset of these data (~ 4.4 Gb) representing the images collected in 2019. These are the same data used for the [CVPR Workshop Challenge](https://www.agriculture-vision.com/) held in June 2020. There is also more information on their [GitHub page](https://github.com/SHI-Labs/Agriculture-Vision) about this challenge.

This subset dataset contains over 21,000 farmland images from 2019, and six annotatios: *cloud shadow, double plant, planter skip, standing water, waterway and weed cluster*. These six patterns are stored separately as binary masks due to potential overlaps between patterns. Each field image has a file name in the format of \(field id)_(x1)-(y1)-(x2)-(y2).(jpg/png). Each field id uniquely identifies the farmland that the image is cropped from, and (x1, y1, x2, y2) is a 4-tuple indicating the position in which the image is cropped.


## 2 - Conda Environment

```{bash}
$ conda env create -f tdi_env.yml

$  conda activate tdi_env

(tdi_env) $  conda install -c conda-forge tensorflow==1.15
```

## 3 - [Download](0_download_data.ipynb)

I contacted the authors of the paper [1], and they sent me a link to a Google Drive where the data was deposited.


## References

1 - Mang Tik Chiu, Xingqian Xu, Yunchao Wei, Zilong Huang, Alexander Schwing, Robert Brunner,  Hrant Khachatrian, Hovnatan Karapetyan, Ivan Dozier, Greg Rose, David Wilson, Adrian Tudor, Naira Hovakimyan, Thomas S. Huang, and Honghui  Shi. Agriculture-vision: A large aerial image database for agricultural pattern analysis. arXiv preprint arXiv:2001.01306, 2020
