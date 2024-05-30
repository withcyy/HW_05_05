import json

def generate_and_export_orders(orders, filename):
    with open(filename, 'w') as f:
        json.dump(orders, f)

def load_and_process_orders(filename):
    with open(filename, 'r') as f:
        orders = json.load(f)
        for order in orders:
            print(f"Processing order {order['order_id']}: {order['quantity']} {order['product']}")

orders_data = [
    {"order_id": 1, "product": "Phone", "quantity": 2},
    {"order_id": 2, "product": "Laptop", "quantity": 1},
    {"order_id": 3, "product": "Tablet", "quantity": 3}
]

generate_and_export_orders(orders_data, "orders.json")
load_and_process_orders("orders.json")
