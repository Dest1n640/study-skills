import argparse
import sys

from orders import submit_order
from storage import MemoryStore


def run(argv, store_factory=MemoryStore):
    parser = argparse.ArgumentParser()
    parser.add_argument("sku")
    parser.add_argument("quantity", type=int)
    args = parser.parse_args(argv)
    return submit_order(args.sku, args.quantity, store_factory)


if __name__ == "__main__":
    print(run(sys.argv[1:]))
