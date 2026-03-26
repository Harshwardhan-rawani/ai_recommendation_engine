import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .cleaning_data import get_unique_products

def get_content_based_recommendations(df, product_id, top_n=5):
    """
    Recommends products similar to the given product_id based on tags.
    """
    if df.empty:
        return []
        
    products_df = get_unique_products(df).reset_index(drop=True)
    
    if product_id not in products_df['product_id'].values:
        return []
        
    # TF-IDF on Tags
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(products_df['tags'])
    
    # Cosine Similarity
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    # Find index of the product
    idx = products_df.index[products_df['product_id'] == product_id].tolist()[0]
    
    # Get similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get top_n similar products (excluding itself)
    sim_scores = sim_scores[1:top_n+1]
    
    product_indices = [i[0] for i in sim_scores]
    similar_products = products_df.iloc[product_indices].to_dict('records')
    
    return similar_products
