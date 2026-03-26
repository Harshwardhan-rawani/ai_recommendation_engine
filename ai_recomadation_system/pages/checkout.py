import reflex as rx
from ai_recomadation_system.state.user_state import UserState
from ai_recomadation_system.components.navbar import navbar
from ai_recomadation_system.components.footer import footer

class CheckoutState(rx.State):
    name: str = ""
    address: str = ""
    phone: str = ""
    
    def process_checkout(self):
        if not self.name or not self.address or not self.phone:
            return rx.window_alert("Please fill in all details.")
        return rx.redirect("/payment")

def checkout() -> rx.Component:
    return rx.box(
        navbar(),
        rx.container(
            rx.center(
                rx.card(
                    rx.vstack(
                        rx.heading("Checkout Details", size="6", margin_bottom="1rem"),
                        rx.input(placeholder="Full Name", on_blur=CheckoutState.set_name, width="100%"),
                        rx.text_area(placeholder="Shipping Address", on_blur=CheckoutState.set_address, width="100%"),
                        rx.input(placeholder="Phone Number", on_blur=CheckoutState.set_phone, width="100%"),
                        rx.button("Continue to Payment", on_click=CheckoutState.process_checkout, width="100%", size="3", color_scheme="green", margin_top="1rem"),
                        spacing="4",
                        width="100%"
                    ),
                    width="100%",
                    max_width="500px",
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
