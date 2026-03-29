import sqlite3


def top_departments(db_path):
    """
    Task 1: Queries employees and departments to find the top 3
    departments by total salary expenditure.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = """
        SELECT d.name, SUM(e.salary) as total_salary
        FROM departments d
        JOIN employees e ON d.dept_id = e.dept_id
        GROUP BY d.name
        ORDER BY total_salary DESC
        LIMIT 3;
    """

    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


def employees_with_projects(db_path):
    """
    Task 2: Returns a list of tuples (employee_name, project_name)
    for all employees assigned to at least one project.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = """
        SELECT e.name, p.name
        FROM employees e
        INNER JOIN project_assignments pa ON e.emp_id = pa.emp_id
        INNER JOIN projects p ON pa.project_id = p.project_id;
    """

    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


def salary_rank_by_department(db_path):
    """
    Task 3: Returns employee name, department name, salary, and their
    rank within that department based on salary.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = """
        SELECT 
            e.name, 
            d.name, 
            e.salary,
            RANK() OVER(PARTITION BY e.dept_id ORDER BY e.salary DESC) as salary_rank
        FROM employees e
        JOIN departments d ON e.dept_id = d.dept_id
        ORDER BY d.name ASC, salary_rank ASC;
    """

    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


# Optional: Add this block to test your functions locally in the VS Code terminal
if __name__ == "__main__":
    db = "drill.db"
   