from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

def cart_summary(request):
    # Grab our cart
    cart = Cart(request)
    cart_products = cart.get_prods
    return render(request, "cart_summary.html", {"cart_products": cart_products})

def cart_add(request):
    # Get cart
    cart = Cart(request)
    # Check for POST
    if request.POST.get("action") == "post":
        # Get stuff
        product_id = int(request.POST.get("product_id"))
        # Lookup product in the DB
        product = get_object_or_404(Product, id=product_id)
        # Save to session
        cart.add(product=product)

        # Get cart quantity
        cart_quantity = cart.__len__()


        # Return response
        # response = JsonResponse({"Product Name: " : product.name})
        response = JsonResponse({"qty" : cart_quantity})

        return response


def cart_delete(request):
    pass

def cart_update(request):
    pass