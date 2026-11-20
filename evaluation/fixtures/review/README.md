# Order report exercise

Build a report for selected order IDs in the order requested. Include an order only if its total is strictly positive and it is not void. Report the count as the number of included rows.

The report is built for large batches with many distinct requested IDs, so a scan of the order list for every ID can matter. Across the storage boundary call `save(rows)`. Callers may provide any store with that method.

Run `python3 -B -m unittest -v` in this directory.
