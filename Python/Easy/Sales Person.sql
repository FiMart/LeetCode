# Write your MySQL query statement below
select s.name
from
    SalesPerson as s
    left join Orders using (sales_id)
    left join Company as c using (com_id)
group by sales_id
having ifnull(sum(c.name = 'RED'), 0) = 0;