import reflex as rx
from ai_recomadation_system.state.cart_state import CartState
from ai_recomadation_system.components.navbar import navbar
from ai_recomadation_system.components.footer import footer

def cart_item(item: dict):
    return rx.flex(
        rx.image(src=item['image_url'], width="100px", height="100px", object_fit="cover", border_radius="md"),
        rx.box(
            rx.heading(item['product_name'], size="4"),
            rx.text(item['category'], color="gray", size="2"),
            rx.text(f"${item['price']}", weight="bold", margin_top="0.5rem"),
            flex_grow="1",
            margin_left="1rem"
        ),
        rx.button(
            rx.icon("trash-2"), 
            color_scheme="red", 
            variant="ghost",
            on_click=CartState.remove_from_cart(item['product_id'])
        ),
        width="100%",
        align="center",
        border_bottom="1px solid #eaeaea",
        padding_y="1rem"
    )

def cart() -> rx.Component:
    return rx.box(
        navbar(),
        rx.container(
            rx.heading("Shopping Cart", size="7", margin_y="2rem"),
            rx.cond(
                CartState.cart_count > 0,
                rx.flex(
                    rx.vstack(
                        rx.foreach(CartState.cart_items, cart_item),
                        width="100%",
                        flex="2"
                    ),
                    rx.card(
                        rx.vstack(
                            rx.heading("Order Summary", size="5"),
                            rx.flex(rx.text("Subtotal"), rx.text(f"${CartState.cart_total}"), justify="between", width="100%"),
                            rx.divider(),
                            rx.flex(rx.text("Total", weight="bold"), rx.text(f"${CartState.cart_total}", weight="bold"), justify="between", width="100%"),
                            rx.link(
                                rx.button("Proceed to Checkout", width="100%", size="3", color_scheme="blue", margin_top="1rem"),
                                href="/checkout",
                                width="100%"
                            ),
                            width="100%",
                            spacing="4"
                        ),
                        flex="1",
                        margin_left=rx.breakpoints(initial="0", md="2rem"),
                        margin_top=rx.breakpoints(initial="2rem", md="0"),
                        height="fit-content"
                    ),
                    width="100%",
                    align="start",
                    direction=rx.breakpoints(initial="column", md="row")
                ),
                rx.vstack(
                    rx.text("Your cart is empty.", size="4", color="gray"),
                    rx.link(rx.button("Continue Shopping"), href="/products"),
                    align="center",
                    margin_top="3rem",
                    width="100%"
                )
            ),
            max_width="1200px",
            margin="0 auto",
            padding_bottom="4rem",
            min_height="60vh"
        ),
        footer()
    )
