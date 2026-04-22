import time

def log_cart(cart):
    # Helper to print cart size
    print(f"Current cart size: {len(cart)}")

def add_item_to_cart(item, cart=[]):
    """
    Adds an item to the shopping cart.
    Intended Behavior: Create a fresh cart for each new user if one is not provided.
    """
    print(f"Adding '{item}' to cart...")
    # BUG: Mutable default argument causes data to persist across calls
    cart.append(item)
    log_cart(cart)
    return cart

if __name__ == "__main__":
    user1 = add_item_to_cart("Apple")
    user2 = add_item_to_cart("Banana")
    # user2 cart will unexpectedly contain 'Apple' as well
