import reflex as rx
from ai_recomadation_system.state.user_state import UserState
from ai_recomadation_system.components.navbar import navbar

def signup() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.card(
                rx.vstack(
                    rx.heading("Sign Up", size="6"),
                    rx.text("Create an account to join", color="gray", size="2"),
                    rx.cond(
                        UserState.auth_error != "",
                        rx.callout(
                            UserState.auth_error,
                            color_scheme="red",
                        )
                    ),
                    rx.input(placeholder="Email", on_blur=UserState.set_email, width="100%"),
                    rx.input(placeholder="Password", type="password", on_blur=UserState.set_password, width="100%"),
                    rx.button("Sign Up", on_click=UserState.signup, width="100%", size="3"),
                    rx.link("Already have an account? Login", href="/login", size="2"),
                    spacing="4",
                    width="100%"
                ),
                width="400px",
                padding="2rem",
                margin_top="10vh",
                box_shadow="xl"
            ),
            width="100%"
        ),
        height="100vh",
        bg="gray.50"
    )
