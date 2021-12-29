import datetime
from dateutil import parser


def date_fmt(date: str, days: int) -> str:
    """Adds days to the provided date."""

    current_date = parser.parse(date)

    end_date = current_date + datetime.timedelta(days=days)

    return str(end_date.isoformat())
