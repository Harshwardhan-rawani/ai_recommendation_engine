import reflex as rx

config = rx.Config(
    app_name="ai_recomadation_system",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)