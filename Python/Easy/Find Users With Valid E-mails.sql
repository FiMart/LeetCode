# Write your MySQL query statement below
select *
from users
where mail regxpl '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'