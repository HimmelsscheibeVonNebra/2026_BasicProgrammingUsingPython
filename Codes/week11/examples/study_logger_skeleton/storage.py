"""Reading and writing data/study.csv. The only module that touches the disk."""


def load_records(path):
    """Return every row of the CSV file as a record dict.

    minutes is converted to int. A missing file returns [].
    """
    # TODO (week 11, F2): implement with csv.DictReader.
    return []


def append_record(path, record):
    """Append one record to the CSV file, writing the header if the file is new."""
    raise NotImplementedError("append_record")
