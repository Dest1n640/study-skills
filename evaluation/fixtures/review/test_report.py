import unittest

from report import build_report, order_count, publish_report


class RecordingStore:
    def __init__(self):
        self.saved = []

    def save(self, rows):
        self.saved.extend(rows)


class ReportTests(unittest.TestCase):
    def test_excludes_zero_and_void_orders(self):
        orders = [
            {"id": 1, "total": 40, "status": "paid"},
            {"id": 2, "total": 0, "status": "paid"},
            {"id": 3, "total": 10, "status": "void"},
        ]
        self.assertEqual(build_report(orders, [1, 2, 3]), [{"id": 1, "total": 40}])

    def test_count_is_number_of_rows(self):
        self.assertEqual(order_count([]), 0)
        self.assertEqual(order_count([{"id": 1}]), 1)

    def test_publish_uses_the_storage_interface(self):
        store = RecordingStore()
        rows = [{"id": 1, "total": 40}]
        publish_report(store, rows)
        self.assertEqual(store.saved, rows)
