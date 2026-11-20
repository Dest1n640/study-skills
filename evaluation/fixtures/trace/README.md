# Submit an order

The CLI submits an order for a stock code and positive quantity. Run `python3 -B cli.py A7 2` to place an order in an in-memory store. The command prints the result and the store lasts only for the process.

The price for each unit is 150. A zero or negative quantity must return status 422 before saving anything. Run `python3 -B -m unittest -v` to check the example.
