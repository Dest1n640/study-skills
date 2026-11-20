UNIT_PRICE = 150


def submit_order(sku, quantity, store_factory):
    if quantity < 0:
        return {"status": 422}

    total = quantity * UNIT_PRICE
    store = store_factory()
    order_id = store.save({"sku": sku, "quantity": quantity, "total": total})
    return {"status": 201, "id": order_id, "total": total}
