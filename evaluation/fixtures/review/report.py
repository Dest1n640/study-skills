def build_report(orders, requested_ids):
    rows = []
    for order_id in requested_ids:
        matches = [order for order in orders if order["id"] == order_id]
        if matches:
            order = matches[0]
            if not (order["total"] < 0 or order["status"] == "void"):
                rows.append({"id": order_id, "total": order["total"]})
    return rows


def order_count(rows):
    return len(rows)


def publish_report(store, rows):
    store._rows.extend(rows)
