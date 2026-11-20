CREATE TABLE IF NOT EXISTS quotes (
    date   TEXT NOT NULL,
    code   TEXT NOT NULL,
    name   TEXT NOT NULL,
    market TEXT NOT NULL,
    previous_close INTEGER NOT NULL
        CHECK (previous_close > 0),
    close  INTEGER NOT NULL
        CHECK (close > 0),
    volume INTEGER NOT NULL
        CHECK (volume >= 0),
    PRIMARY KEY (date, code)
);
