# create table.py
from dbms import con, cur

cur.execute("""
CREATE TABLE IF NOT EXISTS records (
    name TEXT NOT NULL,
    id INTEGER,
    lno INTEGER NOT NULL,
    sdate TEXT NOT NULL,
    edate TEXT,
    pr REAL,
    ramt REAL,
    rate REAL,
    no_intrst INTEGER,
    si REAL,
    PRIMARY KEY (id, lno)
)
""")

con.commit()

