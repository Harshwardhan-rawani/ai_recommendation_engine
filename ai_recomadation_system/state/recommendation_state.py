import reflex as rx
from ai_recomadation_system.backend.recommender import get_recommendations
from .user_state import UserState
from ai_recomadation_system.backend.cleaning_data import load_and_clean_data, get_unique_products

class RecommendationState(rx.State):
    recommendations: list[dict] = []
    all_products: list[dict] = []
    is_loading: bool = False
    
    # Track the last viewed product to influence content-based filtering
    viewed_product_id: str = ""
    
    # Search and filtering
    search_query: str = ""
    selected_category: str = "All"
    
    @rx.var
    def available_categories(self) -> list[str]:
        # Extract unique categories and prepend "All"
        categories = sorted(list({str(p.get('category', '')) for p in self.all_products if p.get('category')}))
        return ["All"] + [c for c in categories if c]
        
    @rx.var
    def filtered_products(self) -> list[dict]:
        products = self.all_products
        
        if self.selected_category != "All":
            products = [p for p in products if p.get('category') == self.selected_category]
            
        if self.search_query:
            query = self.search_query.lower()
            products = [
                p for p in products if 
                query in str(p.get('product_name', '')).lower() or 
                query in str(p.get('description', '')).lower() or
                query in str(p.get('brand', '')).lower()
            ]
            
        return products
    
    def load_all_products(self):
        df = load_and_clean_data()
        if not df.empty:
            self.all_products = get_unique_products(df).to_dict('records')
            
    async def fetch_recommendations(self):
        """ Call ML logic depending on user state """
        self.is_loading = True
        yield
        
        import asyncio
        await asyncio.sleep(0.01)
        
        # We need to access UserState dataset_user_id
        parent: UserState = await self.get_state(UserState)
        
        user_id = parent.dataset_user_id if parent.logged_in else None
        
        # Call backend
        self.recommendations = get_recommendations(
            user_id=user_id if user_id != -1 else None,
            viewed_product_id=self.viewed_product_id if self.viewed_product_id else None
        )
        self.is_loading = False
        yield

    async def set_viewed_product(self, pid: str):
        self.viewed_product_id = pid
        async for update in self.fetch_recommendations():
            yield update
        
    async def on_load_home(self):
        # Always refresh source data and then fetch recommendations
        self.load_all_products()
        async for update in self.fetch_recommendations():
            yield update
