import reflex as rx
from ai_recomadation_system.state.cart_state import CartState

def product_card(product: dict):
    return rx.card(
        rx.vstack(
            # Product Image with hover effect
            rx.box(
                rx.image(
                    src=product['image_url'],
                    width="100%",
                    height="220px",
                    object_fit="cover",
                    border_radius="8px",
                    transition="transform 0.3s ease",
                    _hover={"transform": "scale(1.05)"}
                ),
                width="100%",
                overflow="hidden",
                border_radius="8px",
                margin_bottom="1rem"
            ),

            # Product Info Section
            rx.vstack(
                # Product Name
                rx.heading(
                    product['product_name'],
                    size="4",
                    font_weight="600",
                    line_height="1.3",
                    margin_bottom="0.5rem",
                    no_of_lines=2
                ),

                # # Category Badge
                # rx.badge(
                #     product['category'],
                #     color_scheme="blue",
                #     variant="soft",
                #     size="1",
                #     margin_bottom="0.75rem"
                # ),

                # Price and Rating Row
                rx.flex(
                    rx.text(
                        f"${product['price']}",
                        font_size="1.25rem",
                        font_weight="700",
                        color="green.600"
                    ),
                    rx.flex(
                        rx.icon("star", size=16, color="yellow.500"),
                        rx.text(
                            f"{product['rating']}",
                            font_size="0.9rem",
                            font_weight="500",
                            color="gray.700"
                        ),
                        align="center",
                        spacing="1"
                    ),
                    justify="between",
                    align="center",
                    width="100%",
                    margin_bottom="1rem"
                ),

                spacing="0",
                align_items="start",
                width="100%"
            ),

            # Action Buttons Section
            rx.vstack(
                # View Details Button
                rx.link(
                    rx.button(
                        rx.flex(
                            rx.text("View Details", font_weight="500"),
                            rx.icon("eye", size=16),
                            align="center",
                            justify="center",
                            spacing="2"
                        ),
                        width="100%",
                        variant="outline",
                        color_scheme="blue",
                        size="3",
                        border_radius="6px",
                        _hover={
                            "bg": "blue.50",
                            "border_color": "blue.300"
                        }
                    ),
                    href=rx.cond(
                        product['product_id'] != "",
                        f"/product/{product['product_id']}",
                        "#"
                    ),
                    width="100%",
                    text_decoration="none"
                ),

                # Add to Cart Button
                rx.button(
                    rx.flex(
                        rx.text("Add to Cart", font_weight="500"),
                        rx.icon("shopping-cart", size=16),
                        align="center",
                        justify="center",
                        spacing="2"
                    ),
                    width="100%",
                    color_scheme="green",
                    size="3",
                    border_radius="6px",
                    on_click=CartState.add_to_cart(product),
                    _hover={
                        "bg": "green.600",
                        "transform": "translateY(-1px)"
                    },
                    transition="all 0.2s ease"
                ),

                spacing="3",
                width="100%"
            ),

            spacing="0",
            align_items="start",
            width="100%",
            height="100%"
        ),
        width="100%",
        max_width="320px",
        padding="1.5rem",
        border_radius="12px",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
        border="1px solid",
        border_color="gray.200",
        _hover={
            "box_shadow": "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
            "transform": "translateY(-2px)"
        },
        transition="all 0.3s ease",
        cursor="pointer"
    )

def recommendation_card(product: dict, reason: str = ""):
    return rx.box(
        # Recommendation badge
        rx.badge(
            "Recommended",
            color_scheme="purple",
            position="absolute",
            top="-8px",
            right="-8px",
            z_index=10,
            font_size="0.7rem",
            padding="0.25rem 0.5rem"
        ),

        # Reason text if provided
        rx.cond(
            reason != "",
            rx.box(
                rx.flex(
                    rx.icon("sparkles", size=14, color="purple.500"),
                    rx.text(
                        reason,
                        size="2",
                        color="purple.600",
                        font_weight="500"
                    ),
                    align="center",
                    spacing="1"
                ),
                padding="0.5rem",
                bg="purple.50",
                border_radius="6px",
                margin_bottom="1rem",
                border="1px solid",
                border_color="purple.200"
            )
        ),

        # Enhanced product card
        product_card(product),

        position="relative"
    )
