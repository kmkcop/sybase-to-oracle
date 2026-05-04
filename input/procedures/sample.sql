CREATE PROCEDURE update_employee_status @emp_id INT, @active BIT
AS
BEGIN
    UPDATE employee
    SET active = @active
    WHERE emp_id = @emp_id
END
GO