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

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
