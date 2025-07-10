def generate_sql(structured_info):
    text = structured_info["original_text"].lower()
    if "employee" in text and "list" in text:
        return "SELECT * FROM employees;"
    elif "highest salary" in text:
        return "SELECT name, salary FROM employees ORDER BY salary DESC LIMIT 1;"
    else:
        return "-- Unable to generate SQL for the given input --"