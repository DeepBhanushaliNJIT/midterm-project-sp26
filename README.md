# Dosa Restaurant Order Processor

## What it does
Reads a year of restaurant orders (JSON) and produces two summary files:

- `customers.json` – maps each customer's phone number (`xxx-xxx-xxxx`) to their name.
- `items.json` – maps each menu item name to its `price` and the number of times it was `orders`-ed.

## Design
`process_orders.py` is split into small functions:

- `load_orders(path)` reads the input JSON.
- `build_customers(orders)` builds a phone -> name dict (repeat customers collapse to one key).
- `build_items(orders)` walks every item in every order, using a `collections.Counter` for order counts and a dict for prices.
- `write_json(data, path)` writes output files.
- `main()` parses the command line with `argparse` and ties it together.

Each order is expected to have `name`, `phone`, and `items` (a list of `{name, price}`).

## Usage
```
python process_orders.py example_orders.json
```
Requires Python 3.6+ and no third-party packages. `customers.json` and `items.json` are written to the current directory.