# https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/

# get customer ids and the count of the visit ids of the customers that are not in "Transactions"
SELECT customer_id, COUNT(v.visit_id) AS count_no_trans
FROM Visits v
LEFT JOIN Transactions t
ON v.visit_id = t.visit_id
WHERE t.visit_id IS NULL
GROUP BY v.customer_id


