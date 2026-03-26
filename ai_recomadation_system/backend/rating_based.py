import pandas as pd
from .cleaning_data import get_unique_products

def get_top_rated_products(df, top_n=5):
    """
    Groups by product and computes average rating.
    Returns the top_n rated products.
    """
    if df.empty:
        return []
        
    # Calculate average rating and count for each product
    rating_stats = df.groupby('product_id').agg(
        avg_rating=('rating', 'mean'),
        rating_count=('rating', 'count')
    ).reset_index()
    
    # Sort by avg_rating and then rating_count
    # Filter for products with at least 1 rating (or a threshold)
    top_products = rating_stats.sort_values(by=['avg_rating', 'rating_count'], ascending=[False, False])
    
    top_product_ids = top_products.head(top_n)['product_id'].tolist()
    
    # Get details
    products_df = get_unique_products(df)
    recommended = products_df[products_df['product_id'].isin(top_product_ids)].to_dict('records')
    
    # Ensure exact order as top_product_ids
    recommended_dict = {item['product_id']: item for item in recommended}
    return [recommended_dict[pid] for pid in top_product_ids if pid in recommended_dict]
