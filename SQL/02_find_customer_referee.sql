-- Problem: Find Customer Referee
-- Link: https://leetcode.com/problems/find-customer-referee/
-- Difficulty: Easy

-- Approach:
-- Select customers where referee_id is not 2 or is NULL

select name 
from customer 
where  referee_id !=2 or referee_id is null
