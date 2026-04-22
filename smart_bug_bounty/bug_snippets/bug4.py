def add_item_to_cart(item, cart=[]):
    # BUG: Mutable default argument causes data to persist across calls
    cart.append(item)
    return cart
