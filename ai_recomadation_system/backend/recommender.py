from .cleaning_data import load_and_clean_data
from .rating_based import get_top_rated_products
from .collaborative_filtering import get_collaborative_recommendations
from .content_filtering import get_content_based_recommendations

def get_recommendations(user_id=None, viewed_product_id=None):
    """
    Gateway function for recommendations.
    IF new user: use rating-based
    ELSE: combine collaborative + content
    """
    df = load_and_clean_data()
    if df.empty:
        return []
        
    recommendations = []
    
    # Check if user is known and has rated items (existing user)
    existing_user = False
    if user_id is not None:
        try:
            numeric_user_id = int(user_id)
            if numeric_user_id in df['user_id'].values:
                existing_user = True
        except ValueError:
            pass
            
    if not existing_user:
        # New user -> Rating based
        recommendations = get_top_rated_products(df, top_n=5)
    else:
        # Existing user -> Combine collaborative and content
        numeric_user_id = int(user_id)
        collab_recs = get_collaborative_recommendations(df, numeric_user_id, top_n=3)
        
        content_recs = []
        if viewed_product_id:
            # Recommend similar items based on recently viewed product
            content_recs = get_content_based_recommendations(df, viewed_product_id, top_n=3)
        elif len(collab_recs) > 0:
            # Fallback for content if we have collab recs: base on the first collab rec
            content_recs = get_content_based_recommendations(df, collab_recs[0]['product_id'], top_n=2)
            
        # Combine uniquely
        seen_pids = set()
        for item in collab_recs + content_recs:
            if item['product_id'] not in seen_pids:
                recommendations.append(item)
                seen_pids.add(item['product_id'])
                
    # If still not enough or empty, fill with top-rated
    if not recommendations:
        recommendations = get_top_rated_products(df, top_n=5)
        
    return recommendations
