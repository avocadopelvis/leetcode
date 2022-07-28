# https://leetcode.com/problems/fix-names-in-a-table/

# Explanation:
# https://leetcode.com/problems/fix-names-in-a-table/discuss/1963494/Detailed-explanation-of-QUERY-and-Functions-that-are-required-to-solve-this

SELECT user_id, CONCAT(UPPER(SUBSTR(name, 1, 1)), LOWER(SUBSTR(name, 2))) AS name
FROM users
ORDER BY user_id


