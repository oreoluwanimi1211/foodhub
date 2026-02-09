from .models import Cart
from menu.models import FoodItems

def get_cart_counter(request):
    Cart_Count = 0
    if request.user.is_authenticated:
        try:
            cart_items = Cart.objects.filter(user=request.user)
            if cart_items:
                for cart_item in cart_items:
                    Cart_Counter += cart_item.quantity
            else:
                Cart_Count = 0
        except:
            Cart_Count = 0
    return dict(Cart_Count=Cart_Count)
