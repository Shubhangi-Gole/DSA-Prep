-- Problem: Article Views I
-- Link: https://leetcode.com/problems/article-views-i/
-- Difficulty: Easy

-- Approach:
-- Find authors who viewed their own articles
-- Use DISTINCT to avoid duplicates

select distinct author_id as id 
from Views 
where author_id=viewer_id 
order by author_id 
