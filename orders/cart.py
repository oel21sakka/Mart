from decimal import Decimal

class Cart:
    
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart
    
    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product['id'])
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0, 'price':product['price'], 'product':product}
        if override_quantity:
            self.cart[product_id]['quantity']=quantity
        else:
            self.cart[product_id]['quantity']+=quantity
        self.cart[product_id]['total_price'] = str(int(self.cart[product_id]['quantity']) * Decimal(product['price']))
        self.save()
        return self.cart[product_id]
    
    def remove(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()
    
    def save(self):
        self.session.modified=True
    
    def __iter__(self):
        for item in self.cart.values():
            yield item
    
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_price(self):
        return sum(Decimal(item['total_price']) for item in self.cart.values())
    
    def clear(self):
        del self.session['cart']
        self.save()