# Write your MySQL query statement below
select distinct t.email from
(select email,row_number() over (partition by email order by email) as r1 from person) as t where t.r1 > 1