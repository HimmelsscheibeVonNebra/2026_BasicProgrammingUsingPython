"""Rules of the study logger. No input(), print() or open() in this file.

Week 10 left the contracts. Week 11 fills the bodies, one function at a time.
"""


def parse_minutes(text):
    """Return text as a positive whole number of minutes.

    Raises ValueError if text is not a whole number or is not above 0.
    """
    raise NotImplementedError("parse_minutes")


def make_record(date, course, minutes_text):
    """Return one record: {"date": str, "course": str, "minutes": int}.

    The course is stored in lower case. Raises ValueError for an empty
    course or invalid minutes.
    """
    raise NotImplementedError("make_record")


def weekly_totals(records):
    """Return {course: total minutes} for a list of records.

    An empty list returns {}. The input list is not changed.
    """
    raise NotImplementedError("weekly_totals")
