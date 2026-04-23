-- Problem: Big Countries
-- Link: https://leetcode.com/problems/big-countries/
-- Difficulty: Easy

-- Approach:
-- Filter countries with area >= 3000000 OR population >= 25000000

select name , population , area 
from World
where area>= 3000000 or population>= 25000000
