Для `A7 2` функция `submit_order` получает `sku="A7"`, `quantity=2` и фабрику `store_factory`. После вычисления `total = 2 * 150` она выполняет две строки. [orders.py](/var/folders/8k/h7q4305x2_99njry5v0zh00h0000gn/T/study-trace-eval.mc8CS4Y7/workspaces/trace-explicit/orders.py:8)

```python
store = store_factory()
order_id = store.save({"sku": sku, "quantity": quantity, "total": total})
```

Первая строка создаёт экземпляр хранилища без аргументов. Вторая передаёт его методу `save` **один аргумент** — словарь `{"sku": "A7", "quantity": 2, "total": 300}`. Значение, которое вернёт `save`, становится `order_id`. Затем `submit_order` подставляет его в поле `"id"` ответа. [orders.py](/var/folders/8k/h7q4305x2_99njry5v0zh00h0000gn/T/study-trace-eval.mc8CS4Y7/workspaces/trace-explicit/orders.py:9)

- **При запуске CLI** фабрика по умолчанию — `MemoryStore`. У нового экземпляра `orders = []`. Метод `save` добавляет словарь в список и возвращает `len(self.orders)`. После добавления в списке один заказ, поэтому ответ содержит `"id": 1`. [cli.py](/var/folders/8k/h7q4305x2_99njry5v0zh00h0000gn/T/study-trace-eval.mc8CS4Y7/workspaces/trace-explicit/cli.py:8) · [storage.py](/var/folders/8k/h7q4305x2_99njry5v0zh00h0000gn/T/study-trace-eval.mc8CS4Y7/workspaces/trace-explicit/storage.py:1)
- **В тесте** фабрика — `StubStore`. Его `save` получает словарь, игнорирует его содержимое и возвращает строку `"test-order"`. Проверка ответа подтверждает, что эта строка попала в `"id"`. Точный состав переданного словаря виден в вызове `save` в `submit_order`. [test_trace.py](/var/folders/8k/h7q4305x2_99njry5v0zh00h0000gn/T/study-trace-eval.mc8CS4Y7/workspaces/trace-explicit/test_trace.py:6)