# Write your MySQL query statement below
SELECT d.name AS department, e.name AS employee, salary
FROM
    Employee AS e
    JOIN Department AS d ON e.departmentId = d.id
WHERE
    (d.id, salary) IN (
        SELECT d.id, MAX(salary)
        FROM Employee AS e
        JOIN Department AS d ON e.departmentId = d.id
        GROUP BY d.id
    )