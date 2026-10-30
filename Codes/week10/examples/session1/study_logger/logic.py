"""Rules of the study logger. No input(), print() or open() in this file."""


def parse_minutes(text):
    """Return text as a positive whole number of minutes.

    Raises ValueError if text is not a whole number or is not above 0.
    """
    minutes = int(text)
    if minutes <= 0:
        raise ValueError(f"minutes must be positive, got {minutes}")
    return minutes


def make_record(date, course, minutes_text):
    """Return one record: {"date": str, "course": str, "minutes": int}.

    The course is stored in lower case. Raises ValueError for an empty
    course or invalid minutes.
    """
    course = course.strip().lower()
    if not course:
        raise ValueError("course must not be empty")
    return {"date": date.strip(), "course": course,
            "minutes": parse_minutes(minutes_text)}


def weekly_totals(records):
    """Return {course: total minutes} for a list of records.

    An empty list returns {}. The input list is not changed.
    """
    totals = {}
    for record in records:
        course = record["course"]
        totals[course] = totals.get(course, 0) + record["minutes"]
    return totals
