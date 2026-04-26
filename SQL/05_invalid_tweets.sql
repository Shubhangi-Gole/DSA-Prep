-- Problem: Invalid Tweets
-- Link: https://leetcode.com/problems/invalid-tweets/
-- Difficulty: Easy

-- Approach:
-- Find tweets where content length > 15

select tweet_id 
from Tweets 
where length(content)>15
