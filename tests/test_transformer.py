import unittest
from scripts.transformer import (
    transform_case_statements,
    transform_window_functions,
    transform_calendar_functions,
    transform_dynamic_sql,
)

class TestTransformer(unittest.TestCase):
    def test_transform_case_statements(self):
        cases = ["WHEN age > 18 THEN 'Adult'\n        ELSE 'Minor'"]
        result = transform_case_statements(cases)
        self.assertEqual(result, ["CASE WHEN age > 18 THEN 'Adult'\n        ELSE 'Minor' END"])

    def test_transform_window_functions(self):
        windows = [("ROW_NUMBER()", "PARTITION BY department ORDER BY salary DESC")]
        result = transform_window_functions(windows)
        self.assertEqual(result, ["ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC)"])

    def test_transform_calendar_functions(self):
        dates = [("DATEADD", "day, 7, CURRENT_DATE()"), ("GETDATE", "")]
        result = transform_calendar_functions(dates)
        self.assertEqual(result, ["DATE_ADD(day, 7, CURRENT_DATE())", "CURRENT_TIMESTAMP()"])

    def test_transform_dynamic_sql(self):
        dynamic_sql = ["'SELECT * FROM ' + @table_name"]
        result = transform_dynamic_sql(dynamic_sql)
        self.assertEqual(result, ["-- Dynamic SQL detected: 'SELECT * FROM ' + @table_name"])
