import reflex as rx
from ai_recomadation_system.state.user_state import UserState
from ai_recomadation_system.components.navbar import navbar
from ai_recomadation_system.components.footer import footer

def profile() -> rx.Component:
    return rx.box(
        navbar(),
        rx.container(
            rx.heading("User Profile", size="7", margin_y="2rem"),
            rx.cond(
                UserState.logged_in,
                rx.card(
                    rx.vstack(
                        rx.icon("user", size=64, color="gray"),
                        rx.heading(UserState.email, size="5"),
                        rx.badge(f"Dataset ID: {UserState.dataset_user_id}", color_scheme="green"),
                        rx.badge(f"Type: {UserState.user_type.capitalize()} User", color_scheme="purple"),
                        rx.divider(margin_y="1rem"),
                        rx.text("Order History", weight="bold", size="4"),
                        rx.text("No past orders found.", color="gray"),
                        align="center",
                        spacing="3",
                        width="100%"
                    ),
                    width="100%",
                    max_width="400px",
                    padding="2rem",
                    margin="0 auto",
                    box_shadow="lg"
                ),
                rx.center(
                    rx.vstack(
                        rx.text("Please login to view your profile.", size="5"),
                        rx.link(rx.button("Login Now"), href="/login"),
                        align="center",
                        spacing="4"
                    ),
                    height="40vh"
                )
            ),
            max_width="1200px",
            margin="0 auto",
            min_height="60vh"
        ),
        footer()
    )
