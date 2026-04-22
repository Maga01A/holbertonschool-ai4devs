import time

def log_cart(cart):
    # Helper to print cart size
    print(f"Current cart size: {len(cart)}")

def add_item_to_cart(item, cart=None):
    # FIXED: Using None as default to avoid mutable default arg issue
    if cart is None:
        cart = []
        
    print(f"Adding '{item}' to cart...")
    cart.append(item)
    
    log_cart(cart)
    return cart

if __name__ == "__main__":
    user1 = add_item_to_cart("Apple")
    user2 = add_item_to_cart("Banana")
    # user2 cart now correctly contains ONLY 'Banana'
    print("User 1 Cart:", user1)
    print("User 2 Cart:", user2)
