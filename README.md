# Dosa Restaurant Order Processor

A dosa restaurant has a year of individual orders saved in a JSON file, but nothing else. This script reads that file and builds two summaries from it: a list of customers and a list of menu items with how often each one was ordered.

## What it produces

Running the script creates two files in the current directory.

**`customers.json`** maps each customer's phone number to their name. Both are strings, and the phone number is in the form `xxx-xxx-xxxx`.

```json
{
    "732-555-5509": "Damodhar",
    "609-555-2301": "Tom"
}
```

**`items.json`** maps each menu item's name to its price and the number of times it was ordered.

```json
{
    "Butter Masala Dosa": {
        "price": 12.95,
        "orders": 3632
    },
    "Sada Dosa": {
        "price": 9.95,
        "orders": 1233
    }
}
```

## Input format

The script expects a JSON file containing a list of orders. Each order looks like this:

```json
{
    "timestamp": 1702219784,
    "name": "Damodhar",
    "phone": "732-555-5509",
    "items": [
        {"name": "Cheese Madurai Masala Dosa", "price": 13.95},
        {"name": "Onion Chilli Masala Dosa", "price": 11.95}
    ],
    "notes": "extra spicy"
}
```

Only `name`, `phone` and `items` are used. `timestamp` and `notes` are ignored. A sample file, `example_orders.json`, is included in this repo (10,000 orders).

## How to run it

You need Python 3.6 or newer. There is nothing to install because the script only uses the standard library.

```
python process_orders.py example_orders.json
```

The file name is a positional argument, so you can point the script at any orders file in the same format. To see the built-in help:

```
python process_orders.py --help
```

If `customers.json` or `items.json` already exist in the folder, they get overwritten.

## How it works

The script is split into a few small functions so each one does one job:

- `load_orders(path)` opens the JSON file and returns the list of orders.
- `build_customers(orders)` builds the phone-to-name dictionary. Since the phone number is the key, a customer who orders many times only shows up once.
- `build_items(orders)` goes through every item in every order. It keeps a dictionary of prices and uses a `collections.Counter` to count how many times each item name appears.
- `write_json(data, path)` writes a dictionary to a file with 4-space indentation so the output is easy to read.
- `main()` reads the command line with `argparse`, then calls the functions above.

The `if __name__ == "__main__":` guard at the bottom means the functions can be imported and tested without running the whole script.

## Assumptions

- A phone number always belongs to one customer, and an item name always has one price. That is true for the sample data. If an item's price did change partway through the year, the script would keep the last price it saw.
- The input file is valid JSON in the format shown above. The script does not try to recover from malformed input.

## Files in this repo

| File | Purpose |

| `process_orders.py` | The script |
| `example_orders.json` | Sample orders to test with |
| `README.md` | This file |
| .gitignore | Keeps the generated JSON files out of the repo |