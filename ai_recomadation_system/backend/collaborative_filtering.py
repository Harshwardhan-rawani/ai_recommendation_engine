import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from ai_recomadation_system.backend.cleaning_data import get_unique_products

def get_collaborative_recommendations(df, user_id, top_n=5):
    """
    Recommend products for a given user_id using user-based collaborative filtering.
    """
    if df.empty or user_id not in df['user_id'].values:
        return []
        
    # Create user-item matrix
    user_item_matrix = df.pivot_table(index='user_id', columns='product_id', values='rating').fillna(0)
    
    if user_id not in user_item_matrix.index:
        return []
        
    # Compute user similarity
    user_sim = cosine_similarity(user_item_matrix)
    user_sim_df = pd.DataFrame(user_sim, index=user_item_matrix.index, columns=user_item_matrix.index)
    
    # Get similar users
    similar_users = user_sim_df[user_id].sort_values(ascending=False).index[1:]
    
    # Get products the current user hasn't rated
    user_rated_products = set(df[df['user_id'] == user_id]['product_id'])
    
    recommendations = {}
    for similar_user in similar_users:
        if len(recommendations) >= top_n:
            break
            
        # Products rated highly by similar user
        sim_user_ratings = user_item_matrix.loc[similar_user]
        top_sim_user_products = sim_user_ratings[sim_user_ratings >= 4.0].index.tolist()
        
        for pid in top_sim_user_products:
            if pid not in user_rated_products and pid not in recommendations:
                recommendations[pid] = 1
            if len(recommendations) >= top_n:
                break
                
    recommended_product_ids = list(recommendations.keys())
    
    # Fetch product details
    products_df = get_unique_products(df)
    recommended_items = products_df[products_df['product_id'].isin(recommended_product_ids)].to_dict('records')
    return recommended_items
