# important imports
import numpy as np
import pandas as pd
import cv2

# redis database
import redis

# insightface
from insightface.app import FaceAnalysis

# ml search algo
from sklearn.metrics import pairwise

# Connect to redis client
# redis-10581.c74.us-east-1-4.ec2.redns.redis-cloud.com:10581
# sk2XSE7YT6NWLFacA0N3CkasM97yF19a
hostname = "redis-10581.c74.us-east-1-4.ec2.redns.redis-cloud.com"
portnumber = 10581
password = "sk2XSE7YT6NWLFacA0N3CkasM97yF19a"

r = redis.StrictRedis(host= hostname, port= portnumber, password= password);

# Configure face analysis
faceapp = FaceAnalysis(name='buffalo_l', root='insightface_model', providers=['CPUExecutionProvider'])
faceapp.prepare(ctx_id=0, det_size=(640,640), det_thresh=0.5)

# ML search algo
def ml_search_algorithm(dataframe, feature_column, test_vector, name_role=['Name', 'Role'], thresh=0.5):
    """
    Searches for the most similar embedding in the DataFrame using cosine similarity.
    
    Args:
    - dataframe (pd.DataFrame): DataFrame containing embeddings and metadata.
    - feature_column (str): Column name where embeddings are stored.
    - test_vector (np.ndarray): The embedding vector for comparison.
    - name_role (list): List containing column names for 'Name' and 'Role'.
    - thresh (float): Cosine similarity threshold for matching.

    Returns:
    - person_name (str): Name of the matched person or 'Unknown'.
    - person_role (str): Role of the matched person or 'Unknown'.
    """
    # STEP 1: Make a copy of the DataFrame to avoid modifying the original
    dataframe = dataframe.copy()

    # STEP 2: Extract embeddings from the feature column
    X_list = dataframe[feature_column].tolist()

    # STEP 3: Validate and stack embeddings into a 2D NumPy array
    try:
        X = np.vstack(X_list)  # Stack all embeddings into a 2D array
    except ValueError as e:
        raise ValueError(f"Error stacking embeddings. Ensure all embeddings have consistent dimensions. Details: {e}")

    # Check if the test vector is valid
    if test_vector.shape[0] != X.shape[1]:
        raise ValueError(f"Test vector shape {test_vector.shape} does not match embedding dimensions {X.shape[1]}.")

    # STEP 4: Calculate the cosine similarity between all embeddings and the test vector
    similar = pairwise.cosine_similarity(X, test_vector.reshape(1, -1)).flatten()

    # Add similarity scores to the DataFrame
    dataframe['cosine'] = similar

    # STEP 5: Filter matches based on the similarity threshold
    data_filter = dataframe.query(f'cosine >= {thresh}')
    if not data_filter.empty:
        # STEP 6: Identify the best match (highest similarity score)
        argmax = data_filter['cosine'].idxmax()
        person_name, person_role = data_filter.loc[argmax, name_role]
    else:
        # No matches above the threshold
        person_name = 'Unknown'
        person_role = 'Unknown'

    return person_name, person_role

# FN FOR FACE PREDICTION

def face_prediction(resized_test_image, dataframe, feature_column, name_role = ['Name', 'Role'], thresh=0.5):
    
    # take the test image and apply to model
    results = faceapp.get(resized_test_image)
    resized_test_copy = resized_test_image.copy()
    
    # loop and extract each face embedding using ml_search_algorithm
    for res in results:
        x1, y1, x2, y2 = res['bbox'].astype(int)
        embeddings = res['embedding']
        person_name, person_role = ml_search_algorithm(dataframe, feature_column, test_vector=embeddings,name_role=name_role, thresh=thresh)           
    
        if(person_name == 'Unknown') :
            color = (0,0,255)
        else : 
            color = (0,255,0)
            
        # print(person_name, person_role)
        cv2.rectangle(resized_test_copy, (x1, y1), (x2, y2), color)
    
        text_gen = person_name
        cv2.putText(resized_test_copy, text_gen, (x1, y1), cv2.FONT_HERSHEY_DUPLEX, 0.7, color, 2)
    
    return resized_test_copy






