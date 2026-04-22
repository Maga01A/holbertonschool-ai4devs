import time

def log_cart_creation(cart):
    """Logs the status of a shopping cart"""
    print(f"Cart currently holds {len(cart)} items.")

def validate_item(item):
    """Ensures the item is a valid string"""
    if not isinstance(item, str) or not item:
        raise ValueError("Item name must be a valid string")

def add_item_to_cart(item, cart=[]):
    """
    Adds an item to the user's shopping cart.
    If no cart is provided, a fresh one should be created.
    """
    validate_item(item)
    print(f"Adding '{item}' to the shopping cart...")
    
    # BUG: Mutable default argument causes data to persist across calls
    cart.append(item)
    
    log_cart_creation(cart)
    return cart

if __name__ == "__main__":
    user1_cart = add_item_to_cart("Laptop")
    user2_cart = add_item_to_cart("Smartphone")
    # user2_cart will incorrectly contain the Laptop as well
