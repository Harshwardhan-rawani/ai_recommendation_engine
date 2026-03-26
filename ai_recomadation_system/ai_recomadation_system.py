import reflex as rx
from ai_recomadation_system.pages.home import index
from ai_recomadation_system.pages.login import login
from ai_recomadation_system.pages.signup import signup
from ai_recomadation_system.pages.products import products
from ai_recomadation_system.pages.product_detail import product_detail, ProductDetailState
from ai_recomadation_system.pages.cart import cart
from ai_recomadation_system.pages.checkout import checkout
from ai_recomadation_system.pages.payment import payment, payment_success
from ai_recomadation_system.pages.profile import profile
from ai_recomadation_system.pages.recommendation import recommendation
from ai_recomadation_system.state.recommendation_state import RecommendationState
from ai_recomadation_system.state.cart_state import CartState

app = rx.App(
    theme=rx.theme(
        appearance="light",
        has_background=True,
        radius="large",
        accent_color="indigo"
    )
)

app.add_page(index, route="/", on_load=RecommendationState.on_load_home)
app.add_page(login, route="/login")
app.add_page(signup, route="/signup")
app.add_page(products, route="/products", on_load=RecommendationState.on_load_home)

@rx.page(route="/product/[pid]", on_load=[
    RecommendationState.load_all_products,
    lambda: ProductDetailState.load_product(rx.State.router.page.params.get("pid", ""))
])
def product_page():
    return product_detail()

app.add_page(cart, route="/cart")
app.add_page(checkout, route="/checkout")
app.add_page(payment, route="/payment")
app.add_page(payment_success, route="/payment-success", on_load=CartState.clear_cart)
app.add_page(profile, route="/profile")
app.add_page(recommendation, route="/recommendation", on_load=RecommendationState.on_load_home)
