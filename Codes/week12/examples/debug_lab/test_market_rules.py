"""Contract checks; the starter intentionally fails some of these checks."""
import unittest
from market_rules import change_pct, summarize, rank_changes


class MarketRuleTests(unittest.TestCase):
    def test_daily_change(self):
        for previous, close, expected in [(100, 110, 10), (100, 90, -10), (100, 100, 0)]:
            with self.subTest(previous=previous, close=close):
                self.assertAlmostEqual(change_pct(previous, close), expected)

    def test_invalid_prices(self):
        for pair in [(0, 100), (100, -1), (True, 100), (100, "110"), (1.5, 2)]:
            with self.subTest(pair=pair), self.assertRaises(ValueError):
                change_pct(*pair)

    def test_empty_summary(self):
        self.assertEqual(summarize([]), {"count": 0, "mean": None})

    def test_nonempty_summary(self):
        result = summarize([10, -10, 0])
        self.assertEqual(result["count"], 3)
        self.assertAlmostEqual(result["mean"], 0)

    def test_rank_and_input_preservation(self):
        rows = [{"code": "000003", "change_pct": -1},
                {"code": "000002", "change_pct": 2},
                {"code": "000001", "change_pct": 2}]
        before = [dict(row) for row in rows]
        ranked = rank_changes(rows)
        self.assertEqual([row["code"] for row in ranked], ["000001", "000002", "000003"])
        self.assertEqual(rows, before)
        self.assertIsNot(ranked, rows)


if __name__ == "__main__":
    unittest.main()
