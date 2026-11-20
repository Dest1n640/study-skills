import unittest

from cli import run


class StubStore:
    def save(self, order):
        return "test-order"


class TraceTests(unittest.TestCase):
    def test_order_response_with_stub(self):
        result = run(["A7", "2"], StubStore)
        self.assertEqual(result, {"status": 201, "id": "test-order", "total": 300})

    def test_rejects_zero_quantity(self):
        self.assertEqual(run(["A7", "0"], StubStore), {"status": 422})
