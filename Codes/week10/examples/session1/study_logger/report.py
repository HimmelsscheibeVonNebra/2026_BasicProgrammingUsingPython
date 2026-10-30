"""Turning results into text for the screen."""


def format_totals(totals):
    """Return one line per course, largest total first: "python   90 min"."""
    ordered = sorted(totals.items(), key=lambda item: item[1], reverse=True)
    return [f"{course:<8}{minutes:>4} min" for course, minutes in ordered]
