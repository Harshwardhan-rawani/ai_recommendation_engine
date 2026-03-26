import reflex as rx
from ai_recomadation_system.state.user_state import UserState
from ai_recomadation_system.state.cart_state import CartState

def navbar():
    return rx.flex(
        rx.link(
            rx.heading("AI Store", size="6", color="white", weight="bold"),
            href="/",
            text_decoration="none"
        ),
        rx.flex(
            rx.link("Products", href="/products", color="white", _hover={"color": "gray.300"}, margin_right="1rem"),
            rx.link(
                rx.flex(
                    "Cart",
                    rx.badge(CartState.cart_count, color_scheme="red", border_radius="full", padding_x="0.5rem", margin_left="0.5rem"),
                    align="center"
                ),
                href="/cart", 
                color="white",
                _hover={"color": "gray.300"},
                margin_right="2rem"
            ),
            rx.cond(
                UserState.logged_in,
                rx.flex(
                    rx.link("Profile", href="/profile", color="white", _hover={"color": "gray.300"}, margin_right="1rem"),
                    rx.button("Logout", on_click=UserState.logout, color_scheme="red", variant="solid", size="1"),
                    align="center"
                ),
                rx.link("Login", href="/login", color="white", _hover={"color": "gray.300"}),
            ),
            align="center",
        ),
        justify="between",
        align="center",
        bg="black",
        padding="1rem 2rem",
        box_shadow="0 4px 6px -1px rgba(0,0,0,0.1)",
        width="100%",
        position="sticky",
        top="0",
        z_index=100
    )
