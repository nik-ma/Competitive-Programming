# Write your MySQL query statement below
SELECT MAX(SALARY) AS SecondHighestSalary from Employee where (salary<(select max(salary) from Employee))