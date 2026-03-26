import reflex as rx

def footer():
    return rx.box(
        rx.text("© 2026 AI Store. All rights reserved.", color="gray", size="2"),
        rx.text("Built with Reflex & Machine Learning", color="gray", size="2", margin_top="0.5rem"),
        width="100%",
        text_align="center",
        padding="2rem",
        bg="black",
        margin_top="3rem"
    )
