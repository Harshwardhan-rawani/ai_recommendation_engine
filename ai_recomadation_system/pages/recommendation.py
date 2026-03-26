import reflex as rx
from ai_recomadation_system.state.recommendation_state import RecommendationState
from ai_recomadation_system.state.user_state import UserState
from ai_recomadation_system.components.navbar import navbar
from ai_recomadation_system.components.footer import footer
from ai_recomadation_system.components.product_card import recommendation_card

def recommendation() -> rx.Component:
    return rx.box(
        navbar(),
        rx.container(
            rx.vstack(
                rx.heading("Inside the ML Engine", size="7", margin_y="2rem"),
                rx.text(
                    "Here is a breakdown of your personalized AI recommendations.",
                    color="gray", size="4", margin_bottom="2rem"
                ),
                rx.cond(
                    UserState.user_type == "new",
                    rx.callout("As a new user, you are seeing Top Rated items overall based on product grouping.", icon="info", color_scheme="cyan", width="100%", margin_bottom="2rem"),
                    rx.cond(
                        UserState.user_type == "existing",
                        rx.callout("As an existing user, we apply Collaborative Filtering (similar users) and Content Filtering (TF-IDF on Tags) to show these.", icon="info", color_scheme="indigo", width="100%", margin_bottom="2rem"),
                        rx.callout("Please log in to see recommendations based on ML models.", color_scheme="orange", width="100%", margin_bottom="2rem")
                    )
                ),
                rx.cond(
                    RecommendationState.is_loading,
                    rx.center(
                        rx.spinner(size="3"),
                        rx.text("Processing with AI models...", margin_left="1rem", color="gray"),
                        padding="3rem", margin_y="2rem", width="100%"
                    ),
                    rx.cond(
                        RecommendationState.recommendations.length() > 0,
                        rx.grid(
                            rx.foreach(
                                RecommendationState.recommendations,
                                lambda p: recommendation_card(p, "Recommended Match")
                            ),
                            columns=rx.breakpoints(initial="1", sm="2", md="3", lg="4"),
                            spacing="4",
                            width="100%"
                        ),
                        rx.text("No specific recommendations at this time.", color="gray")
                    )
                )
            ),
            max_width="1200px",
            margin="0 auto",
            min_height="60vh"
        ),
        footer()
    )
