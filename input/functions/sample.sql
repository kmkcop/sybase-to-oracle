CREATE FUNCTION get_employee_count()
RETURNS INT
AS
BEGIN
    DECLARE @count INT
    SELECT @count = COUNT(*) FROM employee
    RETURN @count
END
GO