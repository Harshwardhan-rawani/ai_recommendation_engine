import reflex as rx
import razorpay
import os

class CartState(rx.State):
    cart_items: list[dict] = []
    
    @rx.var
    def cart_total(self) -> float:
        return sum(float(item['price']) for item in self.cart_items)
        
    @rx.var
    def cart_count(self) -> int:
        return len(self.cart_items)

    def add_to_cart(self, product: dict):
        self.cart_items.append(product)
        
    def remove_from_cart(self, product_id: str):
        # Remove first occurrence of this product_id
        for i, item in enumerate(self.cart_items):
            if item['product_id'] == product_id:
                self.cart_items.pop(i)
                break
                
    def clear_cart(self):
        self.cart_items = []
        
    def process_payment(self):
        amount = int(self.cart_total * 100)
        if amount == 0:
            return rx.window_alert("Cart is empty!")
            
        razorpay_key = os.getenv("RAZORPAY_KEY_ID")
        razorpay_secret = os.getenv("RAZORPAY_KEY_SECRET")
        
        try:
            client = razorpay.Client(auth=(razorpay_key, razorpay_secret))
            data = {"amount": amount, "currency": "INR", "receipt": "test_receipt"}
            payment = client.order.create(data=data)
            order_id = payment.get('id')
        except Exception as e:
            print(f"Razorpay Error: {e}")
            return rx.window_alert(f"Payment Initialization Failed. Check keys. Error: {e}")
            
        js_script = f"""
        var options = {{
            "key": "{razorpay_key}",
            "amount": "{amount}",
            "currency": "INR",
            "name": "AI Recommendation System",
            "description": "Test Payment",
            "order_id": "{order_id}",
            "handler": function (response){{
                window.location.href = "/payment-success";
            }},
            "theme": {{
                "color": "#3b82f6"
            }}
        }};
        var rzp1 = new Razorpay(options);
        rzp1.on('payment.failed', function (response){{
            alert("Payment failed: " + response.error.description);
        }});
        rzp1.open();
        """
        return rx.call_script(js_script)
