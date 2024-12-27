import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Example vectors
vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])

# Compute Cosine Similarity
cos_sim = cosine_similarity([vector_a], [vector_b])
print("Cosine Similarity:", cos_sim[0][0])
