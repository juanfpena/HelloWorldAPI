"""Function used to process the services/date-fmt endpoint."""
import datetime


def dateCalculator_func(current_date: str, days: int) -> str:
    """Takes a current date and adds a delta of n days to it."""

    end_date = current_date + datetime.timedelta(days=days)

    return str(end_date.isoformat())
