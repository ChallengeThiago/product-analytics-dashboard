"""Reusable product analytics metrics for a lightweight dashboard."""

from __future__ import annotations

import pandas as pd


def _normalized(events: pd.DataFrame) -> pd.DataFrame:
    required = {"user_id", "event", "timestamp"}
    missing = required - set(events.columns)
    if missing:
        raise ValueError(f"missing columns: {sorted(missing)}")
    result = events.copy()
    result["timestamp"] = pd.to_datetime(result["timestamp"], utc=True).dt.tz_localize(None)
    return result


def build_funnel(events: pd.DataFrame, stages: list[str]) -> dict[str, int]:
    data = _normalized(events)
    return {stage: int(data.loc[data["event"].eq(stage), "user_id"].nunique()) for stage in stages}


def daily_active_users(events: pd.DataFrame) -> pd.Series:
    data = _normalized(events)
    return data.assign(day=data["timestamp"].dt.normalize()).groupby("day")["user_id"].nunique()


def retention_by_week(events: pd.DataFrame) -> pd.DataFrame:
    data = _normalized(events)
    data["cohort_week"] = data.groupby("user_id")["timestamp"].transform("min").dt.to_period("W").astype(str)
    data["active_week"] = data["timestamp"].dt.to_period("W").astype(str)
    return (
        data.groupby(["cohort_week", "active_week"])["user_id"]
        .nunique()
        .rename("retained_users")
        .reset_index()
    )
