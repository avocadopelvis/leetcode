# https://leetcode.com/problems/find-customer-referee/

# check leetcode solution for explanation

SELECT name
FROM Customer
WHERE referee_id <> 2 OR referee_id IS NULL;




