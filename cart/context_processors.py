from .cart import Cart

# Create context processors for  our cart to work on all pages.
def cart(request):
    # Return default data from our cart.
    return { "cart": Cart(request) }