import reflex as rx
from ai_recomadation_system.state.recommendation_state import RecommendationState
from ai_recomadation_system.components.navbar import navbar
from ai_recomadation_system.components.footer import footer
from ai_recomadation_system.components.product_card import product_card

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.container(
            rx.vstack(
                rx.heading("Welcome to AI Store", size="8", margin_top="3rem"),
                rx.text("Personalized recommendations powered by Machine Learning.", size="4", color="gray"),
                
                rx.heading("Recommended For You", size="6", margin_top="3rem", margin_bottom="1rem"),
                rx.cond(
                    RecommendationState.is_loading,
                    rx.center(
                        rx.spinner(size="3"),
                        rx.text("Fetching best products for you...", margin_left="1rem", color="gray"),
                        padding="3rem", margin_y="2rem", width="100%"
                    ),
                    rx.cond(
                        RecommendationState.recommendations.length() > 0,
                        rx.grid(
                            rx.foreach(
                                RecommendationState.recommendations,
                                product_card
                            ),
                            columns=rx.breakpoints(
                                initial="1",
                                sm="2",
                                md="3",
                                lg="4"
                            ),
                            spacing="4",
                            width="100%"
                        ),
                        rx.text("No recommendations available right now.", color="gray")
                    )
                ),
                
                spacing="4",
                align_items="center",
                width="100%"
            ),
            width="100%",
            max_width="1200px",
            margin="0 auto",
            padding_bottom="4rem"
        ),
        footer(),
    )
