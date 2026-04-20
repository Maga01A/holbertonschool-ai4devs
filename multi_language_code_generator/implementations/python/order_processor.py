def process_order(item, price, quantity):
    total = price * quantity
    status = "Processed" if total > 0 else "Invalid"
    return {
        "item": item,
        "total": total,
        "status": status
    }

if __name__ == "__main__":
    print(process_order("Laptop", 1200, 2))
