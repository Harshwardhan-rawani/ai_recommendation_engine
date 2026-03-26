import reflex as rx
from ai_recomadation_system.state.recommendation_state import RecommendationState
from ai_recomadation_system.state.cart_state import CartState
from ai_recomadation_system.components.navbar import navbar
from ai_recomadation_system.components.footer import footer

class ProductDetailState(rx.State):
    product: dict = {}
    
    async def load_product(self, pid: str):
        # Default empty product struct
        self.product = {}
        if pid == "":
            return

        # Notify RecommendationState that we viewed a product
        recommendation_state = await self.get_state(RecommendationState)
        await recommendation_state.set_viewed_product(pid)

        # Load the product details
        for p in recommendation_state.all_products:
            if p['product_id'] == str(pid):
                self.product = p
                return
                
def product_detail() -> rx.Component:
    return rx.box(
        navbar(),
        rx.container(
            rx.cond(
                ProductDetailState.product.contains("product_name"),
                rx.flex(
                    rx.image(src=ProductDetailState.product['image_url'], width="100%", max_width="500px", object_fit="cover", border_radius="lg"),
                    rx.vstack(
                        rx.heading(ProductDetailState.product['product_name'], size="8"),
                        rx.badge(ProductDetailState.product['category'], color_scheme="blue", size="3"),
                        rx.text(ProductDetailState.product['description'], size="5", color="gray", margin_y="1rem"),
                        rx.flex(
                            rx.text(f"${ProductDetailState.product['price']}", size="8", weight="bold"),
                            rx.badge(rx.icon("star", size=18), f" {ProductDetailState.product['rating']}", color_scheme="yellow", size="3"),
                            align="center",
                            justify="between",
                            width="250px",
                            margin_bottom="2rem"
                        ),
                        rx.button("Add to Cart", size="4", color_scheme="green", width="250px", on_click=lambda: CartState.add_to_cart(ProductDetailState.product)),
                        align_items="start",
                        margin_left=rx.breakpoints(initial="0", md="3rem"),
                        margin_top=rx.breakpoints(initial="2rem", md="0")
                    ),
                    direction=rx.breakpoints(initial="column", md="row"),
                    margin_top="3rem"
                ),
                rx.center(rx.spinner(size="3"), height="50vh")
            ),
            max_width="1200px",
            margin="0 auto",
            min_height="60vh"
        ),
        footer()
    )
