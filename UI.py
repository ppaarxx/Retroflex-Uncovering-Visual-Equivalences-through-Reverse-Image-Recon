import streamlit as st
from PIL import Image
import os
from feature_extractor import extract_features
from searcher import perform_search

# Set page configuration to wide mode
st.set_page_config(layout="wide")

# Function to perform reverse image search using uploaded image
def reverse_image_search(uploaded_image, num_results):
    # Extract features from the query image
    query_features = extract_features(uploaded_image)

    # Perform search using searcher
    similar_images = perform_search(query_features, num_results)

    return similar_images

# Main Streamlit UI
def main():
    st.title("Reverse Image Search")

    # Sidebar for query image and number of results
    uploaded_image = st.sidebar.file_uploader("Upload query image", type=["jpg", "png", "jpeg"], help="Limit 200MB per file")
    

    # Display uploaded image preview in sidebar
    if uploaded_image is not None:
        st.sidebar.subheader("Query Image Preview")
        st.sidebar.image(uploaded_image, caption='Uploaded Image', use_column_width=True)

    num_results = st.sidebar.slider("Number of Results", min_value=1, max_value=100, value=5)
    # Search button
    if st.sidebar.button("Search") and uploaded_image is not None:
        # Perform reverse image search with the selected number of results
        similar_images = reverse_image_search(uploaded_image, num_results)


        # Display resultant images in main layout
        st.subheader("Resultant Images")

        # Calculate number of columns based on number of results
        num_columns = 3
        num_rows = (len(similar_images) + num_columns - 1) // num_columns

        # Create grid layout for displaying images
        for i in range(num_rows):
            cols = st.columns(num_columns)
            for j in range(num_columns):
                index = i * num_columns + j
                if index < len(similar_images):
                    image_path = os.path.join('Cat', similar_images[index])
                    image = Image.open(image_path)
                    cols[j].image(image, caption='Result Image', use_column_width=True)

if __name__ == "__main__":
    main()
