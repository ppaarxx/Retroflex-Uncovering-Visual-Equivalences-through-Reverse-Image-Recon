import numpy as np
from numpy.linalg import norm
from tqdm import tqdm
from keras.preprocessing import image
from keras.applications.efficientnet import EfficientNetB7, preprocess_input

model = EfficientNetB7(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

def extract_features(img_path):
    input_shape = (224, 224, 3)
    img = image.load_img(img_path, target_size=(input_shape[0], input_shape[1]))
    img_array = image.img_to_array(img)
    expanded_img_array = np.expand_dims(img_array, axis=0)
    preprocessed_img = preprocess_input(expanded_img_array)
    features = model.predict(preprocessed_img)
    flattened_features = features.flatten()
    normalized_features = flattened_features / norm(flattened_features)
    return normalized_features
