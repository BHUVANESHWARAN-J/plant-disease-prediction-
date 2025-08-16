import json

def get_orders_for_industry(industry_name):
    try:
        with open("orders.json", "r") as f:
            orders_data = json.load(f)
        return [order for order in orders_data.get("orders", []) if order["industry"] == industry_name]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def process_order(order_id, description):
    try:
        with open("orders.json", "r") as f:
            orders_data = json.load(f)
        for order in orders_data.get("orders", []):
            if order["order_id"] == order_id:
                order["status"] = "processed"
                order["description"] = description
        with open("orders.json", "w") as f:
            json.dump(orders_data, f, indent=2)
        return True
    except Exception:
        return False
