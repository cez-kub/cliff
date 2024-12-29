import unittest
import sys
import os
# Add the 'scripts' folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))
from parser import parse_case_statements, parse_window_functions, parse_calendar_functions, parse_dynamic_sql

class TestParser(unittest.TestCase):
    def test_parse_case_statements(self):
        query = """
        SELECT 
            user_id,
            CASE 
                WHEN age > 18 THEN 'Adult'
                ELSE 'Minor'
            END AS age_group
        FROM users;
        """
        result = parse_case_statements(query)
        self.assertEqual(result, ["WHEN age > 18 THEN 'Adult'\n        ELSE 'Minor'"])

    def test_parse_window_functions(self):
        query = """
        SELECT
            user_id,
            ROW_NUMBER() OVER (PARTITION BY region ORDER BY sales DESC) AS rank
        FROM sales_data;
        """
        result = parse_window_functions(query)
        self.assertEqual(result, [('ROW_NUMBER()', 'PARTITION BY region ORDER BY sales DESC')])

    def test_parse_calendar_functions(self):
        query = """
        SELECT 
            DATEADD(day, 7, GETDATE()) AS next_week,
            DATEDIFF(day, '2024-01-01', GETDATE()) AS days_diff
        """
        result = parse_calendar_functions(query)
        self.assertEqual(result, [('DATEADD', 'day, 7, GETDATE()'), ('DATEDIFF', 'day, \'2024-01-01\', GETDATE()')])

    def test_parse_dynamic_sql(self):
        query = """
        DECLARE @query NVARCHAR(MAX);
        SET @query = 'SELECT * FROM ' + @table_name;
        EXEC sp_executesql @query;
        """
        result = parse_dynamic_sql(query)
        self.assertEqual(result, ["'SELECT * FROM ' + @table_name"])

if __name__ == '__main__':
    unittest.main()
