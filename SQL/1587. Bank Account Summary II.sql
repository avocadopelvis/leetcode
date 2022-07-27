# https://leetcode.com/problems/bank-account-summary-ii/

# Note:
# Here, we use SUM which is an aggregate function
# Therefore, WHERE keyword cannot be used with aggregate functions

SELECT u.name, SUM(t.amount) AS balance
FROM Users u
JOIN Transactions t
ON u.account = t.account
GROUP BY t.account
HAVING balance > 10000


