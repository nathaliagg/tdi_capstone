
"""
Author : Nathalia Graf Grachet
Date   : 2021-01-31
Purpose: TDI Capstone Project
"""

import streamlit as st
import os
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
st.set_option('deprecation.showPyplotGlobalUse', False)


# --------------------------------------------------
def random_file():
    """ Sample a pd df and returns """

    to_sample = st.button('Click here to make a prediction')

    return to_sample


# --------------------------------------------------
def get_df(path_csv):

    val_df = pd.read_csv(path_csv)

    list_labels = [('cloud_shadow', 0), ('double_plant', 1), ('planter_skip', 2),
               ('standing_water', 3), ('waterway', 4), ('weed_cluster', 5)]

    for l in list_labels:
        val_df[l[0]] = val_df[l[0]].replace(1, l[1])

    val_df['filename'] = val_df['filename'].str.split('/').str[-1].str[:-4]+'.jpg'

    return val_df


# --------------------------------------------------
def read_image(data_x):
    """Read obj with the path for images.
    data_x ==  *_x
    """

    W, H = 300, 300 # set final size

    x = cv2.imread(data_x, cv2.IMREAD_COLOR) # read in colors
    x = cv2.resize(x, (W, H)) # resize
    x = x / 255.0 # normalize values 0 to 1
    x = x.astype(np.float32) # make it np.float32

    return x


# --------------------------------------------------
def get_label(label):

    list_labels = [('Cloud shadow', 0), ('Double plant', 1), ('Planter skip', 2),
               ('Standing water', 3), ('Waterway', 4), ('Weed cluster', 5)]

    for l in list_labels:
        if label == l[1]:
            return l[0]


# --------------------------------------------------
def make_prediction(df, model):

    # take a sample (== one random row) from val_df
    sample = df.sample()
    # get filename
    image = sample['filename'].to_list()[0]
    # get label
    label = int(sample.sum(axis=1).to_list()[0])
    # get path to the image
    image_path = os.path.join('dataset', 'Agriculture-Vision', 'train', 'images', 'rgb', image)
    # assert it exists
    assert os.path.exists(image_path) == True

    # predict
    img = read_image(image_path)
    prediction = model.predict(np.array([img]))
    predicted_value = np.argmax(prediction)

    return predicted_value, label, image_path


# --------------------------------------------------
def main():
    st.write('# Agriculture-Vision - TDI Capstone Project')

    st.write('## Exploratory CNN model')

    st.write(f"Tensorflow version: {tf.__version__}, and Keras version: {keras.__version__}")

    val_df = get_df('training_singles.csv')

    cnn_model = keras.models.load_model('./model_1_CNN')

    acc = 72.06
    st.write(f"Current Model Accuracy: {str(acc)}%")

    ## Prediction
    if random_file():
        predicted_value, label, image_path  = make_prediction(val_df, cnn_model)
        # plot the image and check if label match...
        img = read_image(image_path)
        st.write(f"The label: {get_label(label)}, and the model predicted: {get_label(predicted_value)}")
        plt.figure(figsize=(3,3))
        plt.imshow(img)
        plt.axis('off')
        st.pyplot()


# --------------------------------------------------
if __name__ == '__main__':
    main()
