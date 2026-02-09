from django.shortcuts import get_object_or_404, render
from accounts.models import User
from marketplace.models import Cart
from vendor.models import Vendor
from menu.models import Category
from django.db.models import Prefetch
from menu.models import FoodItems
from django.http import HttpResponse, JsonResponse



def MarketPlace(request):
    vendors = Vendor.objects.filter(is_approved=True, user__is_active=True)[:8]
    vendor_count = vendors.count()
    context = {
        'vendors': vendors,
        'vendor_count': vendor_count,
    }
    return render(request, 'marketplace/listing.html', context)

def VendorDetails(request, vendor_slug):
    vendor = get_object_or_404(Vendor, vendor_slug=vendor_slug)
    categories = Category.objects.filter(vendor=vendor).prefetch_related(
        Prefetch(
            'fooditems',
            queryset= FoodItems.objects.filter(is_available=True)
        )
    )
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
    else:
        cart_items = None
    context = {
        'vendor': vendor,
        'categories': categories,
        'cart_items': cart_items,
    }
    return render(request, 'marketplace/VendorDetail.html', context)


def add_to_cart(request, food_id):
    if request.user.is_authenticated:
        if request.is_ajax():
            # Check if the food item exist
            try:
                fooditem = FoodItems.objects.get(id=food_id)
                # Check if the user has already added that food to the cart
                try:
                    check_cart = Cart.objects.get(user=request.user, fooditem=fooditem)
                    # increase the cart quality
                    check_cart.quantity += 1
                    check_cart.save()
                    return JsonResponse({'status': 'success', 'message':'Increase the cart quantity'})
                except:
                    check_cart = Cart.objects.create(user=request.user, fooditem=fooditem, quantity=1)
                    return JsonResponse({'status': 'success', 'message':'Increase the cart quantity'})
            except:
                return JsonResponse({'status': 'Failed', 'message':'this food does not exist'})
        else:
            return  JsonResponse({'status': 'Failed', 'message':'Invalid request!'})
    else:
         JsonResponse({'status': 'Failed', 'message':'please login to continue'})    