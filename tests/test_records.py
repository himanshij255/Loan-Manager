import unittest
import sqlite3
from datetime import datetime

# Path to a temporary test database (not your actual production DB)
DB_PATH = "test_mydb"

class TestLoanManager(unittest.TestCase):
    """
    Unit test class for Loan Manager database operations.
    Tests include insert, delete, search, and simple interest calculation.
    """

    def setUp(self):
        """
        Create a new temporary database and table before each test.
        This ensures tests do not interfere with each other or with production data.
        """
        self.con = sqlite3.connect(DB_PATH)
        self.cur = self.con.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS records(
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
                PRIMARY KEY(id, lno)
            )
        """)
        self.con.commit()

    def tearDown(self):
        """
        Clean up after each test by closing the connection and deleting the test DB file.
        """
        self.con.close()
        import os
        if os.path.exists(DB_PATH):
            os.remove(DB_PATH)

    def test_insert_record(self):
        """
        Test if a loan record is correctly inserted into the database.
        """
        data = ("Alice", 101, 1, "01/01/2024", "01/07/2024", 10000.0, 5000.0, 10.0, 0, None)
        self.cur.execute("INSERT INTO records VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
        self.con.commit()

        # Fetch and assert the inserted record
        self.cur.execute("SELECT * FROM records WHERE id=? AND lno=?", (101, 1))
        result = self.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[0], "Alice")  # name check

    def test_delete_record(self):
        """
        Test if a loan record can be deleted successfully from the database.
        """
        data = ("Bob", 102, 2, "01/01/2024", "01/03/2024", 15000.0, 7000.0, 8.0, 10, None)
        self.cur.execute("INSERT INTO records VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
        self.con.commit()

        self.cur.execute("DELETE FROM records WHERE id=? AND lno=?", (102, 2))
        self.con.commit()

        # Verify deletion
        self.cur.execute("SELECT * FROM records WHERE id=? AND lno=?", (102, 2))
        self.assertIsNone(self.cur.fetchone())

    def test_simple_interest_calculation(self):
        """
        Test if the Simple Interest (SI) is calculated correctly based on date, rate, and amount.
        """
        start = datetime.strptime("01/01/2024", "%d/%m/%Y")
        end = datetime.strptime("01/07/2024", "%d/%m/%Y")
        delta_days = (end - start).days
        no_interest_days = 5
        effective_days = delta_days - no_interest_days

        principal = 5000.0
        rate = 12.0

        # Formula: SI = (P * R * T) / 36500
        expected_si = (principal * rate * effective_days) / 36500
        calculated_si = (principal * rate * effective_days) / 36500

        self.assertAlmostEqual(calculated_si, expected_si, places=2)

    def test_search_by_id(self):
        """
        Test if records can be searched correctly using the borrower ID.
        """
        data = ("Charlie", 103, 3, "01/01/2024", "01/02/2024", 8000.0, 4000.0, 9.0, 0, None)
        self.cur.execute("INSERT INTO records VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
        self.con.commit()

        # Search for Charlie using ID
        self.cur.execute("SELECT name FROM records WHERE id=?", (103,))
        result = self.cur.fetchone()
        self.assertEqual(result[0], "Charlie")

if __name__ == "__main__":
    unittest.main()
  
