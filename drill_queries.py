import sqlite3


def top_departments(db_path):
    """
    Returns the top 3 departments by total salary expenditure.
    Output: List of tuples [(dept_name, total_salary), ...]
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = """
    SELECT d.name AS dept_name, SUM(e.salary) AS total_salary
    FROM employees e
    JOIN departments d ON e.dept_id = d.dept_id
    GROUP BY d.name
    ORDER BY total_salary DESC
    LIMIT 3;
    """

    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result


def employees_with_projects(db_path):
    """
    Returns all employees assigned to at least one project.
    Output: List of tuples [(employee_name, project_name), ...]
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = """
    SELECT e.name AS employee_name, p.name AS project_name
    FROM employees e
    INNER JOIN project_assignments pa ON e.emp_id = pa.emp_id
    INNER JOIN projects p ON pa.project_id = p.project_id;
    """

    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result


def salary_rank_by_department(db_path):
    """
    Returns employee salary ranking inside each department.
    Output: List of tuples [(employee_name, dept_name, salary, rank), ...]
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = """
    SELECT
        e.name AS employee_name,
        d.name AS dept_name,
        e.salary,
        RANK() OVER (
            PARTITION BY e.dept_id
            ORDER BY e.salary DESC
        ) AS rank
    FROM employees e
    JOIN departments d ON e.dept_id = d.dept_id
    ORDER BY d.name, rank;
    """

    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result
