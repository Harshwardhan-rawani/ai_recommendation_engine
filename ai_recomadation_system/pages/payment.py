import reflex as rx
from ai_recomadation_system.state.cart_state import CartState
from ai_recomadation_system.components.navbar import navbar
from ai_recomadation_system.components.footer import footer

def payment() -> rx.Component:
    return rx.box(
        rx.script(src="https://checkout.razorpay.com/v1/checkout.js"),
        navbar(),
        rx.container(
            rx.center(
                rx.card(
                    rx.vstack(
                        rx.heading("Payment", size="6"),
                        rx.text("Mock Razorpay Test Payment", color="gray"),
                        rx.divider(margin_y="1rem"),
                        rx.flex(rx.text("Amount to Pay:"), rx.text(f"${CartState.cart_total}", weight="bold"), justify="between", width="100%"),
                        rx.button(
                            "Pay Now", 
                            color_scheme="blue", 
                            size="3", 
                            width="100%", 
                            margin_top="2rem",
                            on_click=CartState.process_payment
                        ),
                        spacing="4",
                        width="100%",
                        align="center"
                    ),
                    width="100%",
                    max_width="400px",
                    padding="2rem",
                    box_shadow="lg"
                ),
                width="100%",
                padding_y="4rem"
            ),
            max_width="1200px",
            margin="0 auto",
            min_height="60vh"
        ),
        footer()
    )

def payment_success() -> rx.Component:
    return rx.box(
        navbar(),
        rx.container(
            rx.center(
                rx.vstack(
                    rx.icon("check-circle", size=64, color="green"),
                    rx.heading("Payment Successful!", size="7", margin_top="1rem"),
                    rx.text("Your order has been placed successfully.", color="gray", size="4"),
                    rx.link(rx.button("Return to Home", size="3", margin_top="2rem"), href="/"),
                    align="center"
                ),
                width="100%",
                padding_y="10rem"
            ),
            max_width="1200px",
            margin="0 auto",
            min_height="60vh"
        ),
        footer()
    )
