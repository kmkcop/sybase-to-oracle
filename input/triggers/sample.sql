CREATE TRIGGER tr_employee_insert
ON employee
FOR INSERT
AS
BEGIN
    PRINT 'New employee inserted'
END
GO