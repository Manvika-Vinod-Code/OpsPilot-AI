
import random
from datetime import datetime, timezone

def generate_log():
    events = {
    "payment-service": [
        {"level": "INFO", "message": "Payment processed successfully"},
        {"level": "WARNING", "message": "Payment processing is slow"},
        {"level": "ERROR", "message": "Database connection timeout"}
    ],
    "order-service": [
        {"level": "INFO", "message": "Order created successfully"},
        {"level": "WARNING", "message": "Order processing is delayed"},
        {"level": "ERROR", "message": "Order creation failed"}
    ],
    "inventory-service": [
        {"level": "INFO", "message": "Inventory updated successfully"},
        {"level": "WARNING", "message": "Inventory stock is running low"},
        {"level": "ERROR", "message": "Inventory database unavailable"}
    ]
    }   

    
    service = random.choice(list(events.keys()))
    event = random.choice(events[service])


    log = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "service": service,
        "level": event["level"],
        "message": event["message"]
    }

    return log
