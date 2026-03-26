import reflex as rx
from ai_recomadation_system.state.recommendation_state import RecommendationState
from ai_recomadation_system.components.navbar import navbar
from ai_recomadation_system.components.footer import footer
from ai_recomadation_system.components.product_card import product_card

def products() -> rx.Component:
    return rx.box(
        navbar(),
        rx.container(
            rx.heading("All Products", size="7", margin_y="2rem"),
            rx.flex(
                rx.input(
                    placeholder="Search products...", 
                    value=RecommendationState.search_query,
                    on_change=RecommendationState.set_search_query,
                    width="100%",
                    max_width="400px"
                ),
                rx.select(
                    RecommendationState.available_categories,
                    value=RecommendationState.selected_category,
                    on_change=RecommendationState.set_selected_category,
                    width="100%",
                    max_width="250px"
                ),
                spacing="4",
                margin_bottom="2rem",
                width="100%",
                align="center",
                flex_wrap="wrap"
            ),
            rx.cond(
                RecommendationState.is_loading,
                rx.center(
                    rx.spinner(size="3"),
                    rx.text("Gathering products...", margin_left="1rem", color="gray"),
                    padding="3rem", width="100%"
                ),
                rx.grid(
                    rx.foreach(
                        RecommendationState.filtered_products,
                        product_card
                    ),
                    columns=rx.breakpoints(initial="1", sm="2", md="3", lg="4"),
                    spacing="4",
                    width="100%"
                )
            ),
            max_width="1200px",
            margin="0 auto",
            padding_bottom="4rem"
        ),
        footer()
    )
