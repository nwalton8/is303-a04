"""
FreshCart POS System
====================
IS 303 — Day 6: Functions Unlocked

Each department fills in their functions below.
The main() function at the bottom wires everything together.

DEPARTMENTS:
  Team 1: CHECKOUT  — scan_item(), calculate_subtotal()
  Team 2: INVENTORY — check_stock(), update_stock()
  Team 3: LOYALTY   — check_membership(), apply_discount()
  Team 4: RECEIPTS  — calculate_tax(), generate_receipt()
"""

# ============================================================
# SHARED DATA — Everyone uses these (do NOT edit)
# ============================================================

INVENTORY = {
    "apple":   {"price": 1.25, "stock": 50},
    "bread":   {"price": 3.49, "stock": 30},
    "milk":    {"price": 4.99, "stock": 20},
    "cheese":  {"price": 6.75, "stock": 15},
    "chips":   {"price": 3.99, "stock": 40},
    "soda":    {"price": 1.99, "stock": 60},
    "eggs":    {"price": 5.49, "stock": 25},
    "chicken": {"price": 8.99, "stock": 10},
}

MEMBERS = {
    "M001": {"name": "Sarah Johnson",  "discount": 0.10},
    "M002": {"name": "Mike Chen",      "discount": 0.15},
    "M003": {"name": "Emma Davis",     "discount": 0.05},
}


# ============================================================
# 1: CHECKOUT — Scan items and calculate subtotal
# ============================================================

def scan_item(item_name, inventory):
    """
    Simulate scanning an item.
    Returns a dict with item details, or None if not found.
    """
    item = inventory.get(item_name)
    if item:
        return {"name": item_name, "price": item["price"]}
    else:
        return None  # Item not found
def calculate_subtotal(cart):
    """
    Calculate the subtotal of items in the cart.
    Returns the total price before discounts and tax.
    """
    return sum(item["price"] for item in cart)


# ============================================================
# 2: INVENTORY — Check and update stock levels
# ============================================================

def check_stock(item_name, inventory):
    item = inventory.get(item_name)
    if item:
        return item["stock"]
    else:
        return -1  # Item not found
def update_stock(item_name, inventory):
    item = inventory.get(item_name)
    if item and item["stock"] > 0:
        item["stock"] -= 1
        return True
    else:
        return False  # Item not found or out of stock


# ============================================================
# 3: LOYALTY — Membership lookup and discounts
# ============================================================

def check_membership(customer_id, members):
    """
    Check if a customer ID is a valid member.
    Returns member details if valid, or None if not found.
    """
    return members.get(customer_id)
def apply_discount(subtotal, discount_rate):
    """
    Apply a discount to the subtotal.
    Returns the amount discounted.
    """
    return subtotal * discount_rate


# ============================================================
# 4: RECEIPTS & TAX — Tax calculation and receipt
# ============================================================

def calculate_tax(amount, tax_rate=0.07):
    """
    Calculate sales tax on a given amount.
    Returns the tax amount.
    """
    return amount * tax_rate
def generate_receipt(cart, subtotal, discount, tax, total, customer_name):
    """
    Generate a formatted receipt string.
    Includes itemized list, totals, and customer name.
    """
    lines = []
    lines.append("\n" + "=" * 40)
    lines.append(f"Receipt for {customer_name}")
    lines.append("=" * 40)
    for item in cart:
        lines.append(f"{item['name'].title():20} ${item['price']:>6.2f}")
    lines.append("-" * 40)
    lines.append(f"{'Subtotal':20} ${subtotal:>6.2f}")
    if discount > 0:
        lines.append(f"{'Discount':20} -${discount:>6.2f}")
    lines.append(f"{'Tax':20} +${tax:>6.2f}")
    lines.append(f"{'Total':20} ${total:>6.2f}")
    lines.append("=" * 40)
    return "\n".join(lines)


# ============================================================
# MAIN — The CEO wires everything together
# (Do NOT edit until integration phase)
# ============================================================

def main():
    """
    Run the FreshCart POS system.
    This is where all department functions come together.
    """
    print("=" * 40)
    print("   Welcome to FreshCart Grocery!")
    print("=" * 40)

    cart = []

    # --- Step 1: Check membership (Team 3) ---
    customer_id = input("\nMembership ID (or Enter to skip): ").strip()
    if customer_id:
        member = check_membership(customer_id, MEMBERS)
    else:
        member = None

    if member:
        customer_name = member["name"]
        discount_rate = member["discount"]
        print(f"Welcome back, {customer_name}! "
              f"({discount_rate * 100:.0f}% member discount)")
    else:
        customer_name = "Guest"
        discount_rate = 0.0
        print("Shopping as Guest today.")

    # --- Step 2: Scan items (Team 1 + Team 2) ---
    while True:
        item = input("\nScan item (or 'done'): ").strip().lower()
        if item == "done":
            break

        # Check stock first (Team 2)
        stock = check_stock(item, INVENTORY)
        if stock <= 0:
            print(f"  Sorry, '{item}' is out of stock or not found!")
            continue

        # Scan the item (Team 1)
        scanned = scan_item(item, INVENTORY)
        if scanned is None:
            print(f"  Item '{item}' not found in system.")
            continue

        cart.append(scanned)
        update_stock(item, INVENTORY)
        print(f"  Added: {scanned['name']} — ${scanned['price']:.2f}")

    if not cart:
        print("\nNo items scanned. Goodbye!")
        return

    # --- Step 3: Calculate totals (Team 1 + Team 3 + Team 4) ---
    subtotal = calculate_subtotal(cart)
    discount = apply_discount(subtotal, discount_rate)
    after_discount = subtotal - discount
    tax = calculate_tax(after_discount)
    total = after_discount + tax

    # --- Step 4: Generate receipt (Team 4) ---
    receipt = generate_receipt(cart, subtotal, discount, tax,
                              total, customer_name)
    print(receipt)

    print("\nThank you for shopping at FreshCart!")


# --- Entry point ---
if __name__ == "__main__":
    main()



