# Cliff: SQL Translation Tool

Cliff is a tool to parse and transform T-SQL queries into Spark SQL, reducing manual translation efforts for complex SQL transformations.

## Features

- **Case Statement Parsing and Transformation**:
  Parses T-SQL `CASE` statements and transforms them into Spark SQL equivalents.

- **Window Functions**:
  Detects and translates T-SQL window functions to Spark SQL.

- **Calendar Functions**:
  Maps T-SQL functions like `DATEADD`, `DATEDIFF`, and `GETDATE` to Spark SQL equivalents.

- **Dynamic SQL**:
  Identifies dynamic SQL constructs for review or custom handling.

## New Feature: `translate_identifiers`

The `translate_identifiers` function translates T-SQL-specific quoting conventions (e.g., `[]` for identifiers, `"` for quoted identifiers) into Spark SQL's backticks (`` ` ``). This ensures identifiers in T-SQL queries are correctly translated to Spark SQL, which uses backticks for quoting table and column names.

### How It Works
- **T-SQL Identifiers**: T-SQL allows table and column names to be enclosed in `[]` or `"`. In Spark SQL, backticks (`` ` ``) are used instead.
- **String Literals**: The function does not modify string literals in single quotes (`'`) as they are already valid in Spark SQL.
  

## How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/cliff.git
    cd cliff
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run tests:
    ```bash
    python -m unittest discover tests
    ```