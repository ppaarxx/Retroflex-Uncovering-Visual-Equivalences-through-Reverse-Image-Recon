import pickle
import numpy as np
from sklearn.decomposition import PCA
from sklearn.neighbors import NearestNeighbors
from tqdm import tqdm
import os

# Get the current folder path
current_folder = os.getcwd()
data_folder = os.path.join(current_folder, 'data')

# Load filenames and compressed feature list
filenames_path = os.path.join(data_folder, 'filenames_unsplash.pickle')
with open(filenames_path, 'rb') as f:
    filenames = pickle.load(f)

compressed_feature_list_path = os.path.join(data_folder, 'compressed_feature_list.pkl')
with open(compressed_feature_list_path, 'rb') as f:
    compressed_feature_list = pickle.load(f)

ipca_path = os.path.join(data_folder, 'ipca.pickle')
with open(ipca_path, 'rb') as f:
    ipca = pickle.load(f)


# Reshape the feature list
n_features = feature_vector_length = len(compressed_feature_list[0])
X = np.array(compressed_feature_list).reshape(-1, n_features)

# Initialize Nearest Neighbors
num_results = 5
neighbors = NearestNeighbors(n_neighbors=num_results, algorithm='kd_tree', metric='euclidean').fit(X)

def perform_search(query_features, num_results):

    # Reshape the query features
    query_features_reshaped = np.array(query_features).reshape(1, -1)

    query_features_compressed = ipca.transform(query_features_reshaped)
    neighbors.set_params(n_neighbors=num_results)
    # Find the nearest neighbors
    distances, indices = neighbors.kneighbors(query_features_compressed)

    # Get filenames of similar images
    similar_images = [filenames[i] for i in indices[0]]

    return similar_images
