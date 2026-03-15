def validate_records(records, schema):
    """
    Validate records against a schema definition.
    """
    results = []

    for i, record in enumerate(records):
        errors = []

        for col_def in schema:
            col = col_def["column"]
            expected_type = col_def["type"]
            nullable = col_def.get("nullable", True)

            # Missing column
            if col not in record:
                errors.append(f"{col}: missing")
                continue

            value = record[col]

            # Null check
            if value is None:
                if not nullable:
                    errors.append(f"{col}: null")
                continue

            # Type check
            actual_type = type(value).__name__

            if expected_type == "int":
                if type(value) is not int:
                    errors.append(f"{col}: expected int, got {actual_type}")
                    continue

            elif expected_type == "float":
                if type(value) not in (int, float):
                    errors.append(f"{col}: expected float, got {actual_type}")
                    continue

            elif expected_type == "str":
                if type(value) is not str:
                    errors.append(f"{col}: expected str, got {actual_type}")
                    continue

            # Range check
            if expected_type in ("int", "float"):
                if "min" in col_def and value < col_def["min"]:
                    errors.append(f"{col}: out of range")
                elif "max" in col_def and value > col_def["max"]:
                    errors.append(f"{col}: out of range")

        results.append((i, len(errors) == 0, errors))

    return results