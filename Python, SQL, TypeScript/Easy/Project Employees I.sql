# Write your MySQL query statement below
select project_id, round(avg(experience_years), 2) as average_years
from
    Project
    join employee using (employee_id)
group by 1