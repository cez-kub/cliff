import re

def parse_case_statements(query: str):
    """Parse T-SQL CASE statement."""
    case_pattern = re.compile(r"CASE\s+(.*?)\s+END", re.DOTALL)
    cases = re.findall(case_pattern, query)

    # Normalize whitespace for consistent formatting
    formatted_cases = []
    for case in cases:
        lines = case.split("\n")
        normalized_lines = [line.strip() for line in lines if line.strip()]
        formatted_case = "\n        ".join(normalized_lines)  # Indent subsequent lines
        formatted_cases.append(formatted_case)
    return formatted_cases


def parse_window_functions(query: str):
    """Parse T-SQL window functions."""
    window_function_pattern = re.compile(r"(\w+\([^)]*\))\s+OVER\s*\((.*?)\)", re.DOTALL)
    window_functions = re.findall(window_function_pattern, query)
    return window_functions

def parse_calendar_functions(query: str):
    """Parse T-SQL date functions like DATEADD, DATEDIFF."""
    # Ensure capturing of the full argument list including closing parenthesis
    date_function_pattern = re.compile(r"(DATEADD|DATEDIFF|GETDATE)\((.*?)\)", re.DOTALL)
    date_functions = re.findall(date_function_pattern, query)
    return [(func, args.rstrip(')') + ')') for func, args in date_functions]

def parse_dynamic_sql(query: str):
    """Parse T-SQL dynamic SQL."""
    dynamic_sql_pattern = re.compile(r"SET\s+@query\s*=\s*(.*?);\s*EXEC\s+sp_executesql\s+@query", re.DOTALL)
    dynamic_sql = re.findall(dynamic_sql_pattern, query)
    # Normalize whitespace in the extracted dynamic SQL
    return [sql.strip() for sql in dynamic_sql]
