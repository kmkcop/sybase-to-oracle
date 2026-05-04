CREATE MATERIALIZED VIEW active_employees
AS
SELECT emp_id, first_name, hire_date
FROM employee
WHERE active = 1
GO