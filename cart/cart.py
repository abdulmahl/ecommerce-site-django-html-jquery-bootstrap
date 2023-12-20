from  store.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session
        # Get current session if it exists.
        cart = self.session.get("session_key")
        # If session key doesn't exist create one.
        if "session_key" not in request.session:
            cart = self.session["session_key"] = {}

        # Make cart accessible on the pages of the site.
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        # Logic
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {"Price: " : str(product.price)}
            self.cart[product_id] = str(product_qty)

        self.session.modified = True

    def __len__(self):
        return len(self.cart)
    

    def get_prods(self):
        # Get ids from cart
        product_ids = self.cart.keys()
        # Use ids to lookup objects in the DB model.
        products = Product.objects.filter(id__in=product_ids)
        # Return looked products.
        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

        # Get cart.
        ourcart = self.cart
        # Update dictionary/cart
        ourcart[product_id] = product_qty

        self.session.modified = True

        thing = self.cart
        return thing
    