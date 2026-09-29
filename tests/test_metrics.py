import unittest

import pandas as pd

from src.metrics import build_funnel, daily_active_users, retention_by_week


class ProductAnalyticsTests(unittest.TestCase):
    def setUp(self):
        self.events = pd.DataFrame(
            [
                {"user_id": "u1", "event": "signup", "timestamp": "2025-01-01"},
                {"user_id": "u1", "event": "activated", "timestamp": "2025-01-02"},
                {"user_id": "u1", "event": "purchase", "timestamp": "2025-01-08"},
                {"user_id": "u2", "event": "signup", "timestamp": "2025-01-01"},
                {"user_id": "u2", "event": "activated", "timestamp": "2025-01-03"},
            ]
        )

    def test_funnel_counts_unique_users_by_stage(self):
        self.assertEqual(build_funnel(self.events, ["signup", "activated", "purchase"]),
                         {"signup": 2, "activated": 2, "purchase": 1})

    def test_daily_active_users(self):
        result = daily_active_users(self.events)
        self.assertEqual(result.loc[pd.Timestamp("2025-01-01")], 2)

    def test_retention_has_cohort_and_week_columns(self):
        result = retention_by_week(self.events)
        self.assertIn("cohort_week", result.columns)
        self.assertIn("retained_users", result.columns)


if __name__ == "__main__":
    unittest.main()
