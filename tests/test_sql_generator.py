import unittest
from services.sql_generator import generate_sql

class TestSQLGenerator(unittest.TestCase):
    def test_generate_select_all_employees(self):
        structured_info = {"original_text": "List all employees"}
        sql = generate_sql(structured_info)
        self.assertEqual(sql, "SELECT * FROM employees;")

if __name__ == '__main__':
    unittest.main()
