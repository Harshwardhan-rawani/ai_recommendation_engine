import pandas as pd
import os

def load_and_clean_data(file_path="clean_data.csv"):
    """
    Loads dataset, drops missing and invalid entries, and enforces types.
    """
    if not os.path.exists(file_path):
        # Fallback for when run from within a module
        file_path = os.path.join("..", file_path)
    
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        return pd.DataFrame()

    # Normalize column names to app-friendly names
    df.columns = df.columns.str.strip()
    rename_map = {
        "User's ID": 'user_id',
        'ProdID': 'product_id',
        'Rating': 'rating',
        'Review Count': 'review_count',
        'Category': 'category',
        'Brand': 'brand',
        'Name': 'product_name',
        'ImageURL': 'image_url',
        'Description': 'description',
        'Tags': 'tags'
    }
    df = df.rename(columns=rename_map)

    # Create missing columns with defaults to prevent key errors in UI paths
    for col, default in {
        'category': '',
        'brand': '',
        'product_name': '',
        'image_url': '',
        'description': '',
        'tags': ''
    }.items():
        if col not in df.columns:
            df[col] = default

    # Drop NAs in critical columns
    required = [c for c in ['user_id', 'product_id', 'rating', 'tags'] if c in df.columns]
    df = df.dropna(subset=required)

    # Convert types
    if 'user_id' in df.columns:
        df['user_id'] = pd.to_numeric(df['user_id'], errors='coerce')
    if 'rating' in df.columns:
        df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
    if 'review_count' in df.columns:
        df['review_count'] = pd.to_numeric(df['review_count'], errors='coerce')

    # Optional price field
    if 'price' in df.columns:
        df['price'] = pd.to_numeric(df['price'], errors='coerce')
    else:
        df['price'] = 0.0

    # Drop rows that couldn't be converted to numeric for critical fields
    df = df.dropna(subset=[c for c in ['user_id', 'rating'] if c in df.columns])

    # Clean up strings
    df['product_id'] = df['product_id'].astype(str)
    df['tags'] = df['tags'].astype(str)
    df['category'] = df['category'].astype(str)
    df['brand'] = df['brand'].astype(str)
    df['product_name'] = df['product_name'].astype(str)
    df['image_url'] = df['image_url'].astype(str)
    df['description'] = df['description'].astype(str)

    return df

def get_unique_products(df):
    """
    Returns a dataframe of unique products with their details.
    """
    return df.drop_duplicates(subset=['product_id']).copy()
