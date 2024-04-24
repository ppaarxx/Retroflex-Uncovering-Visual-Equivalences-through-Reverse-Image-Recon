import os
import pickle

# Get the current folder path
current_folder = os.getcwd()
data_folder = os.path.join(current_folder, '..', 'Code','data')

# Load the filenames_test.pickle file
filenames_test_path = os.path.join(data_folder, 'filenames_unsplash.pickle')
with open(filenames_test_path, 'rb') as f:
    filenames_test = pickle.load(f)

# Get the new path from user input
new_path = input("Enter the new path for the filenames_test.pickle file: ")

# Modify the paths inside the filenames_test list
filenames_test = [os.path.join(new_path, os.path.basename(filename)) for filename in filenames_test]

# Save the modified filenames_test list back to the pickle file
with open(filenames_test_path, 'wb') as f:
    pickle.dump(filenames_test, f)
