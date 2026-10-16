#!/usr/bin/env python3
"""Summarize restaurant orders into customers.json and items.json."""

import argparse
import json
from collections import Counter


def load_orders(path):
    """Return the list of orders stored in the JSON file at `path`."""
    with open(path, encoding="utf-8") as file:
        return json.load(file)


def build_customers(orders):
    """Map each customer's phone number to their name."""
    return {order["phone"]: order["name"] for order in orders}


def build_items(orders):
    """Map each item name to its price and how many times it was ordered."""
    prices = {}
    counts = Counter()
    for order in orders:
        for item in order["items"]:
            prices[item["name"]] = item["price"]
            counts[item["name"]] += 1
    return {
        name: {"price": price, "orders": counts[name]}
        for name, price in prices.items()
    }


def write_json(data, path):
    """Write `data` to `path` as JSON."""
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("orders_file", help="path to a JSON file of orders")
    args = parser.parse_args()

    orders = load_orders(args.orders_file)
    write_json(build_customers(orders), "customers.json")
    write_json(build_items(orders), "items.json")


if __name__ == "__main__":
    main()
    