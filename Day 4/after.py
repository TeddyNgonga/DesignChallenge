from decimal import Decimal
from dataclasses import dataclass
from enum import StrEnum, auto
from typing import Iterable


class OrderType(StrEnum):
    ONLINE = auto()
    IN_STORE = auto()


@dataclass
class Item:
    name: str
    price: Decimal


@dataclass
class Order:
    id: int
    type: OrderType
    customer_email: str


@dataclass
class Email:
    body: str
    subject: str
    recipient: str
    sender: str

SHOP_EMAIL = "sales@webshop.com"

def calculate_total_price(items: Iterable[Item]) -> Decimal:
    total_price = Decimal(sum(item.price for item in items))
    return total_price


def calculate_discounted_price(items: Iterable[Item], discount: Decimal) -> Decimal:
    total_price = calculate_total_price(items)
    discounted_price = total_price - (total_price * discount)
    return discounted_price

def generate_email(order: Order, body: str, subject: str, sender: str) -> Email:
    return Email(
        body=body,
        subject=subject,
        recipient=order.customer_email,
        sender=sender
    )


def generate_order_confirmation_email(order: Order) -> Email:
    return Email(
        body=f"Thank you for your order! Your order #{order.id} has been confirmed.",
        subject="Order Confirmation",
        recipient=order.customer_email,
        sender=SHOP_EMAIL,
    )


def generate_order_shipping_notification(order: Order) -> Email:
    return Email(
        body=f"Good news! Your order #{order.id} has been shipped and is on its way.",
        subject="Order Shipped",
        recipient=order.customer_email,
        sender=SHOP_EMAIL,
    )

def process_order(order: Order) -> None:
    print(f"Processing {order.type} order...")
    print(generate_order_confirmation_email(order))
    if order.type == OrderType.ONLINE:
        print("Shipping the order...")
        print(generate_order_shipping_notification(order))
    else:
        print("Order ready for pickup.")
    
    print("Order processed successfully.")


def main() -> None:
    items = [
        Item(name="T-Shirt", price=Decimal("19.99")),
        Item(name="Jeans", price=Decimal("49.99")),
        Item(name="Shoes", price=Decimal("79.99")),
    ]

    online_order = Order(
        id=123, type=OrderType.ONLINE, customer_email="sarah@gmail.com"
    )

    total_price = calculate_total_price(items)
    print("Total price:", total_price)

    discounted_price = calculate_discounted_price(items, Decimal("0.1"))
    print("Discounted price:", discounted_price)

    process_order(online_order)

    in_store_order = Order(
        id=456, type=OrderType.IN_STORE, customer_email="john@gmail.com"
    )

    process_order(in_store_order)


if __name__ == "__main__":
    main()
