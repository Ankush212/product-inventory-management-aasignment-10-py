def calculate_total_price(price, quantity):
    if price < 0:
        raise ValueError("Price cannot be negative")

    if quantity < 0:
        raise ValueError("Quantity cannot be negative")

    return price * quantity


def apply_discount(total, discount_percent):
    if total < 0:
        raise ValueError("Total cannot be negative")

    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100")
    discount = total * discount_percent / 100
    return total - discount


def check_stock(available_stock, requested_quantity):
    if available_stock < 0 or requested_quantity < 0:
        raise ValueError("Stock quantity cannot be negative")

    if available_stock >= requested_quantity:
        return "Stock is available"
    else:
        return "Stock is not available"


if __name__ == "__main__":
    tp = calculate_total_price(500, 4)
    print(f"Total Price: {tp:.2f}")

    disc_price = apply_discount(tp, 10)
    print(f"Discounted Price: {disc_price:.2f}")

    result = check_stock(10, 8)
    print(result)
