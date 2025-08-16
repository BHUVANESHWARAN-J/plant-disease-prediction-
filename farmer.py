import json
import uuid
from datetime import datetime

def place_order(farmer, industry, product, quantity):
    # Load existing orders
    try:
        with open("orders.json", "r") as f:
            orders_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        orders_data = {"orders": []}

    # Generate unique order ID
    order_id = str(uuid.uuid4())[:8]

    # Alternatively, use incremental numeric ID (uncomment if preferred)
    # order_id = len(orders_data["orders"]) + 1

    # Create new order
    new_order = {
        "order_id": order_id,
        "farmer": farmer,
        "industry": industry,
        "product": product,
        "quantity": quantity,
        "status": "pending",
        "timestamp": str(datetime.now())
    }

    orders_data["orders"].append(new_order)

    # Save back to file
    with open("orders.json", "w") as f:
        json.dump(orders_data, f, indent=2)
